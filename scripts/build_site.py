#!/usr/bin/env python3
"""Render the EIP-7904 repricing site from ``data/`` into ``docs/``.

Data sources (all produced by ``make fetch`` + ``make gasfit``):

* ``data/raw/meta.json``                — reproducibility footer (suites, fork, run window)
* ``data/gasfit/new_gas_proposal.md``   — rendered wholesale for the new-gas page
* ``data/gasfit/*_report.md``           — parsed into filterable per-fit sections
* ``data/gasfit/glue_results.csv``      — per (client, glue_opcode) glue headline stats
* ``data/gasfit/figs/{proposal,runtime,glue}/`` — copied verbatim into ``docs/figs/``

The runtime and glue pages are the only ones with structured parsing; everything
else is either static narrative or a wholesale markdown render.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from importlib.metadata import PackageNotFoundError, version as pkg_version
from pathlib import Path

import markdown
import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
GASFIT = ROOT / "data" / "gasfit"
SRC = ROOT / "site_src"
TEMPLATES = SRC / "templates"
ASSETS = SRC / "assets"
OUT = ROOT / "docs"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "md_in_html", "toc"]


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
def md_to_html(text: str) -> str:
    # The generated reports wrap markdown tables inside raw <details> blocks. Without
    # a `markdown` attribute, md_in_html would leave that inner markdown unprocessed,
    # so tag the collapsibles before rendering.
    text = text.replace("<details>", '<details markdown="1">')
    text = text.replace("<summary>", '<summary markdown="span">')
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def strip_first_h1(text: str) -> str:
    return re.sub(r"^# .*\n", "", text, count=1)


def drop_section(text: str, heading: str) -> str:
    """Remove a ``## heading`` section up to (but not including) the next ``## ``."""
    pattern = rf"^{re.escape(heading)}\n.*?(?=^## )"
    return re.sub(pattern, "", text, count=1, flags=re.S | re.M)


def package_version(dist_name: str, fallback: str) -> str:
    try:
        return pkg_version(dist_name)
    except PackageNotFoundError:
        return fallback


def git_commit() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


# --------------------------------------------------------------------------- #
# Reproducibility metadata (footer)
# --------------------------------------------------------------------------- #
def load_meta() -> dict:
    raw = json.loads((RAW / "meta.json").read_text())
    return {
        "suites": [s["suite_hash"] for s in raw["suites"]],
        "fork": raw["query"]["fork"],
        "run_timestamp": raw["data_window"]["end"],
        "fetch_version": package_version("benchmarkoor-fetch", raw.get("package_version", "?")),
        "gasfit_version": package_version("evm-gasfit", "?"),
        "commit": git_commit(),
    }


# --------------------------------------------------------------------------- #
# Proposal table (used by the landing page for the headline takeaway)
# --------------------------------------------------------------------------- #
def parse_proposed_table() -> list[dict]:
    """Parse the ``## Proposed gas parameters`` table into rows."""
    text = (GASFIT / "new_gas_proposal.md").read_text()
    block = re.search(r"## Proposed gas parameters\n(.*?)(?=^## )", text, re.S | re.M)
    rows: list[dict] = []
    if not block:
        return rows
    for line in block.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("| -"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] in ("Gas param", ""):
            continue
        rows.append({
            "param": cells[0],
            "current": cells[1],
            "proposed": cells[2],
            "diff": cells[3],
            "diff_pct": cells[4],
        })
    return rows


# --------------------------------------------------------------------------- #
# Runtime report → filterable sections
# --------------------------------------------------------------------------- #
_DETAILS_RE = re.compile(
    r"<details><summary>(?P<client>\w+) — NNLS regression summary</summary>\s*"
    r"```\n(?P<nnls>.*?)\n```(?P<rest>.*?)</details>",
    re.S,
)


def _parse_md_table(text: str) -> dict[str, dict]:
    """Parse the per-client summary table at the top of a runtime subsection."""
    rows: dict[str, dict] = {}
    table_lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    for line in table_lines:
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("client", "") or set("".join(cells)) <= set("-: "):
            continue
        rows[cells[0]] = {
            "nobs": cells[1], "rsquared": cells[2], "coef": cells[3],
            "pvalue": cells[4], "ci": cells[5],
        }
    return rows


def _split_combo(heading: str) -> tuple[str, str]:
    m = re.match(r"(?P<test>.+?) — combo `(?P<combo>.+)`", heading)
    if m:
        return m.group("test").strip(), m.group("combo")
    return heading.strip(), "all"


def parse_runtime() -> dict:
    text = (GASFIT / "runtime_estimation_autogenerated_report.md").read_text()
    sections: list[dict] = []
    opcodes: list[str] = []

    opcode_parts = re.split(r"^## (.+)$", text, flags=re.M)
    for i in range(1, len(opcode_parts), 2):
        opcode = opcode_parts[i].strip()
        if opcode.lower() == "contents":
            continue
        opcodes.append(opcode)
        body = opcode_parts[i + 1]

        sub_parts = re.split(r"^### (.+)$", body, flags=re.M)
        for j in range(1, len(sub_parts), 2):
            test, combo = _split_combo(sub_parts[j].strip())
            sub = sub_parts[j + 1]
            table = _parse_md_table(sub)
            for m in _DETAILS_RE.finditer(sub):
                client = m.group("client")
                figs = re.findall(r"!\[\]\((figs/runtime/[^)]+)\)", m.group("rest"))
                sections.append({
                    "opcode": opcode, "test": test, "combo": combo, "client": client,
                    "nnls": m.group("nnls"), "figs": figs,
                    **table.get(client, {}),
                })

    return {
        "sections": sections,
        "opcodes": opcodes,
        "clients": sorted({s["client"] for s in sections}),
    }


# --------------------------------------------------------------------------- #
# Glue report + CSV → filterable sections
# --------------------------------------------------------------------------- #
def _parse_glue_appendix() -> list[dict]:
    """Per-client tier/joint NNLS summaries, grouped by client."""
    text = (GASFIT / "glue_opcodes_autogenerated_report.md").read_text()
    out: list[dict] = []
    client_parts = re.split(r"^## (.+)$", text, flags=re.M)
    for i in range(1, len(client_parts), 2):
        client = client_parts[i].strip()
        if client.lower() == "contents":
            continue
        body = client_parts[i + 1]
        fits: list[dict] = []
        sub_parts = re.split(r"^### (.+)$", body, flags=re.M)
        for j in range(1, len(sub_parts), 2):
            heading = sub_parts[j].strip()
            for m in re.finditer(r"```\n(.*?)\n```", sub_parts[j + 1], re.S):
                fits.append({"heading": heading, "nnls": m.group(1)})
        if fits:
            out.append({"client": client, "fits": fits})
    return out


def parse_glue() -> dict:
    gr = pd.read_csv(GASFIT / "glue_results.csv")
    sections: list[dict] = []
    for _, r in gr.iterrows():
        client, opcode = r["client_name"], r["glue_opcode"]
        figs = [
            f"figs/glue/{opcode}__{client}__{kind}.png"
            for kind in ("regression", "bootstrap", "diagnostics")
        ]
        figs = [f for f in figs if (GASFIT / f).exists()]
        sections.append({
            "client": client, "glue_opcode": opcode,
            "nobs": int(r["nobs"]),
            "glue_runtime_ms": float(r["glue_runtime_ms"]),
            "p_value": float(r["p_value"]),
            "rsquared": float(r["rsquared"]),
            "figs": figs,
        })
    return {
        "sections": sections,
        "clients": sorted(gr["client_name"].unique().tolist()),
        "glue_opcodes": sorted(gr["glue_opcode"].unique().tolist()),
        "appendix": _parse_glue_appendix(),
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def build_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["sci"] = lambda v: f"{v:.3e}"
    env.filters["g4"] = lambda v: f"{v:.4g}"
    return env


def copy_static() -> None:
    OUT.mkdir(exist_ok=True)
    # Disable GitHub Pages' Jekyll processing so files/dirs with leading
    # underscores are served verbatim instead of being silently dropped.
    (OUT / ".nojekyll").touch()
    for asset in ASSETS.iterdir():
        shutil.copy2(asset, OUT / asset.name)
    figs_src = GASFIT / "figs"
    if figs_src.exists():
        shutil.copytree(figs_src, OUT / "figs", dirs_exist_ok=True)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    env = build_env()
    meta = load_meta()
    proposed = parse_proposed_table()

    common = {"meta": meta}

    # Landing page — static narrative + headline counts.
    n_up = sum(1 for r in proposed if r["diff"].startswith("+"))
    n_down = sum(1 for r in proposed if r["diff"].startswith("-"))
    (OUT / "index.html").write_text(env.get_template("index.html").render(
        page="index", proposed=proposed, n_up=n_up, n_down=n_down, **common,
    ))

    # New-gas page — wholesale render of the proposal report.
    report = (GASFIT / "new_gas_proposal.md").read_text()
    report = drop_section(strip_first_h1(report), "## Contents")
    (OUT / "new-gas.html").write_text(env.get_template("new_gas.html").render(
        page="new-gas", report_html=md_to_html(report), **common,
    ))

    # Runtime page — filterable per-fit sections.
    (OUT / "runtime.html").write_text(env.get_template("runtime.html").render(
        page="runtime", **parse_runtime(), **common,
    ))

    # Glue page — filterable per (client, glue_opcode) sections + appendix.
    (OUT / "glue.html").write_text(env.get_template("glue.html").render(
        page="glue", **parse_glue(), **common,
    ))

    # Methodology page — static narrative, config-driven values.
    fit_cfg = yaml.safe_load((ROOT / "fit.yaml").read_text())
    (OUT / "methodology.html").write_text(env.get_template("methodology.html").render(
        page="methodology", fit=fit_cfg, **common,
    ))

    copy_static()
    print(f"Built site → {OUT}")


if __name__ == "__main__":
    main()

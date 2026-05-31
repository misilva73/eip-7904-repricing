# EIP-7904 Repricing

A static, multi-page site summarising the [EIP-7904](https://eips.ethereum.org/EIPS/eip-7904)
gas-repricing analysis. The analysis fits NNLS regressions on EVM client benchmark
runtimes to propose new gas costs for the opcodes and precompiles touched by the EIP.

**Live site:** <https://misilva73.github.io/eip-7904-repricing/>

## Pipeline

```text
benchmarkoor-fetch  →  evm-gasfit  →  build_site.py  →  docs/  (GitHub Pages)
   (data/raw/)         (data/gasfit/)     (Jinja2)
```

1. **Fetch** — `benchmarkoor-fetch` pulls the pinned benchmark suites into `data/raw/`,
   driven by [fetch.yaml](fetch.yaml).
2. **Fit** — `evm-gasfit` runs the NNLS estimation (driven by [fit.yaml](fit.yaml)) and
   emits the proposal artifacts and reports into `data/gasfit/`.
3. **Build** — `scripts/build_site.py` renders the Jinja2 templates in `site_src/` into
   `docs/`, pulling structured data (CSVs, parsed reports) from `data/gasfit/`.
4. **Deploy** — GitHub Pages serves `docs/` from `main`.

`data/` is committed alongside `docs/` so the published site is self-contained and auditable.

## Setup

Requires Python ≥ 3.11, plus `make` and `jq`.

```bash
pip install -e .          # installs benchmarkoor-fetch, evm-gasfit, jinja2, pandas
```

### Benchmarkoor token

Fetching benchmark data needs a Benchmarkoor API key. Request your own key, then create
a gitignored `secrets.json` at the repo root:

```json
{ "benchmarkoor_bearer_token": "bmk_..." }
```

The `Makefile` reads it with `jq` and exports `BENCHMARKOOR_TOKEN` before invoking
`benchmarkoor-fetch`. The token must never live in `fetch.yaml` (the config loader
rejects it).

## Running

```bash
make fetch     # → data/raw/    (reads token from secrets.json)
make gasfit    # → data/gasfit/
make site      # renders site_src/templates → docs/, copies figures
# or end-to-end:
make
```

`make clean` removes `data/` and `docs/`.

## Layout

| Path | Purpose |
| --- | --- |
| `fetch.yaml` | benchmarkoor-fetch config (pinned suites, amsterdam fork) |
| `fit.yaml` | evm-gasfit config (anchor 1e8, osaka cost table, presets, glue on) |
| `scripts/build_site.py` | renders templates → `docs/`, copies figures |
| `site_src/templates/` | Jinja2 templates (`base.html` + one per page) |
| `site_src/assets/` | `style.css`, `runtime_filter.js` |
| `data/raw/` | fetched benchmark inputs |
| `data/gasfit/` | estimation outputs (CSVs, reports, `figs/`) |
| `docs/` | generated static site (served by GitHub Pages) |

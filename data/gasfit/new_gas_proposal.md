# New gas proposal

_Generated 2026-05-31 10:29:16Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 18 parameters proposed — 15 increased, 3 decreased, 0 new, 0 unresolved · 0 warnings · 3 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| OPCODE_DIV | 5 | 6 | +1 | +20% |
| OPCODE_SDIV | 5 | 7 | +2 | +40% |
| OPCODE_MOD | 5 | 8 | +3 | +60% |
| OPCODE_SMOD | 5 | 8 | +3 | +60% |
| OPCODE_ADDMOD | 8 | 11 | +3 | +38% |
| OPCODE_MULMOD | 8 | 16 | +8 | +100% |
| OPCODE_KECCAK256_BASE | 30 | 47 | +17 | +57% |
| OPCODE_KECCAK256_PER_WORD | 6 | 7 | +1 | +17% |
| PRECOMPILE_ECRECOVER | 3000 | 4262 | +1262 | +42% |
| PRECOMPILE_BLAKE2F_BASE | 0 | 123 | +123 | n/a |
| PRECOMPILE_BLAKE2F_PER_ROUND | 1 | 2 | +1 | +100% |
| PRECOMPILE_BLS_G1ADD | 375 | 404 | +29 | +8% |
| PRECOMPILE_BLS_G2ADD | 600 | 557 | -43 | -7% |
| PRECOMPILE_ECADD | 150 | 361 | +211 | +141% |
| PRECOMPILE_ECPAIRING_BASE | 45000 | 27356 | -17644 | -39% |
| PRECOMPILE_ECPAIRING_PER_POINT | 34000 | 19322 | -14678 | -43% |
| PRECOMPILE_POINT_EVALUATION | 50000 | 125511 | +75511 | +151% |
| PRECOMPILE_P256VERIFY | 6900 | 7267 | +367 | +5% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| OPCODE_DIV | geth | 6 | besu | 2 | 3.00× |
| OPCODE_SDIV | geth | 7 | besu | 2 | 3.50× |
| OPCODE_MOD | geth | 8 | besu | 3 | 2.67× |
| OPCODE_SMOD | geth | 8 | besu | 3 | 2.67× |
| OPCODE_ADDMOD | geth | 11 | besu | 3 | 3.67× |
| OPCODE_MULMOD | geth | 16 | besu | 4 | 4.00× |
| OPCODE_KECCAK256_BASE | geth | 47 | besu | 12 | 3.92× |
| OPCODE_KECCAK256_PER_WORD | geth | 7 | nethermind | 3 | 2.33× |
| PRECOMPILE_ECRECOVER | geth | 4262 | erigon | 819 | 5.20× |
| PRECOMPILE_BLAKE2F_BASE | besu | 123 | erigon | 85 | 1.45× |
| PRECOMPILE_BLAKE2F_PER_ROUND | geth | 2 | besu | 1 | 2.00× |
| PRECOMPILE_BLS_G1ADD | geth | 404 | besu | 240 | 1.68× |
| PRECOMPILE_BLS_G2ADD | geth | 557 | besu | 271 | 2.06× |
| PRECOMPILE_ECADD | geth | 361 | besu | 128 | 2.82× |
| PRECOMPILE_ECPAIRING_BASE | geth | 27356 | reth | 8303 | 3.29× |
| PRECOMPILE_ECPAIRING_PER_POINT | geth | 19322 | nethermind | 11758 | 1.64× |
| PRECOMPILE_POINT_EVALUATION | geth | 125511 | nethermind | 23629 | 5.31× |
| PRECOMPILE_P256VERIFY | geth | 7267 | erigon | 1335 | 5.44× |

Per-client proposed gas for each parameter. Cells are colored by `log2(proposed / current)` — red means the proposal is more expensive than the current gas cost, green means cheaper, and white sits at unchanged. Annotations show the absolute proposed gas value; blank rows are parameters with no prior baseline (see warnings below).

![](figs/proposal/heatmap.png)

## Worst-case provenance per gas param

One collapsible block per gas parameter showing every per-client candidate that the worst-case selector saw. Rows are model combos (the source regression's `test_name`, `target_opcode`, `model_coef_name`, and any `model_by` factors — components constant within a parameter are dropped from the label). Cells carry each candidate's proposed gas; the cell the per-client selector picked is outlined in black. Colors are `log2(proposed / current)` against that parameter's baseline on a per-parameter symmetric scale.

_Single-combo parameters omitted (see proposal table for the sole estimation): `OPCODE_DIV`, `OPCODE_SDIV`, `OPCODE_ADDMOD`, `OPCODE_MULMOD`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`._

<details>
<summary><code>OPCODE_MOD</code> — 4 combos × 5 clients</summary>

![](figs/proposal/provenance__OPCODE_MOD.png)

</details>

<details>
<summary><code>OPCODE_SMOD</code> — 4 combos × 5 clients</summary>

![](figs/proposal/provenance__OPCODE_SMOD.png)

</details>

<details>
<summary><code>OPCODE_KECCAK256_BASE</code> — 4 combos × 5 clients</summary>

![](figs/proposal/provenance__OPCODE_KECCAK256_BASE.png)

</details>

<details>
<summary><code>OPCODE_KECCAK256_PER_WORD</code> — 4 combos × 5 clients</summary>

![](figs/proposal/provenance__OPCODE_KECCAK256_PER_WORD.png)

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_BASE</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_BLAKE2F_BASE.png)

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_PER_ROUND</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_BLAKE2F_PER_ROUND.png)

</details>

<details>
<summary><code>PRECOMPILE_ECADD</code> — 5 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECADD.png)

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_BASE</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECPAIRING_BASE.png)

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_PER_POINT</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECPAIRING_PER_POINT.png)

</details>

<details>
<summary><code>PRECOMPILE_POINT_EVALUATION</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_POINT_EVALUATION.png)

</details>

<details>
<summary><code>PRECOMPILE_P256VERIFY</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_P256VERIFY.png)

</details>

## Warnings

### Missing parameters

_None._

### Incomplete client coverage

_None._

### Missing glue adjustments

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 23 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `CALLDATALOAD` | `besu` (both), `erigon` (R²), `geth` (R²), `nethermind` (R²), `reth` (R²) | `OPCODE_ADDMOD`, `OPCODE_MOD`, `OPCODE_MULMOD`, `OPCODE_SMOD` |
| `DUP` | `nethermind` (p-value) | `OPCODE_ADDMOD`, `OPCODE_DIV`, `OPCODE_MOD`, `OPCODE_MULMOD`, `OPCODE_SDIV`, `OPCODE_SMOD` |
| `EXP` | `nethermind` (both) | — |
| `GAS` | `nethermind` (p-value) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `GT` | `nethermind` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `ISZERO` | `nethermind` (R²) | — |
| `JUMPI` | `nethermind` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `KECCAK256` | `besu` (R²), `erigon` (R²), `geth` (R²), `nethermind` (both), `reth` (both) | — |
| `LT` | `nethermind` (R²) | — |
| `MSTORE` | `reth` (R²) | `OPCODE_KECCAK256_BASE`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `PUSH0` | `nethermind` (p-value) | `OPCODE_KECCAK256_BASE` |
| `RETURNDATASIZE` | `nethermind` (R²) | — |
| `SELFBALANCE` | `besu` (R²) | — |
| `STATICCALL` | `geth` (p-value) | — |
| `SWAP` | `nethermind` (R²) | — |

</details>

## Poor-fit selections

Rows where the winning fit's p-value exceeded `modeling.poor_fit_p_value_threshold` (0.05) or its R² fell below `modeling.poor_fit_rsquared_threshold` (0.5). The failing threshold(s) are noted alongside each row; selections in `### Winners with poor fit` still drive the proposal, while `### Other weak candidates` lists losing candidates that the selector dropped in favor of a qualified alternative. See `runtime_estimation_autogenerated_report.md` for per-fit `runtime_ms`, `pvalue`, and `rsquared` metrics.

### Winners with poor fit

| Gas param | Client | Test | Target opcode | Coef | runtime_ms | pvalue | rsquared | Failed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `PRECOMPILE_BLAKE2F_PER_ROUND` | `erigon` | `test_blake2f_benchmark` | `BLAKE2F` | `num_rounds` | 3.926e-07 | 0.224 | 0.8868 | p-value |
| `PRECOMPILE_BLAKE2F_PER_ROUND` | `reth` | `test_blake2f_benchmark` | `BLAKE2F` | `num_rounds` | 0 | 1 | 0.9885 | p-value |
| `PRECOMPILE_BLS_G2ADD` | `erigon` | `test_bls12_381` | `BLS12_G2ADD` | `target_coef` | 0.001012 | 0.001 | 0.3888 | R² |

### Other weak candidates

<details>
<summary><code>PRECOMPILE_BLAKE2F_PER_ROUND</code> — 2 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_blake2f_benchmark` | `BLAKE2F` | `num_rounds` | — | `besu` (p-value) |
| `test_blake2f_uncachable` | `BLAKE2F` | `num_rounds` | — | `erigon` (p-value), `reth` (p-value) |

</details>

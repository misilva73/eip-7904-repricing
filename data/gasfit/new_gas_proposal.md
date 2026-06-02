# New gas proposal

_Generated 2026-06-02 09:40:51Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 18 parameters proposed — 1 increased, 16 decreased, 0 new, 0 unresolved · 0 warnings · 19 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| OPCODE_DIV | 5 | 2 | -3 | -60% |
| OPCODE_SDIV | 5 | 2 | -3 | -60% |
| OPCODE_MOD | 5 | 3 | -2 | -40% |
| OPCODE_SMOD | 5 | 3 | -2 | -40% |
| OPCODE_ADDMOD | 8 | 3 | -5 | -62% |
| OPCODE_MULMOD | 8 | 5 | -3 | -38% |
| OPCODE_KECCAK256_BASE | 30 | 14 | -16 | -53% |
| OPCODE_KECCAK256_PER_WORD | 6 | 3 | -3 | -50% |
| PRECOMPILE_ECRECOVER | 3000 | 1235 | -1765 | -59% |
| PRECOMPILE_BLAKE2F_BASE | 0 | 43 | +43 | n/a |
| PRECOMPILE_BLAKE2F_PER_ROUND | 1 | 1 | 0 | 0% |
| PRECOMPILE_BLS_G1ADD | 375 | 176 | -199 | -53% |
| PRECOMPILE_BLS_G2ADD | 600 | 217 | -383 | -64% |
| PRECOMPILE_ECADD | 150 | 101 | -49 | -33% |
| PRECOMPILE_ECPAIRING_BASE | 45000 | 8225 | -36775 | -82% |
| PRECOMPILE_ECPAIRING_PER_POINT | 34000 | 11543 | -22457 | -66% |
| PRECOMPILE_POINT_EVALUATION | 50000 | 33895 | -16105 | -32% |
| PRECOMPILE_P256VERIFY | 6900 | 1980 | -4920 | -71% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| OPCODE_DIV | besu | 2 | geth | 2 | 1.00× |
| OPCODE_SDIV | besu | 2 | geth | 2 | 1.00× |
| OPCODE_MOD | besu | 3 | geth | 2 | 1.50× |
| OPCODE_SMOD | besu | 3 | geth | 3 | 1.00× |
| OPCODE_ADDMOD | besu | 3 | geth | 3 | 1.00× |
| OPCODE_MULMOD | geth | 5 | besu | 4 | 1.25× |
| OPCODE_KECCAK256_BASE | geth | 14 | besu | 12 | 1.17× |
| OPCODE_KECCAK256_PER_WORD | nethermind | 3 | besu | 2 | 1.50× |
| PRECOMPILE_ECRECOVER | geth | 1235 | nethermind | 715 | 1.73× |
| PRECOMPILE_BLAKE2F_BASE | besu | 43 | reth | 39 | 1.10× |
| PRECOMPILE_BLAKE2F_PER_ROUND | besu | 1 | geth | 1 | 1.00× |
| PRECOMPILE_BLS_G1ADD | besu | 176 | geth | 116 | 1.52× |
| PRECOMPILE_BLS_G2ADD | besu | 217 | geth | 163 | 1.33× |
| PRECOMPILE_ECADD | geth | 101 | besu | 94 | 1.07× |
| PRECOMPILE_ECPAIRING_BASE | reth | 8225 | geth | 7427 | 1.11× |
| PRECOMPILE_ECPAIRING_PER_POINT | nethermind | 11543 | reth | 6178 | 1.87× |
| PRECOMPILE_POINT_EVALUATION | geth | 33895 | nethermind | 24302 | 1.39× |
| PRECOMPILE_P256VERIFY | geth | 1980 | besu | 1096 | 1.81× |

Per-client proposed gas for each parameter. Cells are colored by `log2(proposed / current)` — red means the proposal is more expensive than the current gas cost, green means cheaper, and white sits at unchanged. Annotations show the absolute proposed gas value; blank rows are parameters with no prior baseline (see warnings below).

![](figs/proposal/heatmap.png)

## Worst-case provenance per gas param

One collapsible block per gas parameter showing every per-client candidate that the worst-case selector saw. Rows are model combos (the source regression's `test_name`, `target_opcode`, `model_coef_name`, and any `model_by` factors — components constant within a parameter are dropped from the label). Cells carry each candidate's proposed gas; the cell the per-client selector picked is outlined in black. Colors are `log2(proposed / current)` against that parameter's baseline on a per-parameter symmetric scale.

_Single-combo parameters omitted (see proposal table for the sole estimation): `OPCODE_DIV`, `OPCODE_SDIV`, `OPCODE_ADDMOD`, `OPCODE_MULMOD`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`._

<details>
<summary><code>OPCODE_MOD</code> — 4 combos × 4 clients</summary>

![](figs/proposal/provenance__OPCODE_MOD.png)

</details>

<details>
<summary><code>OPCODE_SMOD</code> — 4 combos × 4 clients</summary>

![](figs/proposal/provenance__OPCODE_SMOD.png)

</details>

<details>
<summary><code>OPCODE_KECCAK256_BASE</code> — 4 combos × 4 clients</summary>

![](figs/proposal/provenance__OPCODE_KECCAK256_BASE.png)

</details>

<details>
<summary><code>OPCODE_KECCAK256_PER_WORD</code> — 4 combos × 4 clients</summary>

![](figs/proposal/provenance__OPCODE_KECCAK256_PER_WORD.png)

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_BASE</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_BLAKE2F_BASE.png)

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_PER_ROUND</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_BLAKE2F_PER_ROUND.png)

</details>

<details>
<summary><code>PRECOMPILE_ECADD</code> — 5 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECADD.png)

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_BASE</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECPAIRING_BASE.png)

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_PER_POINT</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_ECPAIRING_PER_POINT.png)

</details>

<details>
<summary><code>PRECOMPILE_POINT_EVALUATION</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_POINT_EVALUATION.png)

</details>

<details>
<summary><code>PRECOMPILE_P256VERIFY</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__PRECOMPILE_P256VERIFY.png)

</details>

## Warnings

### Missing parameters

_None._

### Incomplete client coverage

**Clients with no estimations at all:** `erigon`. These configured clients produced no fits for any gas parameter — check that the runtimes CSV contains their rows and that the fixture-name conventions match. Inspect the `evm_gasfit` warnings in `meta.json` for the cause.

These gas parameters were fit by at least one client but not by every configured client — the listed clients produced no estimation, so the worst-case value was selected from a smaller pool. Inspect the `evm_gasfit` warnings in `meta.json` for the cause.

| Gas param | Missing clients |
| --- | --- |
| `OPCODE_DIV` | `erigon` |
| `OPCODE_SDIV` | `erigon` |
| `OPCODE_MOD` | `erigon` |
| `OPCODE_SMOD` | `erigon` |
| `OPCODE_ADDMOD` | `erigon` |
| `OPCODE_MULMOD` | `erigon` |
| `OPCODE_KECCAK256_BASE` | `erigon` |
| `OPCODE_KECCAK256_PER_WORD` | `erigon` |
| `PRECOMPILE_ECRECOVER` | `erigon` |
| `PRECOMPILE_BLAKE2F_BASE` | `erigon` |
| `PRECOMPILE_BLAKE2F_PER_ROUND` | `erigon` |
| `PRECOMPILE_BLS_G1ADD` | `erigon` |
| `PRECOMPILE_BLS_G2ADD` | `erigon` |
| `PRECOMPILE_ECADD` | `erigon` |
| `PRECOMPILE_ECPAIRING_BASE` | `erigon` |
| `PRECOMPILE_ECPAIRING_PER_POINT` | `erigon` |
| `PRECOMPILE_POINT_EVALUATION` | `erigon` |
| `PRECOMPILE_P256VERIFY` | `erigon` |

### Missing glue adjustments

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 50 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `ADD` | `geth` (R²), `nethermind` (R²) | `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `AND` | `geth` (R²), `nethermind` (R²) | — |
| `CALLDATACOPY` | `geth` (R²) | `PRECOMPILE_POINT_EVALUATION` |
| `CALLDATALOAD` | `besu` (both), `geth` (R²), `nethermind` (R²), `reth` (R²) | `OPCODE_ADDMOD`, `OPCODE_MOD`, `OPCODE_MULMOD`, `OPCODE_SMOD` |
| `CALLDATASIZE` | `erigon` (p-value), `geth` (R²), `nethermind` (p-value) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `DIV` | `geth` (R²) | — |
| `DUP` | `geth` (R²), `nethermind` (p-value) | `OPCODE_ADDMOD`, `OPCODE_DIV`, `OPCODE_MOD`, `OPCODE_MULMOD`, `OPCODE_SDIV`, `OPCODE_SMOD` |
| `EXP` | `geth` (R²), `nethermind` (both) | — |
| `GAS` | `erigon` (p-value), `geth` (R²), `nethermind` (p-value) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `GT` | `geth` (R²), `nethermind` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `ISZERO` | `geth` (R²) | — |
| `JUMP` | `geth` (R²) | `OPCODE_ADDMOD`, `OPCODE_MULMOD` |
| `JUMPDEST` | `geth` (R²) | `OPCODE_ADDMOD`, `OPCODE_MULMOD`, `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `JUMPI` | `geth` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `KECCAK256` | `besu` (R²), `geth` (R²), `nethermind` (both), `reth` (both) | — |
| `LT` | `geth` (R²) | — |
| `MLOAD` | `erigon` (p-value), `geth` (R²) | `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `MSTORE` | `geth` (R²), `reth` (R²) | `OPCODE_KECCAK256_BASE`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `MSTORE8` | `geth` (R²) | — |
| `MUL` | `geth` (R²) | — |
| `PC` | `geth` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `PUSH` | `erigon` (p-value), `geth` (R²) | `OPCODE_ADDMOD`, `OPCODE_KECCAK256_BASE`, `OPCODE_MOD`, `OPCODE_MULMOD`, `OPCODE_SMOD`, `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_BLS_G1ADD`, `PRECOMPILE_BLS_G2ADD`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_ECRECOVER`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `PUSH0` | `erigon` (p-value), `geth` (both), `nethermind` (p-value) | `OPCODE_KECCAK256_BASE` |
| `RETURNDATASIZE` | `geth` (R²) | — |
| `SELFBALANCE` | `geth` (R²) | — |
| `STATICCALL` | `erigon` (p-value), `geth` (both) | — |
| `SUB` | `geth` (R²) | `PRECOMPILE_BLAKE2F_BASE`, `PRECOMPILE_ECADD`, `PRECOMPILE_ECPAIRING_BASE`, `PRECOMPILE_P256VERIFY`, `PRECOMPILE_POINT_EVALUATION` |
| `SWAP` | `geth` (R²), `nethermind` (R²) | — |

</details>

## Poor-fit selections

Rows where the winning fit's p-value exceeded `modeling.poor_fit_p_value_threshold` (0.05) or its R² fell below `modeling.poor_fit_rsquared_threshold` (0.5). The failing threshold(s) are noted alongside each row; selections in `### Winners with poor fit` still drive the proposal, while `### Other weak candidates` lists losing candidates that the selector dropped in favor of a qualified alternative. See `runtime_estimation_autogenerated_report.md` for per-fit `runtime_ms`, `pvalue`, and `rsquared` metrics.

### Winners with poor fit

| Gas param | Client | Test | Target opcode | Coef | runtime_ms | pvalue | rsquared | Failed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `OPCODE_DIV` | `geth` | `test_arithmetic` | `DIV` | `target_coef` | 1.527e-05 | 0.001 | 0.0792 | R² |
| `OPCODE_SDIV` | `geth` | `test_arithmetic` | `SDIV` | `target_coef` | 1.727e-05 | 0.001 | 0.08369 | R² |
| `OPCODE_MOD` | `geth` | `test_mod` | `MOD` | `target_coef` | 1.961e-05 | 0.001 | 0.08314 | R² |
| `OPCODE_SMOD` | `geth` | `test_mod` | `SMOD` | `target_coef` | 2.044e-05 | 0.001 | 0.08293 | R² |
| `OPCODE_ADDMOD` | `geth` | `test_mod_arithmetic` | `ADDMOD` | `target_coef` | 2.838e-05 | 0.001 | 0.08271 | R² |
| `OPCODE_MULMOD` | `geth` | `test_mod_arithmetic` | `MULMOD` | `target_coef` | 4.072e-05 | 0.001 | 0.08309 | R² |
| `OPCODE_KECCAK256_BASE` | `geth` | `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `target_coef` | 0.0001324 | 0.001 | 0.09198 | R² |
| `OPCODE_KECCAK256_PER_WORD` | `geth` | `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `msg_words` | 1.743e-05 | 0.001 | 0.09236 | R² |
| `PRECOMPILE_ECRECOVER` | `geth` | `test_ecrecover` | `ECRECOVER` | `target_coef` | 0.01235 | 0.001 | 0.1002 | R² |
| `PRECOMPILE_BLAKE2F_BASE` | `geth` | `test_blake2f_uncachable` | `BLAKE2F` | `target_coef` | 0.0001905 | 0.001 | 0.1315 | R² |
| `PRECOMPILE_BLAKE2F_PER_ROUND` | `geth` | `test_blake2f_benchmark` | `BLAKE2F` | `num_rounds` | 3.22e-06 | 0.001 | 0.1425 | R² |
| `PRECOMPILE_BLAKE2F_PER_ROUND` | `reth` | `test_blake2f_benchmark` | `BLAKE2F` | `num_rounds` | 0 | 1 | 0.9897 | p-value |
| `PRECOMPILE_BLS_G1ADD` | `geth` | `test_bls12_381` | `BLS12_G1ADD` | `target_coef` | 0.001156 | 0.001 | 0.09607 | R² |
| `PRECOMPILE_BLS_G2ADD` | `geth` | `test_bls12_381` | `BLS12_G2ADD` | `target_coef` | 0.001623 | 0.001 | 0.101 | R² |
| `PRECOMPILE_ECADD` | `geth` | `test_alt_bn128_uncachable` | `ECADD` | `target_coef` | 0.001003 | 0.001 | 0.08986 | R² |
| `PRECOMPILE_ECPAIRING_BASE` | `geth` | `test_alt_bn128_benchmark` | `ECPAIRING` | `target_coef` | 0.07427 | 0.001 | 0.08377 | R² |
| `PRECOMPILE_ECPAIRING_PER_POINT` | `geth` | `test_ec_pairing` | `ECPAIRING` | `num_pairs` | 0.06014 | 0.001 | 0.111 | R² |
| `PRECOMPILE_POINT_EVALUATION` | `geth` | `test_point_evaluation` | `POINT_EVALUATION` | `target_coef` | 0.3389 | 0.001 | 0.08376 | R² |
| `PRECOMPILE_P256VERIFY` | `geth` | `test_p256verify_uncachable` | `P256VERIFY` | `target_coef` | 0.01979 | 0.001 | 0.08597 | R² |

### Other weak candidates

<details>
<summary><code>OPCODE_MOD</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_mod` | `MOD` | `target_coef` | `param_mod_bits=191` | `geth` (R²) |
| `test_mod` | `MOD` | `target_coef` | `param_mod_bits=255` | `geth` (R²) |
| `test_mod` | `MOD` | `target_coef` | `param_mod_bits=63` | `geth` (R²) |

</details>

<details>
<summary><code>OPCODE_SMOD</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_mod` | `SMOD` | `target_coef` | `param_mod_bits=191` | `geth` (R²) |
| `test_mod` | `SMOD` | `target_coef` | `param_mod_bits=255` | `geth` (R²) |
| `test_mod` | `SMOD` | `target_coef` | `param_mod_bits=63` | `geth` (R²) |

</details>

<details>
<summary><code>OPCODE_KECCAK256_BASE</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `target_coef` | `param_mem_size=1024` | `geth` (R²) |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `target_coef` | `param_mem_size=256` | `geth` (R²) |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `target_coef` | `param_mem_size=32` | `geth` (R²) |

</details>

<details>
<summary><code>OPCODE_KECCAK256_PER_WORD</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `msg_words` | `param_mem_size=0` | `geth` (R²) |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `msg_words` | `param_mem_size=256` | `geth` (R²) |
| `test_keccak_diff_mem_msg_sizes` | `KECCAK256` | `msg_words` | `param_mem_size=32` | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_BASE</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_blake2f_benchmark` | `BLAKE2F` | `target_coef` | — | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_BLAKE2F_PER_ROUND</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_blake2f_uncachable` | `BLAKE2F` | `num_rounds` | — | `geth` (R²), `reth` (p-value) |

</details>

<details>
<summary><code>PRECOMPILE_ECADD</code> — 4 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_alt_bn128` | `ECADD` | `target_coef` | `param_bn128=add` | `geth` (R²) |
| `test_alt_bn128` | `ECADD` | `target_coef` | `param_bn128=add_infinities` | `geth` (R²) |
| `test_alt_bn128` | `ECADD` | `target_coef` | `param_bn128=add_negative` | `geth` (R²) |
| `test_alt_bn128` | `ECADD` | `target_coef` | `param_bn128=double` | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_BASE</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_ec_pairing` | `ECPAIRING` | `target_coef` | — | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_ECPAIRING_PER_POINT</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_alt_bn128_benchmark` | `ECPAIRING` | `num_pairs` | — | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_POINT_EVALUATION</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_point_evaluation_uncachable` | `POINT_EVALUATION` | `target_coef` | — | `geth` (R²) |

</details>

<details>
<summary><code>PRECOMPILE_P256VERIFY</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_p256verify` | `P256VERIFY` | `target_coef` | — | `geth` (R²) |

</details>

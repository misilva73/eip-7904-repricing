# Runtime estimation report

Per-spec NNLS fits of `test_runtime_ms` against `opcount`, one row per (target opcode, test, model_by combo, client).

## Contents

- [DIV](#div)
- [SDIV](#sdiv)
- [MOD](#mod)
- [SMOD](#smod)
- [ADDMOD](#addmod)
- [MULMOD](#mulmod)
- [KECCAK256](#keccak256)
- [ECRECOVER](#ecrecover)
- [BLAKE2F](#blake2f)
- [BLS12_G1ADD](#bls12_g1add)
- [BLS12_G2ADD](#bls12_g2add)
- [ECADD](#ecadd)
- [ECPAIRING](#ecpairing)
- [POINT_EVALUATION](#point_evaluation)
- [P256VERIFY](#p256verify)

## DIV

### test_arithmetic

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8405 | 1.421e-05 | 1.00e-03 | [1.386e-05, 1.456e-05] |
| `erigon` | 44 | 0.8776 | 1.009e-05 | 1.00e-03 | [8.893e-06, 1.093e-05] |
| `geth` | 539 | 0.9949 | 5.835e-05 | 1.00e-03 | [5.803e-05, 5.867e-05] |
| `nethermind` | 242 | 0.6228 | 8.105e-06 | 1.00e-03 | [7.143e-06, 9.109e-06] |
| `reth` | 176 | 0.8432 | 7.166e-06 | 1.00e-03 | [6.684e-06, 7.639e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.840
Model:                  NNLS                    Adj. R-squared:          0.840
No. Observations:       1067                              RMSE:          48.88
Df Residuals:           1065                               MAE:          37.85
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    125.4361      4.1378       0.001    117.4160    133.8386
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__besu__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__besu__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.878
Model:                  NNLS                    Adj. R-squared:          0.875
No. Observations:       44                                RMSE:          29.76
Df Residuals:           42                                 MAE:          25.59
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.7903     14.3459       0.069      0.0000     51.8869
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__erigon__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__erigon__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       539                               RMSE:          33.06
Df Residuals:           537                                MAE:          20.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     14.5687      3.8772       0.001      7.1492     22.4393
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__geth__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__geth__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.623
Model:                  NNLS                    Adj. R-squared:          0.621
No. Observations:       242                               RMSE:          49.80
Df Residuals:           240                                MAE:          39.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    120.1294     14.2698       0.001     92.1950    147.0756
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__nethermind__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__nethermind__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.843
Model:                  NNLS                    Adj. R-squared:          0.842
No. Observations:       176                               RMSE:          24.40
Df Residuals:           174                                MAE:          20.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     55.4797      6.8203       0.001     42.3223     68.5901
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__reth__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__reth__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__reth__diagnostics.png)

</details>

## SDIV

### test_arithmetic

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8629 | 1.628e-05 | 1.00e-03 | [1.59e-05, 1.669e-05] |
| `erigon` | 44 | 0.8716 | 1.129e-05 | 1.00e-03 | [1.002e-05, 1.232e-05] |
| `geth` | 539 | 0.9903 | 6.434e-05 | 1.00e-03 | [6.396e-05, 6.475e-05] |
| `nethermind` | 242 | 0.7853 | 1.387e-05 | 1.00e-03 | [1.294e-05, 1.482e-05] |
| `reth` | 176 | 0.8609 | 9.136e-06 | 1.00e-03 | [8.575e-06, 9.722e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.863
Model:                  NNLS                    Adj. R-squared:          0.863
No. Observations:       1067                              RMSE:          51.21
Df Residuals:           1065                               MAE:          43.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    114.5735      5.3489       0.001    103.8198    123.9954
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__besu__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__besu__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.872
Model:                  NNLS                    Adj. R-squared:          0.869
No. Observations:       44                                RMSE:          34.21
Df Residuals:           42                                 MAE:          28.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     25.0914     16.6815       0.072      0.0000     60.3315
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__erigon__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__erigon__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       539                               RMSE:          50.30
Df Residuals:           537                                MAE:          23.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      8.7634      4.6031       0.042      0.0000     18.5132
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__geth__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__geth__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.785
Model:                  NNLS                    Adj. R-squared:          0.784
No. Observations:       242                               RMSE:          57.24
Df Residuals:           240                                MAE:          41.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     62.2123     10.5216       0.001     41.6352     82.9120
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__nethermind__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__nethermind__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.861
Model:                  NNLS                    Adj. R-squared:          0.860
No. Observations:       176                               RMSE:          28.99
Df Residuals:           174                                MAE:          23.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     73.1488      8.1156       0.001     57.0333     88.0767
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__reth__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__reth__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__reth__diagnostics.png)

</details>

## MOD

### test_mod — combo `127`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8863 | 1.78e-05 | 1.00e-03 | [1.738e-05, 1.821e-05] |
| `erigon` | 44 | 0.8743 | 1.211e-05 | 1.00e-03 | [1.052e-05, 1.317e-05] |
| `geth` | 539 | 0.9953 | 7.289e-05 | 1.00e-03 | [7.248e-05, 7.333e-05] |
| `nethermind` | 242 | 0.9131 | 9.792e-06 | 1.00e-03 | [9.408e-06, 1.017e-05] |
| `reth` | 176 | 0.8636 | 7.116e-06 | 1.00e-03 | [6.672e-06, 7.567e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.886
Model:                  NNLS                    Adj. R-squared:          0.886
No. Observations:       1067                              RMSE:          50.28
Df Residuals:           1065                               MAE:          42.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.1999      5.5990       0.001     98.3457    120.6456
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__besu__regression.png)

![](figs/runtime/MOD__test_mod__127__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.874
Model:                  NNLS                    Adj. R-squared:          0.871
No. Observations:       44                                RMSE:          36.22
Df Residuals:           42                                 MAE:          31.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     28.4374     18.9389       0.035      0.0000     71.9993
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__erigon__regression.png)

![](figs/runtime/MOD__test_mod__127__erigon__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       539                               RMSE:          39.66
Df Residuals:           537                                MAE:          29.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     17.0963      4.8482       0.001      7.3759     26.4249
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__geth__regression.png)

![](figs/runtime/MOD__test_mod__127__geth__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.913
Model:                  NNLS                    Adj. R-squared:          0.913
No. Observations:       242                               RMSE:          23.82
Df Residuals:           240                                MAE:          18.57
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     47.3813      4.6982       0.001     38.5191     56.5596
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__nethermind__regression.png)

![](figs/runtime/MOD__test_mod__127__nethermind__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.864
Model:                  NNLS                    Adj. R-squared:          0.863
No. Observations:       176                               RMSE:          22.29
Df Residuals:           174                                MAE:          18.52
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     46.9639      6.4502       0.001     34.9659     59.4412
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__reth__regression.png)

![](figs/runtime/MOD__test_mod__127__reth__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__reth__diagnostics.png)

</details>

### test_mod — combo `191`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8811 | 1.625e-05 | 1.00e-03 | [1.587e-05, 1.659e-05] |
| `erigon` | 44 | 0.8793 | 1.196e-05 | 1.00e-03 | [1.063e-05, 1.291e-05] |
| `geth` | 539 | 0.9953 | 6.963e-05 | 1.00e-03 | [6.919e-05, 7.006e-05] |
| `nethermind` | 242 | 0.8916 | 1.158e-05 | 1.00e-03 | [1.102e-05, 1.207e-05] |
| `reth` | 176 | 0.8565 | 9.559e-06 | 1.00e-03 | [8.952e-06, 1.019e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.881
Model:                  NNLS                    Adj. R-squared:          0.881
No. Observations:       1067                              RMSE:          47.05
Df Residuals:           1065                               MAE:          39.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    114.4569      4.7107       0.001    105.6270    124.0936
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__besu__regression.png)

![](figs/runtime/MOD__test_mod__191__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.879
Model:                  NNLS                    Adj. R-squared:          0.876
No. Observations:       44                                RMSE:          34.94
Df Residuals:           42                                 MAE:          30.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.1106     15.4408       0.101      0.0000     57.0750
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__erigon__regression.png)

![](figs/runtime/MOD__test_mod__191__erigon__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       539                               RMSE:          37.75
Df Residuals:           537                                MAE:          26.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     10.0504      4.7668       0.013      1.0841     19.5201
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__geth__regression.png)

![](figs/runtime/MOD__test_mod__191__geth__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.892
Model:                  NNLS                    Adj. R-squared:          0.891
No. Observations:       242                               RMSE:          31.84
Df Residuals:           240                                MAE:          23.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     46.0036      6.1772       0.001     34.6437     58.6727
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__nethermind__regression.png)

![](figs/runtime/MOD__test_mod__191__nethermind__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.856
Model:                  NNLS                    Adj. R-squared:          0.856
No. Observations:       176                               RMSE:          30.85
Df Residuals:           174                                MAE:          25.76
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.1039      8.7053       0.001     68.3950    102.0626
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__reth__regression.png)

![](figs/runtime/MOD__test_mod__191__reth__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__reth__diagnostics.png)

</details>

### test_mod — combo `255`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8657 | 1.297e-05 | 1.00e-03 | [1.265e-05, 1.328e-05] |
| `erigon` | 44 | 0.8912 | 1.111e-05 | 1.00e-03 | [9.87e-06, 1.206e-05] |
| `geth` | 539 | 0.9941 | 6.332e-05 | 1.00e-03 | [6.292e-05, 6.356e-05] |
| `nethermind` | 242 | 0.9007 | 1.076e-05 | 1.00e-03 | [1.03e-05, 1.121e-05] |
| `reth` | 176 | 0.8616 | 8.056e-06 | 1.00e-03 | [7.575e-06, 8.557e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.866
Model:                  NNLS                    Adj. R-squared:          0.866
No. Observations:       1067                              RMSE:          40.29
Df Residuals:           1065                               MAE:          33.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.7579      4.0845       0.001     83.6845     99.8295
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__besu__regression.png)

![](figs/runtime/MOD__test_mod__255__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.891
Model:                  NNLS                    Adj. R-squared:          0.889
No. Observations:       44                                RMSE:          30.59
Df Residuals:           42                                 MAE:          26.20
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     24.7279     15.2728       0.048      0.0000     59.5607
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__erigon__regression.png)

![](figs/runtime/MOD__test_mod__255__erigon__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.994
No. Observations:       539                               RMSE:          38.54
Df Residuals:           537                                MAE:          27.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      2.8387      3.3948       0.258      0.0000     10.8961
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__geth__regression.png)

![](figs/runtime/MOD__test_mod__255__geth__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.901
Model:                  NNLS                    Adj. R-squared:          0.900
No. Observations:       242                               RMSE:          28.15
Df Residuals:           240                                MAE:          22.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     45.2051      5.4480       0.001     34.3939     55.0747
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__nethermind__regression.png)

![](figs/runtime/MOD__test_mod__255__nethermind__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.862
Model:                  NNLS                    Adj. R-squared:          0.861
No. Observations:       176                               RMSE:          25.46
Df Residuals:           174                                MAE:          21.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     77.5750      6.9109       0.001     64.3702     90.7380
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__reth__regression.png)

![](figs/runtime/MOD__test_mod__255__reth__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__reth__diagnostics.png)

</details>

### test_mod — combo `63`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8606 | 1.309e-05 | 1.00e-03 | [1.277e-05, 1.34e-05] |
| `erigon` | 44 | 0.884 | 8.575e-06 | 1.00e-03 | [7.579e-06, 9.276e-06] |
| `geth` | 539 | 0.9947 | 5.155e-05 | 1.00e-03 | [5.126e-05, 5.178e-05] |
| `nethermind` | 242 | 0.8466 | 7.085e-06 | 1.00e-03 | [6.707e-06, 7.433e-06] |
| `reth` | 176 | 0.8447 | 6.196e-06 | 1.00e-03 | [5.792e-06, 6.615e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.861
Model:                  NNLS                    Adj. R-squared:          0.861
No. Observations:       1067                              RMSE:          41.53
Df Residuals:           1065                               MAE:          34.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     80.9897      4.2325       0.001     72.6705     89.4556
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__besu__regression.png)

![](figs/runtime/MOD__test_mod__63__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.884
Model:                  NNLS                    Adj. R-squared:          0.881
No. Observations:       44                                RMSE:          24.49
Df Residuals:           42                                 MAE:          20.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     18.1931     12.1521       0.044      0.0000     46.2689
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__erigon__regression.png)

![](figs/runtime/MOD__test_mod__63__erigon__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       539                               RMSE:          29.59
Df Residuals:           537                                MAE:          19.17
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      3.2403      2.8625       0.192      0.0000      9.3464
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__geth__regression.png)

![](figs/runtime/MOD__test_mod__63__geth__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.847
Model:                  NNLS                    Adj. R-squared:          0.846
No. Observations:       242                               RMSE:          23.78
Df Residuals:           240                                MAE:          16.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     33.0721      4.4703       0.001     25.1067     42.2573
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__nethermind__regression.png)

![](figs/runtime/MOD__test_mod__63__nethermind__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.845
Model:                  NNLS                    Adj. R-squared:          0.844
No. Observations:       176                               RMSE:          20.95
Df Residuals:           174                                MAE:          17.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     53.1469      5.8948       0.001     41.7655     63.8233
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__reth__regression.png)

![](figs/runtime/MOD__test_mod__63__reth__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__reth__diagnostics.png)

</details>

## SMOD

### test_mod — combo `127`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8738 | 1.801e-05 | 1.00e-03 | [1.757e-05, 1.843e-05] |
| `erigon` | 44 | 0.8183 | 1.284e-05 | 1.00e-03 | [1.122e-05, 1.41e-05] |
| `geth` | 539 | 0.9953 | 7.573e-05 | 1.00e-03 | [7.532e-05, 7.617e-05] |
| `nethermind` | 242 | 0.8849 | 1.117e-05 | 1.00e-03 | [1.059e-05, 1.173e-05] |
| `reth` | 176 | 0.8561 | 6.896e-06 | 1.00e-03 | [6.456e-06, 7.336e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.874
Model:                  NNLS                    Adj. R-squared:          0.874
No. Observations:       1067                              RMSE:          53.98
Df Residuals:           1065                               MAE:          45.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    124.7526      5.6646       0.001    113.7042    136.7730
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__besu__regression.png)

![](figs/runtime/SMOD__test_mod__127__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.818
Model:                  NNLS                    Adj. R-squared:          0.814
No. Observations:       44                                RMSE:          47.70
Df Residuals:           42                                 MAE:          35.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     29.6536     19.1408       0.055      0.0000     73.2373
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__erigon__regression.png)

![](figs/runtime/SMOD__test_mod__127__erigon__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       539                               RMSE:          40.86
Df Residuals:           537                                MAE:          29.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.4333      4.6673       0.001     11.5452     29.1952
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__geth__regression.png)

![](figs/runtime/SMOD__test_mod__127__geth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.885
Model:                  NNLS                    Adj. R-squared:          0.884
No. Observations:       242                               RMSE:          31.76
Df Residuals:           240                                MAE:          22.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.1180      7.3608       0.001     37.1873     65.6706
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__nethermind__regression.png)

![](figs/runtime/SMOD__test_mod__127__nethermind__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.856
Model:                  NNLS                    Adj. R-squared:          0.855
No. Observations:       176                               RMSE:          22.29
Df Residuals:           174                                MAE:          18.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     58.7463      5.9442       0.001     47.4491     70.1803
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__reth__regression.png)

![](figs/runtime/SMOD__test_mod__127__reth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__reth__diagnostics.png)

</details>

### test_mod — combo `191`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8648 | 1.679e-05 | 1.00e-03 | [1.638e-05, 1.72e-05] |
| `erigon` | 44 | 0.8663 | 1.235e-05 | 1.00e-03 | [1.096e-05, 1.346e-05] |
| `geth` | 539 | 0.9964 | 7.233e-05 | 1.00e-03 | [7.196e-05, 7.273e-05] |
| `nethermind` | 242 | 0.8788 | 1.276e-05 | 1.00e-03 | [1.217e-05, 1.336e-05] |
| `reth` | 176 | 0.8528 | 9.827e-06 | 1.00e-03 | [9.189e-06, 1.047e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.865
Model:                  NNLS                    Adj. R-squared:          0.865
No. Observations:       1067                              RMSE:          52.32
Df Residuals:           1065                               MAE:          43.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.7342      5.3398       0.001     99.3939    120.7712
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__besu__regression.png)

![](figs/runtime/SMOD__test_mod__191__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.866
Model:                  NNLS                    Adj. R-squared:          0.863
No. Observations:       44                                RMSE:          38.25
Df Residuals:           42                                 MAE:          32.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     29.0003     17.9779       0.038      0.0000     70.0213
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__erigon__regression.png)

![](figs/runtime/SMOD__test_mod__191__erigon__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       539                               RMSE:          34.28
Df Residuals:           537                                MAE:          26.12
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     15.9738      4.3880       0.001      7.4149     24.4322
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__geth__regression.png)

![](figs/runtime/SMOD__test_mod__191__geth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.879
Model:                  NNLS                    Adj. R-squared:          0.878
No. Observations:       242                               RMSE:          37.36
Df Residuals:           240                                MAE:          29.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     53.8783      7.0984       0.001     39.5812     68.1132
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__nethermind__regression.png)

![](figs/runtime/SMOD__test_mod__191__nethermind__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.853
Model:                  NNLS                    Adj. R-squared:          0.852
No. Observations:       176                               RMSE:          32.20
Df Residuals:           174                                MAE:          26.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     89.7391      8.5882       0.001     72.6100    106.8115
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__reth__regression.png)

![](figs/runtime/SMOD__test_mod__191__reth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__reth__diagnostics.png)

</details>

### test_mod — combo `255`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8402 | 1.38e-05 | 1.00e-03 | [1.341e-05, 1.417e-05] |
| `erigon` | 44 | 0.878 | 1.143e-05 | 1.00e-03 | [1.019e-05, 1.25e-05] |
| `geth` | 539 | 0.9967 | 6.5e-05 | 1.00e-03 | [6.47e-05, 6.535e-05] |
| `nethermind` | 242 | 0.8935 | 1.117e-05 | 1.00e-03 | [1.068e-05, 1.165e-05] |
| `reth` | 176 | 0.8486 | 8.144e-06 | 1.00e-03 | [7.597e-06, 8.705e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.840
Model:                  NNLS                    Adj. R-squared:          0.840
No. Observations:       1067                              RMSE:          47.44
Df Residuals:           1065                               MAE:          38.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.1635      4.9158       0.001     77.6691     96.8752
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__besu__regression.png)

![](figs/runtime/SMOD__test_mod__255__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.878
Model:                  NNLS                    Adj. R-squared:          0.875
No. Observations:       44                                RMSE:          33.59
Df Residuals:           42                                 MAE:          28.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     25.9510     15.9474       0.052      0.0000     59.5767
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__erigon__regression.png)

![](figs/runtime/SMOD__test_mod__255__erigon__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       539                               RMSE:          29.62
Df Residuals:           537                                MAE:          22.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      7.6463      3.6152       0.030      0.0000     14.2565
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__geth__regression.png)

![](figs/runtime/SMOD__test_mod__255__geth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.894
Model:                  NNLS                    Adj. R-squared:          0.893
No. Observations:       242                               RMSE:          30.40
Df Residuals:           240                                MAE:          22.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     53.9883      5.9540       0.001     42.6419     66.3272
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__nethermind__regression.png)

![](figs/runtime/SMOD__test_mod__255__nethermind__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.849
Model:                  NNLS                    Adj. R-squared:          0.848
No. Observations:       176                               RMSE:          27.12
Df Residuals:           174                                MAE:          22.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.6060      7.6758       0.001     70.8309    101.5058
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__reth__regression.png)

![](figs/runtime/SMOD__test_mod__255__reth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__reth__diagnostics.png)

</details>

### test_mod — combo `63`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8439 | 1.368e-05 | 1.00e-03 | [1.329e-05, 1.403e-05] |
| `erigon` | 44 | 0.4382 | 7.591e-06 | 1.00e-03 | [4.391e-06, 9.388e-06] |
| `geth` | 539 | 0.9944 | 5.499e-05 | 1.00e-03 | [5.465e-05, 5.516e-05] |
| `nethermind` | 242 | 0.8893 | 8.258e-06 | 1.00e-03 | [7.884e-06, 8.669e-06] |
| `reth` | 176 | 0.8548 | 6.518e-06 | 1.00e-03 | [6.085e-06, 6.949e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.844
No. Observations:       1067                              RMSE:          46.37
Df Residuals:           1065                               MAE:          37.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.0891      5.1330       0.001     77.0472     97.5292
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__besu__regression.png)

![](figs/runtime/SMOD__test_mod__63__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.438
Model:                  NNLS                    Adj. R-squared:          0.425
No. Observations:       44                                RMSE:          67.77
Df Residuals:           42                                 MAE:          34.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     58.7820     42.7039       0.008      3.4764    160.8349
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__erigon__regression.png)

![](figs/runtime/SMOD__test_mod__63__erigon__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.994
No. Observations:       539                               RMSE:          32.48
Df Residuals:           537                                MAE:          18.49
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      2.2352      3.2862       0.300      0.0000     10.7590
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__geth__regression.png)

![](figs/runtime/SMOD__test_mod__63__geth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.889
Model:                  NNLS                    Adj. R-squared:          0.889
No. Observations:       242                               RMSE:          22.97
Df Residuals:           240                                MAE:          16.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     37.1818      4.5001       0.001     28.5958     45.8341
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__nethermind__regression.png)

![](figs/runtime/SMOD__test_mod__63__nethermind__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.855
Model:                  NNLS                    Adj. R-squared:          0.854
No. Observations:       176                               RMSE:          21.18
Df Residuals:           174                                MAE:          17.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.1483      5.9284       0.001     36.6357     59.1228
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__reth__regression.png)

![](figs/runtime/SMOD__test_mod__63__reth__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__reth__diagnostics.png)

</details>

## ADDMOD

### test_mod_arithmetic — combo `191`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8621 | 2.112e-05 | 1.00e-03 | [2.066e-05, 2.159e-05] |
| `erigon` | 44 | 0.8762 | 1.768e-05 | 1.00e-03 | [1.555e-05, 1.938e-05] |
| `geth` | 539 | 0.9932 | 0.0001032 | 1.00e-03 | [0.0001024, 0.0001036] |
| `nethermind` | 242 | 0.799 | 1.361e-05 | 1.00e-03 | [1.29e-05, 1.446e-05] |
| `reth` | 176 | 0.8461 | 9.294e-06 | 1.00e-03 | [8.699e-06, 9.908e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.862
Model:                  NNLS                    Adj. R-squared:          0.862
No. Observations:       1067                              RMSE:          38.03
Df Residuals:           1065                               MAE:          31.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.2423      3.4896       0.001     84.9828     99.0091
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.876
Model:                  NNLS                    Adj. R-squared:          0.873
No. Observations:       44                                RMSE:          29.92
Df Residuals:           42                                 MAE:          25.49
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     27.5625     15.0995       0.026      0.0000     61.3975
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__erigon__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__erigon__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       539                               RMSE:          38.32
Df Residuals:           537                                MAE:          23.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      1.9685      3.2862       0.321      0.0000     10.8767
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__geth__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__geth__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.799
Model:                  NNLS                    Adj. R-squared:          0.798
No. Observations:       242                               RMSE:          30.73
Df Residuals:           240                                MAE:          15.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     33.1711      5.6453       0.001     22.0092     44.0444
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__nethermind__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__nethermind__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.846
Model:                  NNLS                    Adj. R-squared:          0.845
No. Observations:       176                               RMSE:          17.85
Df Residuals:           174                                MAE:          14.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     42.3008      4.7480       0.001     32.6743     51.3150
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__reth__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__reth__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__reth__diagnostics.png)

</details>

## MULMOD

### test_mod_arithmetic — combo `191`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8595 | 3.254e-05 | 1.00e-03 | [3.178e-05, 3.329e-05] |
| `erigon` | 44 | 0.8586 | 2.859e-05 | 1.00e-03 | [2.477e-05, 3.004e-05] |
| `geth` | 539 | 0.9963 | 0.0001507 | 1.00e-03 | [0.0001499, 0.000151] |
| `nethermind` | 242 | 0.902 | 3.38e-05 | 1.00e-03 | [3.239e-05, 3.521e-05] |
| `reth` | 176 | 0.8518 | 1.686e-05 | 1.00e-03 | [1.587e-05, 1.795e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.859
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       1067                              RMSE:          59.23
Df Residuals:           1065                               MAE:          50.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    132.3330      5.8009       0.001    121.3863    143.5928
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.859
Model:                  NNLS                    Adj. R-squared:          0.855
No. Observations:       44                                RMSE:          52.23
Df Residuals:           42                                 MAE:          40.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      4.3637     16.5460       0.423      0.0000     55.7677
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__erigon__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__erigon__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       539                               RMSE:          41.16
Df Residuals:           537                                MAE:          30.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.7769      2.9455       0.465      0.0000     10.4077
       opcount      0.0002      0.0000       0.001      0.0001      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__geth__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__geth__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.902
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       242                               RMSE:          50.15
Df Residuals:           240                                MAE:          38.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     82.6517      9.9531       0.001     64.2140    102.0847
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__nethermind__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__nethermind__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.852
Model:                  NNLS                    Adj. R-squared:          0.851
No. Observations:       176                               RMSE:          31.66
Df Residuals:           174                                MAE:          25.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.4623      8.2709       0.001     72.9210    105.0477
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__reth__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__reth__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__reth__diagnostics.png)

</details>

## KECCAK256

### test_keccak_diff_mem_msg_sizes — combo `0`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.7734 | 0.0001028 | 1.00e-03 | [0.000101, 0.0001046] |
| `erigon` | 176 | 0.8078 | 7.447e-05 | 1.00e-03 | [6.829e-05, 7.963e-05] |
| `geth` | 2156 | 0.9353 | 0.0004654 | 1.00e-03 | [0.0004603, 0.0004686] |
| `nethermind` | 924 | 0.6996 | 2.419e-05 | 1.00e-03 | [1.637e-05, 3.164e-05] |
| `reth` | 704 | 0.5559 | 1.578e-05 | 1.00e-03 | [1.021e-05, 2.18e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.773
Model:                  NNLS                    Adj. R-squared:          0.773
No. Observations:       4268                              RMSE:          88.40
Df Residuals:           4265                               MAE:          72.61
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    118.9894      4.3553       0.001    110.9819    128.1559
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__besu__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__besu__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.808
Model:                  NNLS                    Adj. R-squared:          0.806
No. Observations:       176                               RMSE:          61.96
Df Residuals:           173                                MAE:          50.95
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     37.7400     13.8655       0.002     13.4349     65.9355
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__erigon__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__erigon__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       2156                              RMSE:         188.36
Df Residuals:           2153                               MAE:         167.75
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      9.6394      9.4086       0.194      0.0000     31.2832
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
     msg_words      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__geth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__geth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.700
Model:                  NNLS                    Adj. R-squared:          0.699
No. Observations:       924                               RMSE:         158.93
Df Residuals:           921                                MAE:         129.54
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.8263     15.1220       0.001     61.6465    120.1660
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__nethermind__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__nethermind__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.556
Model:                  NNLS                    Adj. R-squared:          0.555
No. Observations:       704                               RMSE:         106.86
Df Residuals:           701                                MAE:          86.35
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     60.5514     11.1303       0.001     38.1823     81.2270
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__reth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__reth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__0__reth__diagnostics.png)

</details>

### test_keccak_diff_mem_msg_sizes — combo `1024`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.7791 | 0.0001085 | 1.00e-03 | [0.0001068, 0.0001103] |
| `erigon` | 176 | 0.8146 | 7.433e-05 | 1.00e-03 | [6.831e-05, 8.002e-05] |
| `geth` | 2156 | 0.9328 | 0.0004664 | 1.00e-03 | [0.0004613, 0.0004699] |
| `nethermind` | 924 | 0.7016 | 2.488e-05 | 1.00e-03 | [1.768e-05, 3.261e-05] |
| `reth` | 704 | 0.5581 | 1.603e-05 | 1.00e-03 | [1.018e-05, 2.196e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.779
Model:                  NNLS                    Adj. R-squared:          0.779
No. Observations:       4268                              RMSE:          89.22
Df Residuals:           4265                               MAE:          72.56
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    125.6008      4.5317       0.001    116.0993    133.8891
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__besu__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__besu__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.815
Model:                  NNLS                    Adj. R-squared:          0.812
No. Observations:       176                               RMSE:          60.69
Df Residuals:           173                                MAE:          49.65
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.5125     14.3769       0.005     11.1649     67.4203
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__erigon__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__erigon__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.933
Model:                  NNLS                    Adj. R-squared:          0.933
No. Observations:       2156                              RMSE:         192.52
Df Residuals:           2153                               MAE:         167.16
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      8.7874      9.4118       0.244      0.0000     30.7227
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
     msg_words      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__geth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__geth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.702
Model:                  NNLS                    Adj. R-squared:          0.701
No. Observations:       924                               RMSE:         158.74
Df Residuals:           921                                MAE:         129.49
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.6075     15.3593       0.001     56.3268    116.5245
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__nethermind__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__nethermind__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.558
Model:                  NNLS                    Adj. R-squared:          0.557
No. Observations:       704                               RMSE:         106.33
Df Residuals:           701                                MAE:          85.98
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     59.3755     11.4467       0.001     36.0494     79.8772
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__reth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__reth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__1024__reth__diagnostics.png)

</details>

### test_keccak_diff_mem_msg_sizes — combo `256`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.7758 | 0.0001107 | 1.00e-03 | [0.0001088, 0.0001126] |
| `erigon` | 176 | 0.7956 | 7.485e-05 | 1.00e-03 | [6.864e-05, 8.042e-05] |
| `geth` | 2156 | 0.9353 | 0.0004657 | 1.00e-03 | [0.0004603, 0.0004689] |
| `nethermind` | 924 | 0.7018 | 2.471e-05 | 1.00e-03 | [1.714e-05, 3.252e-05] |
| `reth` | 704 | 0.5583 | 1.558e-05 | 1.00e-03 | [1.012e-05, 2.167e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.776
Model:                  NNLS                    Adj. R-squared:          0.776
No. Observations:       4268                              RMSE:          91.48
Df Residuals:           4265                               MAE:          74.40
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    121.6530      4.5558       0.001    112.9593    130.9402
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__besu__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__besu__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.796
Model:                  NNLS                    Adj. R-squared:          0.793
No. Observations:       176                               RMSE:          64.75
Df Residuals:           173                                MAE:          51.74
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     37.0427     14.7407       0.004      9.6734     67.7061
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__erigon__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__erigon__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       2156                              RMSE:         188.45
Df Residuals:           2153                               MAE:         167.50
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      8.9563      9.5965       0.200      0.0000     31.9312
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
     msg_words      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__geth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__geth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.702
Model:                  NNLS                    Adj. R-squared:          0.701
No. Observations:       924                               RMSE:         158.59
Df Residuals:           921                                MAE:         129.00
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.6138     14.9302       0.001     56.7212    116.5239
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__nethermind__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__nethermind__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.558
Model:                  NNLS                    Adj. R-squared:          0.557
No. Observations:       704                               RMSE:         106.55
Df Residuals:           701                                MAE:          85.81
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     61.8342     11.5437       0.001     39.1548     84.9327
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__reth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__reth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__256__reth__diagnostics.png)

</details>

### test_keccak_diff_mem_msg_sizes — combo `32`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.7521 | 0.0001014 | 1.00e-03 | [9.953e-05, 0.0001032] |
| `erigon` | 176 | 0.81 | 7.512e-05 | 1.00e-03 | [6.849e-05, 8.08e-05] |
| `geth` | 2156 | 0.9352 | 0.0004661 | 1.00e-03 | [0.0004607, 0.000469] |
| `nethermind` | 924 | 0.7007 | 2.439e-05 | 1.00e-03 | [1.637e-05, 3.249e-05] |
| `reth` | 704 | 0.5565 | 1.546e-05 | 1.00e-03 | [9.81e-06, 2.174e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.752
Model:                  NNLS                    Adj. R-squared:          0.752
No. Observations:       4268                              RMSE:          90.87
Df Residuals:           4265                               MAE:          74.86
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    148.5137      4.3183       0.001    139.9523    157.1251
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__besu__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__besu__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.810
Model:                  NNLS                    Adj. R-squared:          0.808
No. Observations:       176                               RMSE:          62.65
Df Residuals:           173                                MAE:          51.36
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     33.8933     15.1127       0.009      6.1785     65.5337
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__erigon__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__erigon__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       2156                              RMSE:         188.95
Df Residuals:           2153                               MAE:         166.90
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      5.8751      8.5958       0.294      0.0000     29.8335
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
     msg_words      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__geth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__geth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.701
Model:                  NNLS                    Adj. R-squared:          0.700
No. Observations:       924                               RMSE:         158.70
Df Residuals:           921                                MAE:         129.43
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     89.6165     15.2487       0.001     58.0081    119.4082
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__nethermind__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__nethermind__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.556
Model:                  NNLS                    Adj. R-squared:          0.555
No. Observations:       704                               RMSE:         106.42
Df Residuals:           701                                MAE:          85.72
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     62.8356     11.5272       0.001     39.2938     84.1109
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__reth__regression.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__reth__bootstrap.png)

![](figs/runtime/KECCAK256__test_keccak_diff_mem_msg_sizes__32__reth__diagnostics.png)

</details>

## ECRECOVER

### test_ecrecover

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8765 | 0.0075 | 1.00e-03 | [0.007318, 0.007656] |
| `erigon` | 44 | 0.9031 | 0.008677 | 1.00e-03 | [0.007769, 0.009439] |
| `geth` | 539 | 0.9978 | 0.04266 | 1.00e-03 | [0.04249, 0.04281] |
| `nethermind` | 231 | 0.8844 | 0.006924 | 1.00e-03 | [0.006551, 0.007279] |
| `reth` | 176 | 0.8432 | 0.006548 | 1.00e-03 | [0.006105, 0.007006] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.877
Model:                  NNLS                    Adj. R-squared:          0.876
No. Observations:       1067                              RMSE:          56.79
Df Residuals:           1065                               MAE:          48.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    139.7016      5.9963       0.001    128.7725    151.9784
       opcount      0.0075      0.0001       0.001      0.0073      0.0077
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.903
Model:                  NNLS                    Adj. R-squared:          0.901
No. Observations:       44                                RMSE:          57.34
Df Residuals:           42                                 MAE:          48.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     50.4955     27.7048       0.029      0.0000    111.1614
       opcount      0.0087      0.0004       0.001      0.0078      0.0094
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__erigon__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__erigon__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          39.96
Df Residuals:           537                                MAE:          32.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      6.5496      4.6466       0.093      0.0000     16.1182
       opcount      0.0427      0.0001       0.001      0.0425      0.0428
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__geth__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__geth__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.884
Model:                  NNLS                    Adj. R-squared:          0.884
No. Observations:       231                               RMSE:          50.50
Df Residuals:           229                                MAE:          41.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    106.2000     12.3866       0.001     82.2979    130.9545
       opcount      0.0069      0.0002       0.001      0.0066      0.0073
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__nethermind__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__nethermind__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.843
Model:                  NNLS                    Adj. R-squared:          0.842
No. Observations:       176                               RMSE:          56.97
Df Residuals:           174                                MAE:          48.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.1690     16.5544       0.001     94.2149    158.4891
       opcount      0.0065      0.0002       0.001      0.0061      0.0070
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__reth__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__reth__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__reth__diagnostics.png)

</details>

## BLAKE2F

### test_blake2f_benchmark

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.9737 | 0.001231 | 1.00e-03 | [0.001225, 0.001238] |
| `erigon` | 176 | 0.8339 | 0.0004753 | 1.00e-03 | [0.0004451, 0.0005037] |
| `geth` | 2156 | 0.9941 | 0.000435 | 1.00e-03 | [0.0004332, 0.000437] |
| `nethermind` | 968 | 0.8862 | 0.0001796 | 1.00e-03 | [0.0001746, 0.0001869] |
| `reth` | 704 | 0.988 | 0.0003808 | 1.00e-03 | [0.0003779, 0.0003834] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.974
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       4268                              RMSE:         101.98
Df Residuals:           4265                               MAE:          86.32
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    168.5539      5.2334       0.001    157.9759    179.0634
       opcount      0.0012      0.0000       0.001      0.0012      0.0012
    num_rounds      0.0000      0.0000       1.000      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.834
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       176                               RMSE:         107.32
Df Residuals:           173                                MAE:          82.76
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     43.1406     19.4790       0.020      2.9534     82.6914
       opcount      0.0005      0.0000       0.001      0.0004      0.0005
    num_rounds      0.0000      0.0000       0.261      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__erigon__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__erigon__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.994
No. Observations:       2156                              RMSE:          21.87
Df Residuals:           2153                               MAE:          14.50
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     11.7764      1.2494       0.001      9.2338     13.9879
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__geth__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__geth__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.886
Model:                  NNLS                    Adj. R-squared:          0.886
No. Observations:       968                               RMSE:          34.42
Df Residuals:           965                                MAE:          17.44
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     35.5320      4.0133       0.001     26.6305     41.9169
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__nethermind__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__nethermind__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       704                               RMSE:          21.16
Df Residuals:           701                                MAE:          17.09
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     12.5655      2.2944       0.001      8.0351     17.0673
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
    num_rounds      0.0000      0.0000       1.000      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__reth__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__reth__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__reth__diagnostics.png)

</details>

### test_blake2f_uncachable

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 4268 | 0.8493 | 0.0003771 | 1.00e-03 | [0.0003715, 0.0003825] |
| `erigon` | 176 | 0.9199 | 0.0009368 | 1.00e-03 | [0.0008859, 0.0009525] |
| `geth` | 2156 | 0.9949 | 0.0005606 | 1.00e-03 | [0.0005585, 0.0005627] |
| `nethermind` | 968 | 0.949 | 0.0001882 | 1.00e-03 | [0.0001852, 0.0001913] |
| `reth` | 704 | 0.9871 | 0.0003739 | 1.00e-03 | [0.0003709, 0.0003767] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.849
Model:                  NNLS                    Adj. R-squared:          0.849
No. Observations:       4268                              RMSE:          68.77
Df Residuals:           4265                               MAE:          57.96
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    133.5310      3.7846       0.001    126.2383    140.7114
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__besu__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__besu__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.920
Model:                  NNLS                    Adj. R-squared:          0.919
No. Observations:       176                               RMSE:         114.22
Df Residuals:           173                                MAE:          90.00
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      1.4754     15.1679       0.486      0.0000     49.4851
       opcount      0.0009      0.0000       0.001      0.0009      0.0010
    num_rounds      0.0000      0.0000       1.000      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__erigon__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__erigon__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       2156                              RMSE:          20.23
Df Residuals:           2153                               MAE:          15.45
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     14.4142      1.2877       0.001     12.0146     17.1320
       opcount      0.0006      0.0000       0.001      0.0006      0.0006
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__geth__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__geth__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.949
Model:                  NNLS                    Adj. R-squared:          0.949
No. Observations:       968                               RMSE:          19.31
Df Residuals:           965                                MAE:          15.27
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     34.6266      1.8253       0.001     31.3665     38.5034
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__nethermind__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__nethermind__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.987
Model:                  NNLS                    Adj. R-squared:          0.987
No. Observations:       704                               RMSE:          17.68
Df Residuals:           701                                MAE:          14.31
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.9384      2.1232       0.001     12.5873     21.0338
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
    num_rounds      0.0000      0.0000       1.000      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__reth__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__reth__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_uncachable__all__reth__diagnostics.png)

</details>

## BLS12_G1ADD

### test_bls12_381

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9497 | 0.002328 | 1.00e-03 | [0.002296, 0.002361] |
| `erigon` | 44 | 0.4836 | 0.0008364 | 1.00e-03 | [0.0005194, 0.001063] |
| `geth` | 539 | 0.9976 | 0.004035 | 1.00e-03 | [0.004018, 0.004053] |
| `nethermind` | 242 | 0.9235 | 0.0009944 | 1.00e-03 | [0.0009582, 0.001032] |
| `reth` | 176 | 0.8812 | 0.000754 | 1.00e-03 | [0.0007174, 0.0007969] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.950
Model:                  NNLS                    Adj. R-squared:          0.950
No. Observations:       1067                              RMSE:          68.67
Df Residuals:           1065                               MAE:          57.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.0503      7.2036       0.001     76.3646    105.3860
       opcount      0.0023      0.0000       0.001      0.0023      0.0024
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.484
Model:                  NNLS                    Adj. R-squared:          0.471
No. Observations:       44                                RMSE:         110.72
Df Residuals:           42                                 MAE:          67.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    112.5904     69.9850       0.041      0.0000    268.0930
       opcount      0.0008      0.0001       0.001      0.0005      0.0011
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__erigon__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__erigon__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          25.36
Df Residuals:           537                                MAE:          21.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     12.6505      3.2558       0.001      5.8549     19.0328
       opcount      0.0040      0.0000       0.001      0.0040      0.0041
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__geth__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__geth__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.924
Model:                  NNLS                    Adj. R-squared:          0.923
No. Observations:       242                               RMSE:          36.65
Df Residuals:           240                                MAE:          27.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.8485      8.1054       0.001     69.9280    101.8214
       opcount      0.0010      0.0000       0.001      0.0010      0.0010
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__nethermind__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__nethermind__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.881
Model:                  NNLS                    Adj. R-squared:          0.881
No. Observations:       176                               RMSE:          35.46
Df Residuals:           174                                MAE:          28.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     97.2164      9.3147       0.001     78.5039    114.1654
       opcount      0.0008      0.0000       0.001      0.0007      0.0008
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__reth__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__reth__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__reth__diagnostics.png)

</details>

## BLS12_G2ADD

### test_bls12_381

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9316 | 0.002632 | 1.00e-03 | [0.002592, 0.002673] |
| `erigon` | 44 | 0.5295 | 0.001104 | 1.00e-03 | [0.0007407, 0.00133] |
| `geth` | 539 | 0.9983 | 0.00556 | 1.00e-03 | [0.00554, 0.005581] |
| `nethermind` | 242 | 0.9379 | 0.001527 | 1.00e-03 | [0.001478, 0.001574] |
| `reth` | 176 | 0.8537 | 0.001027 | 1.00e-03 | [0.0009624, 0.001086] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.932
Model:                  NNLS                    Adj. R-squared:          0.932
No. Observations:       1067                              RMSE:          62.74
Df Residuals:           1065                               MAE:          51.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    107.2409      6.4413       0.001     94.8171    119.4322
       opcount      0.0026      0.0000       0.001      0.0026      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.530
Model:                  NNLS                    Adj. R-squared:          0.518
No. Observations:       44                                RMSE:          91.54
Df Residuals:           42                                 MAE:          45.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     81.0363     56.7071       0.022      1.7637    207.8710
       opcount      0.0011      0.0002       0.001      0.0007      0.0013
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__erigon__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__erigon__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          20.38
Df Residuals:           537                                MAE:          16.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      7.2548      2.5399       0.006      2.2017     12.1265
       opcount      0.0056      0.0000       0.001      0.0055      0.0056
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__geth__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__geth__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       242                               RMSE:          34.57
Df Residuals:           240                                MAE:          28.23
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     81.7228      6.6375       0.001     69.2527     94.3709
       opcount      0.0015      0.0000       0.001      0.0015      0.0016
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__nethermind__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__nethermind__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.854
Model:                  NNLS                    Adj. R-squared:          0.853
No. Observations:       176                               RMSE:          37.39
Df Residuals:           174                                MAE:          31.07
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.0801     10.2816       0.001     78.7045    116.0400
       opcount      0.0010      0.0000       0.001      0.0010      0.0011
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__reth__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__reth__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__reth__diagnostics.png)

</details>

## ECADD

### test_alt_bn128 — combo `add`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.941 | 0.001247 | 1.00e-03 | [0.001226, 0.001265] |
| `erigon` | 44 | 0.8799 | 0.0006605 | 1.00e-03 | [0.0005855, 0.0007157] |
| `geth` | 539 | 0.9975 | 0.002282 | 1.00e-03 | [0.002273, 0.002291] |
| `nethermind` | 242 | 0.8288 | 0.0004869 | 1.00e-03 | [0.0004529, 0.0005204] |
| `reth` | 176 | 0.8634 | 0.000592 | 1.00e-03 | [0.0005526, 0.0006297] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.941
Model:                  NNLS                    Adj. R-squared:          0.941
No. Observations:       1067                              RMSE:          73.59
Df Residuals:           1065                               MAE:          62.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    153.7495      8.0972       0.001    138.2629    170.4783
       opcount      0.0012      0.0000       0.001      0.0012      0.0013
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.880
Model:                  NNLS                    Adj. R-squared:          0.877
No. Observations:       44                                RMSE:          57.50
Df Residuals:           42                                 MAE:          47.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     36.7820     26.0373       0.079      0.0000     96.9272
       opcount      0.0007      0.0000       0.001      0.0006      0.0007
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__erigon__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__erigon__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          26.67
Df Residuals:           537                                MAE:          20.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.9496      3.2263       0.001     10.2887     23.2006
       opcount      0.0023      0.0000       0.001      0.0023      0.0023
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__geth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__geth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.829
Model:                  NNLS                    Adj. R-squared:          0.828
No. Observations:       242                               RMSE:          52.15
Df Residuals:           240                                MAE:          31.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     74.6770     12.9756       0.001     50.8348    101.3689
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__nethermind__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__nethermind__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.863
Model:                  NNLS                    Adj. R-squared:          0.863
No. Observations:       176                               RMSE:          55.49
Df Residuals:           174                                MAE:          47.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.4207     16.0201       0.001     97.5586    159.5877
       opcount      0.0006      0.0000       0.001      0.0006      0.0006
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__reth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__reth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__reth__diagnostics.png)

</details>

### test_alt_bn128 — combo `add_infinities`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9734 | 0.0012 | 1.00e-03 | [0.001188, 0.00121] |
| `erigon` | 44 | 0.9046 | 0.0004992 | 1.00e-03 | [0.0004461, 0.0005139] |
| `geth` | 539 | 0.9904 | 0.0004758 | 1.00e-03 | [0.0004716, 0.00048] |
| `nethermind` | 242 | 0.6489 | 0.0002591 | 1.00e-03 | [0.0002337, 0.0002713] |
| `reth` | 176 | 0.99 | 0.0003796 | 1.00e-03 | [0.0003745, 0.0003848] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.973
No. Observations:       1067                              RMSE:          46.77
Df Residuals:           1065                               MAE:          39.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     82.1963      4.9013       0.001     73.1709     91.6398
       opcount      0.0012      0.0000       0.001      0.0012      0.0012
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.905
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       44                                RMSE:          38.20
Df Residuals:           42                                 MAE:          32.37
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      1.2583     10.6089       0.473      0.0000     36.1347
       opcount      0.0005      0.0000       0.001      0.0004      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__erigon__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__erigon__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       539                               RMSE:          11.05
Df Residuals:           537                                MAE:           8.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      3.8053      1.5540       0.006      0.8057      7.0498
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__geth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__geth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.649
Model:                  NNLS                    Adj. R-squared:          0.647
No. Observations:       242                               RMSE:          44.91
Df Residuals:           240                                MAE:          16.76
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      2.8547      5.5391       0.338      0.0000     17.5264
       opcount      0.0003      0.0000       0.001      0.0002      0.0003
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__nethermind__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__nethermind__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       176                               RMSE:           9.01
Df Residuals:           174                                MAE:           6.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      6.1770      2.1381       0.001      2.0067     10.4761
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__reth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__reth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__reth__diagnostics.png)

</details>

### test_alt_bn128 — combo `add_negative`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9706 | 0.001199 | 1.00e-03 | [0.001186, 0.001211] |
| `erigon` | 44 | 0.8922 | 0.000489 | 1.00e-03 | [0.000432, 0.0005263] |
| `geth` | 539 | 0.9945 | 0.0008156 | 1.00e-03 | [0.0008108, 0.0008206] |
| `nethermind` | 242 | 0.9353 | 0.0003057 | 1.00e-03 | [0.0002949, 0.0003154] |
| `reth` | 176 | 0.9809 | 0.000357 | 1.00e-03 | [0.0003501, 0.0003637] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.971
No. Observations:       1067                              RMSE:          49.15
Df Residuals:           1065                               MAE:          41.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.1584      5.3187       0.001     76.8118     97.8806
       opcount      0.0012      0.0000       0.001      0.0012      0.0012
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.892
Model:                  NNLS                    Adj. R-squared:          0.890
No. Observations:       44                                RMSE:          40.06
Df Residuals:           42                                 MAE:          34.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     19.5448     16.9526       0.149      0.0000     58.4382
       opcount      0.0005      0.0000       0.001      0.0004      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__erigon__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__erigon__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.994
No. Observations:       539                               RMSE:          14.34
Df Residuals:           537                                MAE:          10.33
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      3.6291      1.6810       0.015      0.3190      6.7217
       opcount      0.0008      0.0000       0.001      0.0008      0.0008
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__geth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__geth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       242                               RMSE:          18.94
Df Residuals:           240                                MAE:          14.51
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     27.7571      3.7893       0.001     20.8952     35.6487
       opcount      0.0003      0.0000       0.001      0.0003      0.0003
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__nethermind__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__nethermind__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       176                               RMSE:          11.75
Df Residuals:           174                                MAE:           9.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.3048      2.9291       0.001     14.9646     26.2695
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__reth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__reth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__reth__diagnostics.png)

</details>

### test_alt_bn128 — combo `double`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9382 | 0.001259 | 1.00e-03 | [0.001239, 0.001279] |
| `erigon` | 44 | 0.7086 | 0.000634 | 1.00e-03 | [0.0005175, 0.0007122] |
| `geth` | 539 | 0.9972 | 0.002315 | 1.00e-03 | [0.002305, 0.002327] |
| `nethermind` | 242 | 0.9378 | 0.0005176 | 1.00e-03 | [0.0004996, 0.0005357] |
| `reth` | 176 | 0.8648 | 0.0005931 | 1.00e-03 | [0.0005599, 0.0006292] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       1067                              RMSE:          76.14
Df Residuals:           1065                               MAE:          64.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    147.4706      8.3834       0.001    131.8892    164.7921
       opcount      0.0013      0.0000       0.001      0.0012      0.0013
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.709
Model:                  NNLS                    Adj. R-squared:          0.702
No. Observations:       44                                RMSE:          95.83
Df Residuals:           42                                 MAE:          61.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     69.9406     47.1826       0.045      0.0000    176.3389
       opcount      0.0006      0.0001       0.001      0.0005      0.0007
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__erigon__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__erigon__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       539                               RMSE:          28.75
Df Residuals:           537                                MAE:          22.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     11.4880      3.6210       0.001      4.2035     18.3862
       opcount      0.0023      0.0000       0.001      0.0023      0.0023
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__geth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__geth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       242                               RMSE:          31.41
Df Residuals:           240                                MAE:          24.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.6294      6.0073       0.001     36.8947     60.7555
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__nethermind__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__nethermind__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.865
Model:                  NNLS                    Adj. R-squared:          0.864
No. Observations:       176                               RMSE:          55.26
Df Residuals:           174                                MAE:          46.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.8768     15.0007       0.001    107.1287    166.2258
       opcount      0.0006      0.0000       0.001      0.0006      0.0006
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__reth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__reth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__reth__diagnostics.png)

</details>

### test_alt_bn128_uncachable

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8687 | 0.0008915 | 1.00e-03 | [0.0008683, 0.000913] |
| `erigon` | 44 | 0.9006 | 0.001052 | 1.00e-03 | [0.0009458, 0.001128] |
| `geth` | 539 | 0.9982 | 0.0036 | 1.00e-03 | [0.003586, 0.003613] |
| `nethermind` | 242 | 0.9044 | 0.0008175 | 1.00e-03 | [0.0007879, 0.0008485] |
| `reth` | 176 | 0.844 | 0.0009242 | 1.00e-03 | [0.0008614, 0.00099] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.869
Model:                  NNLS                    Adj. R-squared:          0.869
No. Observations:       1067                              RMSE:          74.20
Df Residuals:           1065                               MAE:          63.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    156.1199      8.1969       0.001    140.5788    172.6464
       opcount      0.0009      0.0000       0.001      0.0009      0.0009
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.901
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       44                                RMSE:          74.82
Df Residuals:           42                                 MAE:          62.54
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.8468     34.9838       0.071      0.0000    125.3510
       opcount      0.0011      0.0001       0.001      0.0009      0.0011
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__erigon__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__erigon__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          32.63
Df Residuals:           537                                MAE:          28.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     14.7764      4.0773       0.001      6.9447     22.8109
       opcount      0.0036      0.0000       0.001      0.0036      0.0036
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__geth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__geth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.904
Model:                  NNLS                    Adj. R-squared:          0.904
No. Observations:       242                               RMSE:          56.92
Df Residuals:           240                                MAE:          39.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     64.1296      9.6856       0.001     45.1101     82.4436
       opcount      0.0008      0.0000       0.001      0.0008      0.0008
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__nethermind__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__nethermind__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.843
No. Observations:       176                               RMSE:          85.08
Df Residuals:           174                                MAE:          72.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    214.7676     23.7868       0.001    168.2533    262.0326
       opcount      0.0009      0.0000       0.001      0.0009      0.0010
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__reth__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__reth__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__reth__diagnostics.png)

</details>

## ECPAIRING

### test_alt_bn128_benchmark

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 5335 | 0.8702 | 0.04865 | 1.00e-03 | [0.04793, 0.04942] |
| `erigon` | 220 | 0.6095 | 0.05138 | 1.00e-03 | [0.04723, 0.05569] |
| `geth` | 2695 | 0.9876 | 0.2733 | 1.00e-03 | [0.2718, 0.2748] |
| `nethermind` | 1210 | 0.9428 | 0.06799 | 1.00e-03 | [0.06519, 0.07078] |
| `reth` | 880 | 0.8203 | 0.04631 | 1.00e-03 | [0.04292, 0.05017] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.870
Model:                  NNLS                    Adj. R-squared:          0.870
No. Observations:       5335                              RMSE:          22.47
Df Residuals:           5332                               MAE:          18.95
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.1074      1.0924       0.001     48.8447     53.1473
       opcount      0.0487      0.0004       0.001      0.0479      0.0494
     num_pairs      0.0276      0.0002       0.001      0.0272      0.0279
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.609
Model:                  NNLS                    Adj. R-squared:          0.606
No. Observations:       220                               RMSE:          52.29
Df Residuals:           217                                MAE:          23.80
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     12.9724      7.4025       0.067      0.0000     27.0743
       opcount      0.0514      0.0022       0.001      0.0472      0.0557
     num_pairs      0.0318      0.0019       0.001      0.0288      0.0358
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__erigon__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__erigon__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       2695                              RMSE:          38.00
Df Residuals:           2692                               MAE:          30.27
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.3452      2.1321       0.001     12.3115     20.5312
       opcount      0.2733      0.0008       0.001      0.2718      0.2748
     num_pairs      0.1631      0.0004       0.001      0.1622      0.1640
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__geth__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__geth__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.943
Model:                  NNLS                    Adj. R-squared:          0.943
No. Observations:       1210                              RMSE:          48.16
Df Residuals:           1207                               MAE:          37.76
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     78.0138      4.0624       0.001     69.6036     85.9905
       opcount      0.0680      0.0014       0.001      0.0652      0.0708
     num_pairs      0.1033      0.0008       0.001      0.1018      0.1049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__nethermind__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__nethermind__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.820
Model:                  NNLS                    Adj. R-squared:          0.820
No. Observations:       880                               RMSE:          51.12
Df Residuals:           877                                MAE:          42.00
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    116.2032      6.2738       0.001    103.7028    128.7487
       opcount      0.0463      0.0019       0.001      0.0429      0.0502
     num_pairs      0.0577      0.0010       0.001      0.0559      0.0597
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__reth__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__reth__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__reth__diagnostics.png)

</details>

### test_ec_pairing

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 5335 | 0.8934 | 0.05285 | 1.00e-03 | [0.05208, 0.05361] |
| `erigon` | 220 | 0.9187 | 0.04797 | 1.00e-03 | [0.04503, 0.05103] |
| `geth` | 2695 | 0.9977 | 0.253 | 1.00e-03 | [0.2522, 0.2537] |
| `nethermind` | 1210 | 0.8886 | 0.05137 | 1.00e-03 | [0.04738, 0.05516] |
| `reth` | 880 | 0.838 | 0.08184 | 1.00e-03 | [0.07816, 0.08539] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.893
Model:                  NNLS                    Adj. R-squared:          0.893
No. Observations:       5335                              RMSE:          21.55
Df Residuals:           5332                               MAE:          17.86
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     43.0073      0.9943       0.001     41.0489     44.9760
       opcount      0.0528      0.0004       0.001      0.0521      0.0536
     num_pairs      0.0344      0.0002       0.001      0.0340      0.0347
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.919
Model:                  NNLS                    Adj. R-squared:          0.918
No. Observations:       220                               RMSE:          19.90
Df Residuals:           217                                MAE:          17.06
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     18.5129      4.3739       0.001     10.9067     27.4946
       opcount      0.0480      0.0015       0.001      0.0450      0.0510
     num_pairs      0.0398      0.0009       0.001      0.0381      0.0413
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__erigon__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__erigon__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       2695                              RMSE:          15.84
Df Residuals:           2692                               MAE:          12.96
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      9.6768      0.8895       0.001      8.0018     11.4946
       opcount      0.2530      0.0004       0.001      0.2522      0.2537
     num_pairs      0.1935      0.0002       0.001      0.1931      0.1939
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__geth__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__geth__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.889
Model:                  NNLS                    Adj. R-squared:          0.888
No. Observations:       1210                              RMSE:          62.84
Df Residuals:           1207                               MAE:          38.56
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.5884      6.5441       0.001     74.9090    101.0005
       opcount      0.0514      0.0020       0.001      0.0474      0.0552
     num_pairs      0.1144      0.0012       0.001      0.1121      0.1165
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__nethermind__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__nethermind__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.838
Model:                  NNLS                    Adj. R-squared:          0.838
No. Observations:       880                               RMSE:          46.13
Df Residuals:           877                                MAE:          39.04
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    107.5672      5.6894       0.001     96.3024    118.2596
       opcount      0.0818      0.0019       0.001      0.0782      0.0854
     num_pairs      0.0605      0.0010       0.001      0.0585      0.0625
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__reth__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__reth__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__reth__diagnostics.png)

</details>

## POINT_EVALUATION

### test_point_evaluation

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8398 | 0.18 | 1.00e-03 | [0.1747, 0.1853] |
| `erigon` | 44 | 0.8568 | 0.1779 | 1.00e-03 | [0.1561, 0.1935] |
| `geth` | 539 | 0.9981 | 1.256 | 1.00e-03 | [1.251, 1.259] |
| `nethermind` | 231 | 0.8821 | 0.2152 | 1.00e-03 | [0.2029, 0.2272] |
| `reth` | 176 | 0.8363 | 0.1911 | 1.00e-03 | [0.1773, 0.2048] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.840
Model:                  NNLS                    Adj. R-squared:          0.840
No. Observations:       1067                              RMSE:          99.54
Df Residuals:           1065                               MAE:          80.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    426.5919     12.0165       0.001    402.8128    450.2069
       opcount      0.1800      0.0028       0.001      0.1747      0.1853
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.857
Model:                  NNLS                    Adj. R-squared:          0.853
No. Observations:       44                                RMSE:          92.10
Df Residuals:           42                                 MAE:          75.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     59.0049     41.4451       0.072      0.0000    148.6747
       opcount      0.1779      0.0098       0.001      0.1561      0.1935
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__erigon__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__erigon__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          69.48
Df Residuals:           537                                MAE:          59.85
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      6.1181      6.9200       0.221      0.0000     22.8726
       opcount      1.2562      0.0021       0.001      1.2513      1.2590
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__geth__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__geth__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.882
Model:                  NNLS                    Adj. R-squared:          0.882
No. Observations:       231                               RMSE:          99.66
Df Residuals:           229                                MAE:          80.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    203.6383     25.5486       0.001    154.9240    257.1631
       opcount      0.2152      0.0060       0.001      0.2029      0.2272
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__nethermind__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__nethermind__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.836
Model:                  NNLS                    Adj. R-squared:          0.835
No. Observations:       176                               RMSE:         107.11
Df Residuals:           174                                MAE:          92.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    253.4639     31.3966       0.001    193.7719    316.0095
       opcount      0.1911      0.0070       0.001      0.1773      0.2048
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__reth__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__reth__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__reth__diagnostics.png)

</details>

### test_point_evaluation_uncachable

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.8705 | 0.2183 | 1.00e-03 | [0.2125, 0.2242] |
| `erigon` | 44 | 0.8816 | 0.191 | 1.00e-03 | [0.1689, 0.206] |
| `geth` | 539 | 0.9983 | 1.161 | 1.00e-03 | [1.157, 1.164] |
| `nethermind` | 235 | 0.09138 | 0.2945 | 1.00e-03 | [0.2093, 0.3504] |
| `reth` | 176 | 0.8271 | 0.1935 | 1.00e-03 | [0.1795, 0.2076] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.870
Model:                  NNLS                    Adj. R-squared:          0.870
No. Observations:       1067                              RMSE:          99.68
Df Residuals:           1065                               MAE:          85.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    211.0492     11.6390       0.001    187.3349    234.6860
       opcount      0.2183      0.0029       0.001      0.2125      0.2242
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.882
Model:                  NNLS                    Adj. R-squared:          0.879
No. Observations:       44                                RMSE:          82.84
Df Residuals:           42                                 MAE:          71.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     58.2389     39.6088       0.052      0.0000    147.7267
       opcount      0.1910      0.0099       0.001      0.1689      0.2060
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__erigon__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__erigon__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          55.93
Df Residuals:           537                                MAE:          47.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      3.8833      5.3741       0.267      0.0000     17.7836
       opcount      1.1614      0.0018       0.001      1.1572      1.1637
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__geth__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__geth__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.091
Model:                  NNLS                    Adj. R-squared:          0.087
No. Observations:       235                               RMSE:        1101.73
Df Residuals:           233                                MAE:         241.52
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     37.5895    113.5559       0.395      0.0000    377.8336
       opcount      0.2945      0.0397       0.001      0.2093      0.3504
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__nethermind__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__nethermind__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.827
Model:                  NNLS                    Adj. R-squared:          0.826
No. Observations:       176                               RMSE:         104.74
Df Residuals:           174                                MAE:          89.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    233.2821     30.2701       0.001    177.9257    292.5049
       opcount      0.1935      0.0073       0.001      0.1795      0.2076
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__reth__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__reth__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__reth__diagnostics.png)

</details>

## P256VERIFY

### test_p256verify

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.841 | 0.008646 | 1.00e-03 | [0.008402, 0.00888] |
| `erigon` | 44 | 0.6198 | 0.01295 | 1.00e-03 | [0.01023, 0.01488] |
| `geth` | 539 | 0.9982 | 0.07205 | 1.00e-03 | [0.07177, 0.07232] |
| `nethermind` | 231 | 0.8567 | 0.008672 | 1.00e-03 | [0.00821, 0.009093] |
| `reth` | 176 | 0.8305 | 0.008067 | 1.00e-03 | [0.007481, 0.008625] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.841
Model:                  NNLS                    Adj. R-squared:          0.841
No. Observations:       1067                              RMSE:          33.86
Df Residuals:           1065                               MAE:          27.85
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     88.1365      3.9057       0.001     80.5532     96.0510
       opcount      0.0086      0.0001       0.001      0.0084      0.0089
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.620
Model:                  NNLS                    Adj. R-squared:          0.611
No. Observations:       44                                RMSE:          91.38
Df Residuals:           42                                 MAE:          53.12
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     73.6213     44.8010       0.017      2.9034    176.2578
       opcount      0.0130      0.0012       0.001      0.0102      0.0149
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__erigon__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__erigon__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          27.88
Df Residuals:           537                                MAE:          23.58
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      6.7663      3.4776       0.033      0.0000     13.5870
       opcount      0.0720      0.0001       0.001      0.0718      0.0723
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__geth__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__geth__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.857
Model:                  NNLS                    Adj. R-squared:          0.856
No. Observations:       231                               RMSE:          31.93
Df Residuals:           229                                MAE:          22.89
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     59.3728      6.5779       0.001     46.8202     72.8897
       opcount      0.0087      0.0002       0.001      0.0082      0.0091
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__nethermind__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__nethermind__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.831
Model:                  NNLS                    Adj. R-squared:          0.830
No. Observations:       176                               RMSE:          32.82
Df Residuals:           174                                MAE:          27.23
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     72.3019      9.6192       0.001     54.0549     91.1328
       opcount      0.0081      0.0003       0.001      0.0075      0.0086
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__reth__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__reth__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__reth__diagnostics.png)

</details>

### test_p256verify_uncachable

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 1067 | 0.9017 | 0.01129 | 1.00e-03 | [0.01106, 0.01151] |
| `erigon` | 44 | 0.8899 | 0.01384 | 1.00e-03 | [0.01218, 0.01512] |
| `geth` | 539 | 0.9981 | 0.07258 | 1.00e-03 | [0.07231, 0.0728] |
| `nethermind` | 231 | 0.8907 | 0.008806 | 1.00e-03 | [0.008328, 0.009253] |
| `reth` | 176 | 0.8333 | 0.00814 | 1.00e-03 | [0.007565, 0.008737] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.902
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       1067                              RMSE:          33.33
Df Residuals:           1065                               MAE:          27.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     22.3916      3.3702       0.001     15.7216     29.3295
       opcount      0.0113      0.0001       0.001      0.0111      0.0115
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.890
Model:                  NNLS                    Adj. R-squared:          0.887
No. Observations:       44                                RMSE:          43.57
Df Residuals:           42                                 MAE:          36.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     41.6199     22.4759       0.019      1.2093     95.0529
       opcount      0.0138      0.0008       0.001      0.0122      0.0151
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__erigon__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__erigon__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__erigon__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       539                               RMSE:          28.06
Df Residuals:           537                                MAE:          23.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      5.2163      3.3366       0.067      0.0000     11.9832
       opcount      0.0726      0.0001       0.001      0.0723      0.0728
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__geth__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__geth__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.891
Model:                  NNLS                    Adj. R-squared:          0.890
No. Observations:       231                               RMSE:          27.60
Df Residuals:           229                                MAE:          22.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     57.1469      7.0178       0.001     44.1421     71.2071
       opcount      0.0088      0.0002       0.001      0.0083      0.0093
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__nethermind__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__nethermind__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.833
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       176                               RMSE:          32.57
Df Residuals:           174                                MAE:          27.89
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     74.0527      9.4323       0.001     55.6810     92.1971
       opcount      0.0081      0.0003       0.001      0.0076      0.0087
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__diagnostics.png)

</details>

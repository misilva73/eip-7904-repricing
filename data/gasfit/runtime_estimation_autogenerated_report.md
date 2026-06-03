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
| `besu` | 110 | 0.8662 | 1.763e-05 | 1.00e-03 | [1.638e-05, 1.896e-05] |
| `geth` | 165 | 0.8121 | 8.941e-06 | 1.00e-03 | [8.16e-06, 9.669e-06] |
| `nethermind` | 44 | 0.6535 | 7.35e-06 | 1.00e-03 | [5.217e-06, 9.617e-06] |
| `reth` | 11 | 0.7824 | 5.285e-06 | 1.00e-03 | [4.189e-06, 7.211e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.866
Model:                  NNLS                    Adj. R-squared:          0.865
No. Observations:       110                               RMSE:          54.70
Df Residuals:           108                                MAE:          47.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    130.8023     17.1832       0.001     97.7292    163.0970
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DIV__test_arithmetic__all__besu__regression.png)

![](figs/runtime/DIV__test_arithmetic__all__besu__bootstrap.png)

![](figs/runtime/DIV__test_arithmetic__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.812
Model:                  NNLS                    Adj. R-squared:          0.811
No. Observations:       165                               RMSE:          33.95
Df Residuals:           163                                MAE:          28.58
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     89.0752     10.9231       0.001     69.2863    111.4592
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.653
Model:                  NNLS                    Adj. R-squared:          0.645
No. Observations:       44                                RMSE:          42.25
Df Residuals:           42                                 MAE:          33.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    137.2436     31.3181       0.001     71.9984    197.8966
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
Dep. Variable:          test_runtime_ms              R-squared:          0.782
Model:                  NNLS                    Adj. R-squared:          0.758
No. Observations:       11                                RMSE:          22.00
Df Residuals:           9                                  MAE:          18.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     97.6283     20.2554       0.001     43.5648    121.3519
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
| `besu` | 110 | 0.844 | 1.791e-05 | 1.00e-03 | [1.645e-05, 1.936e-05] |
| `geth` | 165 | 0.8333 | 1.03e-05 | 1.00e-03 | [9.551e-06, 1.103e-05] |
| `nethermind` | 44 | 0.955 | 1.214e-05 | 1.00e-03 | [1.134e-05, 1.289e-05] |
| `reth` | 11 | 0.8252 | 7.756e-06 | 1.00e-03 | [6.291e-06, 1.007e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.843
No. Observations:       110                               RMSE:          60.80
Df Residuals:           108                                MAE:          50.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    131.4979     19.4159       0.001     95.0272    169.3176
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SDIV__test_arithmetic__all__besu__regression.png)

![](figs/runtime/SDIV__test_arithmetic__all__besu__bootstrap.png)

![](figs/runtime/SDIV__test_arithmetic__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.833
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       165                               RMSE:          36.36
Df Residuals:           163                                MAE:          30.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     80.8804     10.3550       0.001     61.2336    100.8381
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.955
Model:                  NNLS                    Adj. R-squared:          0.954
No. Observations:       44                                RMSE:          20.81
Df Residuals:           42                                 MAE:          16.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.3097     10.4648       0.001     66.9186    107.4513
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
Dep. Variable:          test_runtime_ms              R-squared:          0.825
Model:                  NNLS                    Adj. R-squared:          0.806
No. Observations:       11                                RMSE:          28.18
Df Residuals:           9                                  MAE:          23.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    101.5503     24.3499       0.002     48.2758    142.8045
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
| `besu` | 110 | 0.8653 | 2.07e-05 | 1.00e-03 | [1.917e-05, 2.239e-05] |
| `geth` | 165 | 0.837 | 1.179e-05 | 1.00e-03 | [1.089e-05, 1.263e-05] |
| `nethermind` | 44 | 0.9649 | 9.961e-06 | 1.00e-03 | [9.429e-06, 1.056e-05] |
| `reth` | 11 | 0.893 | 7.05e-06 | 1.00e-03 | [5.432e-06, 8.992e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.865
Model:                  NNLS                    Adj. R-squared:          0.864
No. Observations:       110                               RMSE:          64.37
Df Residuals:           108                                MAE:          56.09
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.1091     22.8256       0.001     83.5949    170.8882
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__127__besu__regression.png)

![](figs/runtime/MOD__test_mod__127__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__127__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.837
Model:                  NNLS                    Adj. R-squared:          0.836
No. Observations:       165                               RMSE:          41.03
Df Residuals:           163                                MAE:          34.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.4271     11.9952       0.001     63.1463    110.0246
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.964
No. Observations:       44                                RMSE:          14.97
Df Residuals:           42                                 MAE:          12.37
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     50.8339      7.8591       0.001     34.9043     65.4756
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
Dep. Variable:          test_runtime_ms              R-squared:          0.893
Model:                  NNLS                    Adj. R-squared:          0.881
No. Observations:       11                                RMSE:          19.24
Df Residuals:           9                                  MAE:          16.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     52.2640     26.8987       0.013      3.7038    100.8071
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
| `besu` | 110 | 0.8627 | 1.913e-05 | 1.00e-03 | [1.759e-05, 2.059e-05] |
| `geth` | 165 | 0.8449 | 1.134e-05 | 1.00e-03 | [1.051e-05, 1.211e-05] |
| `nethermind` | 44 | 0.9598 | 1.127e-05 | 1.00e-03 | [1.055e-05, 1.197e-05] |
| `reth` | 11 | 0.8114 | 9.97e-06 | 1.00e-03 | [7.039e-06, 1.302e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.863
Model:                  NNLS                    Adj. R-squared:          0.861
No. Observations:       110                               RMSE:          60.18
Df Residuals:           108                                MAE:          52.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.3285     19.9378       0.001     87.1004    167.9925
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__191__besu__regression.png)

![](figs/runtime/MOD__test_mod__191__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__191__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.845
Model:                  NNLS                    Adj. R-squared:          0.844
No. Observations:       165                               RMSE:          38.33
Df Residuals:           163                                MAE:          32.59
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     79.4200     11.5794       0.001     57.9082    103.2368
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.960
Model:                  NNLS                    Adj. R-squared:          0.959
No. Observations:       44                                RMSE:          18.20
Df Residuals:           42                                 MAE:          14.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.5337      9.3564       0.001     34.7592     71.3483
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
Dep. Variable:          test_runtime_ms              R-squared:          0.811
Model:                  NNLS                    Adj. R-squared:          0.790
No. Observations:       11                                RMSE:          37.90
Df Residuals:           9                                  MAE:          29.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     70.3823     43.6006       0.058      0.0000    153.8452
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
| `besu` | 110 | 0.8602 | 1.562e-05 | 1.00e-03 | [1.434e-05, 1.689e-05] |
| `geth` | 165 | 0.845 | 1.05e-05 | 1.00e-03 | [9.77e-06, 1.12e-05] |
| `nethermind` | 44 | 0.9671 | 1.093e-05 | 1.00e-03 | [1.029e-05, 1.159e-05] |
| `reth` | 11 | 0.8207 | 8.288e-06 | 1.00e-03 | [5.917e-06, 1.075e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.860
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       110                               RMSE:          49.64
Df Residuals:           108                                MAE:          43.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    101.6480     17.3385       0.001     67.8755    135.0517
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__255__besu__regression.png)

![](figs/runtime/MOD__test_mod__255__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__255__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.845
Model:                  NNLS                    Adj. R-squared:          0.844
No. Observations:       165                               RMSE:          35.44
Df Residuals:           163                                MAE:          29.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     72.2195     10.0203       0.001     53.4418     92.4402
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.967
Model:                  NNLS                    Adj. R-squared:          0.966
No. Observations:       44                                RMSE:          15.88
Df Residuals:           42                                 MAE:          12.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     46.7627      8.1679       0.001     30.7375     62.5476
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
Dep. Variable:          test_runtime_ms              R-squared:          0.821
Model:                  NNLS                    Adj. R-squared:          0.801
No. Observations:       11                                RMSE:          30.54
Df Residuals:           9                                  MAE:          25.95
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     61.6328     36.9923       0.045      0.0000    127.8561
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
| `besu` | 110 | 0.8548 | 1.535e-05 | 1.00e-03 | [1.406e-05, 1.668e-05] |
| `geth` | 165 | 0.8295 | 8.119e-06 | 1.00e-03 | [7.523e-06, 8.731e-06] |
| `nethermind` | 44 | 0.85 | 7.216e-06 | 1.00e-03 | [6.66e-06, 8.059e-06] |
| `reth` | 11 | 0.8607 | 5.954e-06 | 1.00e-03 | [4.846e-06, 7.176e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.855
Model:                  NNLS                    Adj. R-squared:          0.853
No. Observations:       110                               RMSE:          49.89
Df Residuals:           108                                MAE:          43.39
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     95.3500     17.7429       0.001     58.4579    130.2606
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MOD__test_mod__63__besu__regression.png)

![](figs/runtime/MOD__test_mod__63__besu__bootstrap.png)

![](figs/runtime/MOD__test_mod__63__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.830
Model:                  NNLS                    Adj. R-squared:          0.828
No. Observations:       165                               RMSE:          29.02
Df Residuals:           163                                MAE:          24.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     65.1924      8.6546       0.001     48.6867     82.5861
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.850
Model:                  NNLS                    Adj. R-squared:          0.846
No. Observations:       44                                RMSE:          23.90
Df Residuals:           42                                 MAE:          11.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     34.0247      6.7621       0.001     19.5757     45.6024
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
Dep. Variable:          test_runtime_ms              R-squared:          0.861
Model:                  NNLS                    Adj. R-squared:          0.845
No. Observations:       11                                RMSE:          18.88
Df Residuals:           9                                  MAE:          14.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     66.4261     18.2757       0.008     28.9624    100.1968
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
| `besu` | 110 | 0.8603 | 2.142e-05 | 1.00e-03 | [1.965e-05, 2.319e-05] |
| `geth` | 165 | 0.8326 | 1.21e-05 | 1.00e-03 | [1.114e-05, 1.304e-05] |
| `nethermind` | 44 | 0.959 | 1.105e-05 | 1.00e-03 | [1.042e-05, 1.173e-05] |
| `reth` | 11 | 0.7921 | 6.852e-06 | 1.00e-03 | [4.367e-06, 9.48e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.860
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       110                               RMSE:          68.05
Df Residuals:           108                                MAE:          59.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.7625     24.4825       0.001     89.7074    185.9858
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__127__besu__regression.png)

![](figs/runtime/SMOD__test_mod__127__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__127__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.833
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       165                               RMSE:          42.77
Df Residuals:           163                                MAE:          36.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.7814     13.1457       0.001     67.7392    119.3684
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.959
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       44                                RMSE:          18.01
Df Residuals:           42                                 MAE:          14.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     62.6299      9.1030       0.001     45.2224     81.3989
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
Dep. Variable:          test_runtime_ms              R-squared:          0.792
Model:                  NNLS                    Adj. R-squared:          0.769
No. Observations:       11                                RMSE:          27.68
Df Residuals:           9                                  MAE:          23.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     59.9738     37.4563       0.037      0.0000    136.3769
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
| `besu` | 110 | 0.8644 | 2.022e-05 | 1.00e-03 | [1.857e-05, 2.171e-05] |
| `geth` | 165 | 0.8419 | 1.15e-05 | 1.00e-03 | [1.074e-05, 1.228e-05] |
| `nethermind` | 44 | 0.9545 | 1.305e-05 | 1.00e-03 | [1.219e-05, 1.399e-05] |
| `reth` | 11 | 0.9109 | 1.136e-05 | 1.00e-03 | [8.92e-06, 1.338e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.864
Model:                  NNLS                    Adj. R-squared:          0.863
No. Observations:       110                               RMSE:          63.14
Df Residuals:           108                                MAE:          54.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.5107     21.5010       0.001     87.2020    172.2654
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__191__besu__regression.png)

![](figs/runtime/SMOD__test_mod__191__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__191__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.842
Model:                  NNLS                    Adj. R-squared:          0.841
No. Observations:       165                               RMSE:          39.28
Df Residuals:           163                                MAE:          33.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.7718     11.1105       0.001     67.1216    109.1406
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.955
Model:                  NNLS                    Adj. R-squared:          0.953
No. Observations:       44                                RMSE:          22.46
Df Residuals:           42                                 MAE:          17.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.0024     10.3408       0.001     28.9520     71.3590
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
Dep. Variable:          test_runtime_ms              R-squared:          0.911
Model:                  NNLS                    Adj. R-squared:          0.901
No. Observations:       11                                RMSE:          28.01
Df Residuals:           9                                  MAE:          22.96
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     52.2167     37.6434       0.086      0.0000    126.7686
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
| `besu` | 110 | 0.852 | 1.654e-05 | 1.00e-03 | [1.518e-05, 1.787e-05] |
| `geth` | 165 | 0.8418 | 1.082e-05 | 1.00e-03 | [1.003e-05, 1.16e-05] |
| `nethermind` | 44 | 0.9522 | 1.129e-05 | 1.00e-03 | [1.054e-05, 1.2e-05] |
| `reth` | 11 | 0.8871 | 9.547e-06 | 1.00e-03 | [7.236e-06, 1.16e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.852
Model:                  NNLS                    Adj. R-squared:          0.851
No. Observations:       110                               RMSE:          54.34
Df Residuals:           108                                MAE:          46.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.3872     18.5880       0.001     68.8889    141.8218
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__255__besu__regression.png)

![](figs/runtime/SMOD__test_mod__255__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__255__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.842
Model:                  NNLS                    Adj. R-squared:          0.841
No. Observations:       165                               RMSE:          36.99
Df Residuals:           163                                MAE:          30.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     69.9622     10.9188       0.001     49.2287     91.5729
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.952
Model:                  NNLS                    Adj. R-squared:          0.951
No. Observations:       44                                RMSE:          19.95
Df Residuals:           42                                 MAE:          15.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.0715      9.0423       0.001     34.7405     69.7202
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
Dep. Variable:          test_runtime_ms              R-squared:          0.887
Model:                  NNLS                    Adj. R-squared:          0.875
No. Observations:       11                                RMSE:          26.85
Df Residuals:           9                                  MAE:          21.58
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     50.3160     34.9517       0.066      0.0000    118.9965
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
| `besu` | 110 | 0.8316 | 1.621e-05 | 1.00e-03 | [1.492e-05, 1.765e-05] |
| `geth` | 165 | 0.8369 | 8.555e-06 | 1.00e-03 | [7.976e-06, 9.137e-06] |
| `nethermind` | 44 | 0.9536 | 8.501e-06 | 1.00e-03 | [7.916e-06, 9.043e-06] |
| `reth` | 11 | 0.8518 | 6.334e-06 | 1.00e-03 | [4.67e-06, 8.29e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.832
Model:                  NNLS                    Adj. R-squared:          0.830
No. Observations:       110                               RMSE:          57.50
Df Residuals:           108                                MAE:          48.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    118.2294     18.8805       0.001     81.8546    152.3563
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SMOD__test_mod__63__besu__regression.png)

![](figs/runtime/SMOD__test_mod__63__besu__bootstrap.png)

![](figs/runtime/SMOD__test_mod__63__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.837
Model:                  NNLS                    Adj. R-squared:          0.836
No. Observations:       165                               RMSE:          29.77
Df Residuals:           163                                MAE:          25.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     71.3957      8.1883       0.001     55.3290     87.5683
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.954
Model:                  NNLS                    Adj. R-squared:          0.953
No. Observations:       44                                RMSE:          14.78
Df Residuals:           42                                 MAE:          12.54
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     30.4817      6.5960       0.001     17.2546     43.0924
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
Dep. Variable:          test_runtime_ms              R-squared:          0.852
Model:                  NNLS                    Adj. R-squared:          0.835
No. Observations:       11                                RMSE:          20.83
Df Residuals:           9                                  MAE:          17.16
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.1322     27.3011       0.023      0.2892     98.5894
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
| `besu` | 110 | 0.8699 | 2.49e-05 | 1.00e-03 | [2.32e-05, 2.663e-05] |
| `geth` | 165 | 0.8443 | 1.645e-05 | 1.00e-03 | [1.532e-05, 1.765e-05] |
| `nethermind` | 44 | 0.971 | 1.381e-05 | 1.00e-03 | [1.31e-05, 1.463e-05] |
| `reth` | 11 | 0.9084 | 8.611e-06 | 1.00e-03 | [7.134e-06, 1.008e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.870
Model:                  NNLS                    Adj. R-squared:          0.869
No. Observations:       110                               RMSE:          43.36
Df Residuals:           108                                MAE:          37.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    108.5323     13.4271       0.001     83.2923    136.8624
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__regression.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__bootstrap.png)

![](figs/runtime/ADDMOD__test_mod_arithmetic__191__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.843
No. Observations:       165                               RMSE:          31.82
Df Residuals:           163                                MAE:          26.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     72.1930      9.2102       0.001     54.1620     89.9631
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       44                                RMSE:          10.74
Df Residuals:           42                                 MAE:           8.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     32.3836      5.6205       0.001     20.8160     42.7435
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
Dep. Variable:          test_runtime_ms              R-squared:          0.908
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       11                                RMSE:          12.31
Df Residuals:           9                                  MAE:          10.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.6470     11.3774       0.001     30.1509     73.3517
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
| `besu` | 110 | 0.8476 | 3.767e-05 | 1.00e-03 | [3.467e-05, 4.084e-05] |
| `geth` | 165 | 0.8402 | 2.392e-05 | 1.00e-03 | [2.211e-05, 2.575e-05] |
| `nethermind` | 44 | 0.921 | 3.742e-05 | 1.00e-03 | [3.472e-05, 4.077e-05] |
| `reth` | 11 | 0.9004 | 1.63e-05 | 1.00e-03 | [1.36e-05, 2.056e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.848
Model:                  NNLS                    Adj. R-squared:          0.846
No. Observations:       110                               RMSE:          71.93
Df Residuals:           108                                MAE:          62.17
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    157.3168     22.8777       0.001    114.3569    201.4668
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__regression.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__bootstrap.png)

![](figs/runtime/MULMOD__test_mod_arithmetic__191__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.840
Model:                  NNLS                    Adj. R-squared:          0.839
No. Observations:       165                               RMSE:          46.96
Df Residuals:           163                                MAE:          39.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    100.2541     14.6851       0.001     71.6749    130.4791
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.921
Model:                  NNLS                    Adj. R-squared:          0.919
No. Observations:       44                                RMSE:          49.33
Df Residuals:           42                                 MAE:          33.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     55.3522     19.5782       0.004     16.8027     93.2004
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
Dep. Variable:          test_runtime_ms              R-squared:          0.900
Model:                  NNLS                    Adj. R-squared:          0.889
No. Observations:       11                                RMSE:          24.41
Df Residuals:           9                                  MAE:          21.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.3102     25.6087       0.002     47.8750    149.9281
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
| `besu` | 440 | 0.7449 | 0.0001034 | 1.00e-03 | [9.721e-05, 0.0001094] |
| `geth` | 660 | 0.7832 | 8.125e-05 | 1.00e-03 | [7.803e-05, 8.444e-05] |
| `nethermind` | 176 | 0.7306 | 2.564e-05 | 3.00e-03 | [8.547e-06, 4.313e-05] |
| `reth` | 44 | 0.5348 | 1.62e-05 | 1.14e-01 | [0, 4.115e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.745
Model:                  NNLS                    Adj. R-squared:          0.744
No. Observations:       440                               RMSE:          94.11
Df Residuals:           437                                MAE:          77.43
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    142.8404     14.2630       0.001    116.6861    170.2324
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

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.783
Model:                  NNLS                    Adj. R-squared:          0.783
No. Observations:       660                               RMSE:          64.35
Df Residuals:           657                                MAE:          52.44
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.9061      8.3044       0.001     89.6263    122.7039
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.731
Model:                  NNLS                    Adj. R-squared:          0.727
No. Observations:       176                               RMSE:         154.85
Df Residuals:           173                                MAE:         124.45
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     81.4559     33.8014       0.006     16.6299    147.4092
       opcount      0.0000      0.0000       0.003      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.535
Model:                  NNLS                    Adj. R-squared:          0.512
No. Observations:       44                                RMSE:         110.65
Df Residuals:           41                                 MAE:          91.13
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     63.0365     42.7498       0.118      0.0000    148.0146
       opcount      0.0000      0.0000       0.114      0.0000      0.0000
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
| `besu` | 440 | 0.7733 | 0.000115 | 1.00e-03 | [0.0001087, 0.0001208] |
| `geth` | 660 | 0.7945 | 8.193e-05 | 1.00e-03 | [7.882e-05, 8.497e-05] |
| `nethermind` | 176 | 0.7373 | 2.568e-05 | 1.00e-03 | [8.55e-06, 4.309e-05] |
| `reth` | 44 | 0.5687 | 1.776e-05 | 9.00e-02 | [0, 4.052e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.773
Model:                  NNLS                    Adj. R-squared:          0.772
No. Observations:       440                               RMSE:          94.36
Df Residuals:           437                                MAE:          76.89
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    129.9397     14.7102       0.001    102.9790    160.2277
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

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.795
Model:                  NNLS                    Adj. R-squared:          0.794
No. Observations:       660                               RMSE:          62.95
Df Residuals:           657                                MAE:          51.07
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.4659      8.1835       0.001     80.7816    112.3133
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.737
Model:                  NNLS                    Adj. R-squared:          0.734
No. Observations:       176                               RMSE:         153.60
Df Residuals:           173                                MAE:         121.79
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     80.4098     34.1095       0.009     15.0781    144.7888
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
Dep. Variable:          test_runtime_ms              R-squared:          0.569
Model:                  NNLS                    Adj. R-squared:          0.548
No. Observations:       44                                RMSE:         109.54
Df Residuals:           41                                 MAE:          88.34
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.7411     41.0663       0.165      0.0000    135.2069
       opcount      0.0000      0.0000       0.090      0.0000      0.0000
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
| `besu` | 440 | 0.7647 | 0.0001177 | 1.00e-03 | [0.0001117, 0.0001234] |
| `geth` | 660 | 0.789 | 8.114e-05 | 1.00e-03 | [7.776e-05, 8.444e-05] |
| `nethermind` | 176 | 0.7363 | 2.555e-05 | 2.00e-03 | [8.978e-06, 4.359e-05] |
| `reth` | 44 | 0.5517 | 1.844e-05 | 5.10e-02 | [0, 4.174e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.765
Model:                  NNLS                    Adj. R-squared:          0.764
No. Observations:       440                               RMSE:          98.47
Df Residuals:           437                                MAE:          80.03
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.9549     14.8209       0.001     98.0341    155.0446
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

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.789
Model:                  NNLS                    Adj. R-squared:          0.788
No. Observations:       660                               RMSE:          63.35
Df Residuals:           657                                MAE:          51.70
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.1670      8.2268       0.001     86.7039    119.0345
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.736
Model:                  NNLS                    Adj. R-squared:          0.733
No. Observations:       176                               RMSE:         154.03
Df Residuals:           173                                MAE:         123.68
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     80.6019     32.0013       0.009     16.2957    142.9172
       opcount      0.0000      0.0000       0.002      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.552
Model:                  NNLS                    Adj. R-squared:          0.530
No. Observations:       44                                RMSE:         110.49
Df Residuals:           41                                 MAE:          90.74
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     50.2779     38.8141       0.151      0.0000    132.1075
       opcount      0.0000      0.0000       0.051      0.0000      0.0000
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
| `besu` | 440 | 0.7369 | 0.0001056 | 1.00e-03 | [9.959e-05, 0.0001115] |
| `geth` | 660 | 0.7968 | 8.118e-05 | 1.00e-03 | [7.805e-05, 8.423e-05] |
| `nethermind` | 176 | 0.7314 | 2.521e-05 | 2.00e-03 | [7.673e-06, 4.281e-05] |
| `reth` | 44 | 0.5557 | 1.803e-05 | 7.30e-02 | [0, 3.877e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.737
Model:                  NNLS                    Adj. R-squared:          0.736
No. Observations:       440                               RMSE:          96.27
Df Residuals:           437                                MAE:          79.83
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    162.2167     14.6775       0.001    132.8592    190.7527
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

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.797
Model:                  NNLS                    Adj. R-squared:          0.796
No. Observations:       660                               RMSE:          62.01
Df Residuals:           657                                MAE:          50.91
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    100.1701      8.1560       0.001     84.8186    116.2651
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
     msg_words      0.0000      0.0000       0.001      0.0000      0.0000
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
Dep. Variable:          test_runtime_ms              R-squared:          0.731
Model:                  NNLS                    Adj. R-squared:          0.728
No. Observations:       176                               RMSE:         154.59
Df Residuals:           173                                MAE:         124.79
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     83.4732     34.0535       0.003     20.3367    151.8663
       opcount      0.0000      0.0000       0.002      0.0000      0.0000
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
Model:                  NNLS                    Adj. R-squared:          0.534
No. Observations:       44                                RMSE:         109.48
Df Residuals:           41                                 MAE:          88.01
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     53.1670     39.7741       0.130      0.0000    137.2592
       opcount      0.0000      0.0000       0.073      0.0000      0.0000
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
| `besu` | 110 | 0.8344 | 0.006802 | 1.00e-03 | [0.006208, 0.007441] |
| `geth` | 165 | 0.8931 | 0.007889 | 1.00e-03 | [0.007456, 0.008318] |
| `nethermind` | 44 | 0.9504 | 0.007403 | 1.00e-03 | [0.006805, 0.007931] |
| `reth` | 11 | 0.8287 | 0.006435 | 1.00e-03 | [0.004683, 0.008447] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.834
Model:                  NNLS                    Adj. R-squared:          0.833
No. Observations:       110                               RMSE:          61.15
Df Residuals:           108                                MAE:          52.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    145.8495     19.8089       0.001    105.6202    184.4505
       opcount      0.0068      0.0003       0.001      0.0062      0.0074
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__regression.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__bootstrap.png)

![](figs/runtime/ECRECOVER__test_ecrecover__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.893
Model:                  NNLS                    Adj. R-squared:          0.892
No. Observations:       165                               RMSE:          55.06
Df Residuals:           163                                MAE:          47.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    111.7943     15.1753       0.001     82.0694    141.5771
       opcount      0.0079      0.0002       0.001      0.0075      0.0083
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
Dep. Variable:          test_runtime_ms              R-squared:          0.950
Model:                  NNLS                    Adj. R-squared:          0.949
No. Observations:       44                                RMSE:          34.13
Df Residuals:           42                                 MAE:          28.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.9285     21.4975       0.001     53.5419    133.4197
       opcount      0.0074      0.0003       0.001      0.0068      0.0079
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
Dep. Variable:          test_runtime_ms              R-squared:          0.829
Model:                  NNLS                    Adj. R-squared:          0.810
No. Observations:       11                                RMSE:          59.03
Df Residuals:           9                                  MAE:          51.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    125.3016     72.3388       0.055      0.0000    255.1661
       opcount      0.0064      0.0010       0.001      0.0047      0.0084
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
| `besu` | 440 | 0.8493 | 0.0003497 | 1.00e-03 | [0.0003347, 0.0003653] |
| `geth` | 660 | 0.9308 | 0.0001045 | 1.00e-03 | [0.0001018, 0.0001072] |
| `nethermind` | 176 | 0.9862 | 0.0001688 | 1.00e-03 | [0.0001657, 0.0001721] |
| `reth` | 44 | 0.9909 | 0.000381 | 1.00e-03 | [0.0003714, 0.0003893] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.849
Model:                  NNLS                    Adj. R-squared:          0.849
No. Observations:       440                               RMSE:          77.33
Df Residuals:           437                                MAE:          66.69
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    162.0063     13.2396       0.001    136.5034    186.9525
       opcount      0.0003      0.0000       0.001      0.0003      0.0004
    num_rounds      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__regression.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__bootstrap.png)

![](figs/runtime/BLAKE2F__test_blake2f_benchmark__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.931
Model:                  NNLS                    Adj. R-squared:          0.931
No. Observations:       660                               RMSE:          17.35
Df Residuals:           657                                MAE:          13.73
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     35.0251      2.4438       0.001     30.0608     39.8374
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
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
Dep. Variable:          test_runtime_ms              R-squared:          0.986
Model:                  NNLS                    Adj. R-squared:          0.986
No. Observations:       176                               RMSE:          10.80
Df Residuals:           173                                MAE:           8.72
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     28.8254      2.4769       0.001     23.9983     33.7913
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
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       44                                RMSE:          18.42
Df Residuals:           41                                 MAE:          14.41
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     13.3904      8.0089       0.054      0.0000     30.4595
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
| `besu` | 440 | 0.8525 | 0.0004259 | 1.00e-03 | [0.0004075, 0.0004451] |
| `geth` | 660 | 0.9234 | 0.000135 | 1.00e-03 | [0.0001311, 0.0001389] |
| `nethermind` | 176 | 0.9837 | 0.0001765 | 1.00e-03 | [0.0001728, 0.0001802] |
| `reth` | 44 | 0.9876 | 0.0003735 | 1.00e-03 | [0.0003634, 0.0003838] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.853
Model:                  NNLS                    Adj. R-squared:          0.852
No. Observations:       440                               RMSE:          75.93
Df Residuals:           437                                MAE:          65.58
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    154.8532     13.8010       0.001    128.2050    181.3330
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

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.923
Model:                  NNLS                    Adj. R-squared:          0.923
No. Observations:       660                               RMSE:          18.53
Df Residuals:           657                                MAE:          14.38
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     24.2944      2.7140       0.001     18.6921     29.5651
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
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
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       176                               RMSE:          10.19
Df Residuals:           173                                MAE:           8.09
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     30.8104      2.5647       0.001     25.9687     35.9412
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
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.987
No. Observations:       44                                RMSE:          17.26
Df Residuals:           41                                 MAE:          13.86
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     19.6605      7.9214       0.008      3.2700     34.7780
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
| `besu` | 110 | 0.8601 | 0.001795 | 1.00e-03 | [0.001651, 0.001925] |
| `geth` | 165 | 0.9036 | 0.0007348 | 1.00e-03 | [0.0006967, 0.0007752] |
| `nethermind` | 44 | 0.9677 | 0.0009866 | 1.00e-03 | [0.0009341, 0.001046] |
| `reth` | 11 | 0.8615 | 0.0007866 | 1.00e-03 | [0.0006068, 0.000986] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.860
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       110                               RMSE:          92.72
Df Residuals:           108                                MAE:          72.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.7044     31.8752       0.002     28.4997    155.2673
       opcount      0.0018      0.0001       0.001      0.0017      0.0019
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__regression.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__bootstrap.png)

![](figs/runtime/BLS12_G1ADD__test_bls12_381__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.904
Model:                  NNLS                    Adj. R-squared:          0.903
No. Observations:       165                               RMSE:          30.75
Df Residuals:           163                                MAE:          26.16
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     67.3362      9.0578       0.001     49.5428     84.3130
       opcount      0.0007      0.0000       0.001      0.0007      0.0008
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
Dep. Variable:          test_runtime_ms              R-squared:          0.968
Model:                  NNLS                    Adj. R-squared:          0.967
No. Observations:       44                                RMSE:          23.08
Df Residuals:           42                                 MAE:          18.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.1216     12.5784       0.001     65.0022    115.3911
       opcount      0.0010      0.0000       0.001      0.0009      0.0010
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
Dep. Variable:          test_runtime_ms              R-squared:          0.862
Model:                  NNLS                    Adj. R-squared:          0.846
No. Observations:       11                                RMSE:          40.40
Df Residuals:           9                                  MAE:          34.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     77.2084     49.6191       0.073      0.0000    166.7087
       opcount      0.0008      0.0001       0.001      0.0006      0.0010
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
| `besu` | 110 | 0.8737 | 0.002125 | 1.00e-03 | [0.00195, 0.002289] |
| `geth` | 165 | 0.9028 | 0.001066 | 1.00e-03 | [0.001003, 0.001126] |
| `nethermind` | 44 | 0.9752 | 0.0016 | 1.00e-03 | [0.001529, 0.001671] |
| `reth` | 11 | 0.808 | 0.001059 | 1.00e-03 | [0.0007592, 0.001348] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.874
Model:                  NNLS                    Adj. R-squared:          0.873
No. Observations:       110                               RMSE:          71.04
Df Residuals:           108                                MAE:          56.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.3122     25.6359       0.001     49.4325    146.7912
       opcount      0.0021      0.0001       0.001      0.0020      0.0023
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__regression.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__bootstrap.png)

![](figs/runtime/BLS12_G2ADD__test_bls12_381__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.903
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       165                               RMSE:          30.75
Df Residuals:           163                                MAE:          26.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     52.7834      9.4116       0.001     34.6479     71.3468
       opcount      0.0011      0.0000       0.001      0.0010      0.0011
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
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       44                                RMSE:          22.43
Df Residuals:           42                                 MAE:          17.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     72.4022     10.6740       0.001     51.5582     94.0554
       opcount      0.0016      0.0000       0.001      0.0015      0.0017
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
Dep. Variable:          test_runtime_ms              R-squared:          0.808
Model:                  NNLS                    Adj. R-squared:          0.787
No. Observations:       11                                RMSE:          45.40
Df Residuals:           9                                  MAE:          39.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     84.4381     51.4020       0.054      0.0000    180.6600
       opcount      0.0011      0.0002       0.001      0.0008      0.0013
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
| `besu` | 110 | 0.8749 | 0.0006589 | 1.00e-03 | [0.0006117, 0.0007145] |
| `geth` | 165 | 0.8829 | 0.0003985 | 1.00e-03 | [0.0003771, 0.0004212] |
| `nethermind` | 44 | 0.9658 | 0.0004658 | 1.00e-03 | [0.0004356, 0.000494] |
| `reth` | 11 | 0.9085 | 0.0005528 | 1.00e-03 | [0.0004417, 0.0007148] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.875
Model:                  NNLS                    Adj. R-squared:          0.874
No. Observations:       110                               RMSE:          58.72
Df Residuals:           108                                MAE:          50.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    131.6680     20.5174       0.001     91.9180    170.1355
       opcount      0.0007      0.0000       0.001      0.0006      0.0007
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.883
Model:                  NNLS                    Adj. R-squared:          0.882
No. Observations:       165                               RMSE:          34.21
Df Residuals:           163                                MAE:          29.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     77.5623      9.6807       0.001     58.0908     96.6127
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
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
Dep. Variable:          test_runtime_ms              R-squared:          0.966
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       44                                RMSE:          20.65
Df Residuals:           42                                 MAE:          16.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     78.5184     11.9635       0.001     55.8720    101.6383
       opcount      0.0005      0.0000       0.001      0.0004      0.0005
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
Dep. Variable:          test_runtime_ms              R-squared:          0.909
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       11                                RMSE:          41.33
Df Residuals:           9                                  MAE:          34.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    171.9035     52.1833       0.001     69.4383    267.9282
       opcount      0.0006      0.0001       0.001      0.0004      0.0007
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
| `besu` | 110 | 0.8702 | 0.0003767 | 1.00e-03 | [0.0003472, 0.0004063] |
| `geth` | 165 | 0.8072 | 0.0001091 | 1.00e-03 | [0.0001011, 0.0001166] |
| `nethermind` | 44 | 0.9722 | 0.0002132 | 1.00e-03 | [0.0002031, 0.000222] |
| `reth` | 11 | 0.9828 | 0.0003798 | 1.00e-03 | [0.0003446, 0.0003909] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.870
Model:                  NNLS                    Adj. R-squared:          0.869
No. Observations:       110                               RMSE:          34.29
Df Residuals:           108                                MAE:          29.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     76.1501     12.0728       0.001     52.4391    100.9545
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_infinities__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.807
Model:                  NNLS                    Adj. R-squared:          0.806
No. Observations:       165                               RMSE:          12.57
Df Residuals:           163                                MAE:          10.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     12.5956      3.4086       0.001      6.0828     19.4434
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
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
Dep. Variable:          test_runtime_ms              R-squared:          0.972
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       44                                RMSE:           8.49
Df Residuals:           42                                 MAE:           6.33
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     17.7732      3.9145       0.001     10.7202     25.6657
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
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
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       11                                RMSE:          11.85
Df Residuals:           9                                  MAE:           9.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      4.0743     11.0090       0.406      0.0000     36.4832
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
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
| `besu` | 110 | 0.8614 | 0.0003974 | 1.00e-03 | [0.0003649, 0.0004298] |
| `geth` | 165 | 0.8673 | 0.0001741 | 1.00e-03 | [0.0001642, 0.0001837] |
| `nethermind` | 44 | 0.9464 | 0.0002786 | 1.00e-03 | [0.0002608, 0.0002978] |
| `reth` | 11 | 0.9853 | 0.0003517 | 1.00e-03 | [0.0003336, 0.0003744] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.861
Model:                  NNLS                    Adj. R-squared:          0.860
No. Observations:       110                               RMSE:          37.56
Df Residuals:           108                                MAE:          32.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     81.1468     13.1300       0.001     54.8166    108.1374
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__add_negative__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.867
Model:                  NNLS                    Adj. R-squared:          0.866
No. Observations:       165                               RMSE:          16.05
Df Residuals:           163                                MAE:          12.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.2491      4.7040       0.001      7.5065     25.4910
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
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
Dep. Variable:          test_runtime_ms              R-squared:          0.946
Model:                  NNLS                    Adj. R-squared:          0.945
No. Observations:       44                                RMSE:          15.62
Df Residuals:           42                                 MAE:          12.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     33.3078      6.8878       0.001     18.9859     45.5530
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
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       11                                RMSE:          10.13
Df Residuals:           9                                  MAE:           6.89
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     24.2775      8.3067       0.006      8.0098     41.6059
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
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
| `besu` | 110 | 0.8619 | 0.0006691 | 1.00e-03 | [0.0006161, 0.000725] |
| `geth` | 165 | 0.8656 | 0.0004141 | 1.00e-03 | [0.0003882, 0.0004411] |
| `nethermind` | 44 | 0.9567 | 0.0004885 | 1.00e-03 | [0.0004577, 0.0005161] |
| `reth` | 11 | 0.8687 | 0.0006047 | 1.00e-03 | [0.0004838, 0.0007515] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.862
Model:                  NNLS                    Adj. R-squared:          0.861
No. Observations:       110                               RMSE:          63.13
Df Residuals:           108                                MAE:          54.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    130.0692     21.7947       0.001     85.8670    173.2777
       opcount      0.0007      0.0000       0.001      0.0006      0.0007
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128__double__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128__double__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128__double__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.866
Model:                  NNLS                    Adj. R-squared:          0.865
No. Observations:       165                               RMSE:          38.46
Df Residuals:           163                                MAE:          32.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     73.7514     10.6418       0.001     52.9805     94.6431
       opcount      0.0004      0.0000       0.001      0.0004      0.0004
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
Dep. Variable:          test_runtime_ms              R-squared:          0.957
Model:                  NNLS                    Adj. R-squared:          0.956
No. Observations:       44                                RMSE:          24.50
Df Residuals:           42                                 MAE:          19.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     53.0272     11.1305       0.001     30.7442     76.1044
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
Dep. Variable:          test_runtime_ms              R-squared:          0.869
Model:                  NNLS                    Adj. R-squared:          0.854
No. Observations:       11                                RMSE:          55.40
Df Residuals:           9                                  MAE:          47.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.2111     61.6802       0.019      6.1263    237.5319
       opcount      0.0006      0.0001       0.001      0.0005      0.0008
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
| `besu` | 110 | 0.8587 | 0.0009363 | 1.00e-03 | [0.0008589, 0.00101] |
| `geth` | 165 | 0.8657 | 0.0006122 | 1.00e-03 | [0.0005736, 0.0006532] |
| `nethermind` | 44 | 0.9735 | 0.0007895 | 1.00e-03 | [0.0007415, 0.0008358] |
| `reth` | 11 | 0.8046 | 0.0009439 | 1.00e-03 | [0.0006651, 0.001237] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.859
Model:                  NNLS                    Adj. R-squared:          0.857
No. Observations:       110                               RMSE:          81.33
Df Residuals:           108                                MAE:          70.51
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    165.8213     28.4895       0.001    111.9997    221.2769
       opcount      0.0009      0.0000       0.001      0.0009      0.0010
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__regression.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__bootstrap.png)

![](figs/runtime/ECADD__test_alt_bn128_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.866
Model:                  NNLS                    Adj. R-squared:          0.865
No. Observations:       165                               RMSE:          51.62
Df Residuals:           163                                MAE:          44.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    106.4372     15.0787       0.001     77.6807    134.9949
       opcount      0.0006      0.0000       0.001      0.0006      0.0007
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
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.973
No. Observations:       44                                RMSE:          27.91
Df Residuals:           42                                 MAE:          22.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     78.7185     15.9447       0.001     51.2433    110.9521
       opcount      0.0008      0.0000       0.001      0.0007      0.0008
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
Dep. Variable:          test_runtime_ms              R-squared:          0.805
Model:                  NNLS                    Adj. R-squared:          0.783
No. Observations:       11                                RMSE:          99.57
Df Residuals:           9                                  MAE:          91.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    196.1474    119.1188       0.042      0.0000    409.7211
       opcount      0.0009      0.0002       0.001      0.0007      0.0012
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
| `besu` | 550 | 0.8514 | 0.04727 | 1.00e-03 | [0.04479, 0.04975] |
| `geth` | 825 | 0.8164 | 0.04431 | 1.00e-03 | [0.04217, 0.04644] |
| `nethermind` | 220 | 0.9544 | 0.07004 | 1.00e-03 | [0.06368, 0.07693] |
| `reth` | 55 | 0.8217 | 0.05296 | 1.00e-03 | [0.03915, 0.06797] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.851
Model:                  NNLS                    Adj. R-squared:          0.851
No. Observations:       550                               RMSE:          23.64
Df Residuals:           547                                MAE:          20.23
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     51.5762      3.5638       0.001     44.4670     58.6609
       opcount      0.0473      0.0012       0.001      0.0448      0.0498
     num_pairs      0.0268      0.0006       0.001      0.0258      0.0280
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__regression.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__bootstrap.png)

![](figs/runtime/ECPAIRING__test_alt_bn128_benchmark__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.816
Model:                  NNLS                    Adj. R-squared:          0.816
No. Observations:       825                               RMSE:          26.06
Df Residuals:           822                                MAE:          22.01
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     55.0012      3.4283       0.001     48.6299     61.9188
       opcount      0.0443      0.0011       0.001      0.0422      0.0464
     num_pairs      0.0265      0.0005       0.001      0.0255      0.0275
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
Dep. Variable:          test_runtime_ms              R-squared:          0.954
Model:                  NNLS                    Adj. R-squared:          0.954
No. Observations:       220                               RMSE:          44.10
Df Residuals:           217                                MAE:          35.85
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     82.8645      9.9241       0.001     64.0965    102.1045
       opcount      0.0700      0.0034       0.001      0.0637      0.0769
     num_pairs      0.1066      0.0018       0.001      0.1032      0.1101
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
Dep. Variable:          test_runtime_ms              R-squared:          0.822
Model:                  NNLS                    Adj. R-squared:          0.815
No. Observations:       55                                RMSE:          52.00
Df Residuals:           52                                 MAE:          43.82
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    100.7731     26.0460       0.001     52.7262    155.6279
       opcount      0.0530      0.0073       0.001      0.0391      0.0680
     num_pairs      0.0589      0.0041       0.001      0.0511      0.0671
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
| `besu` | 550 | 0.8846 | 0.05167 | 1.00e-03 | [0.04919, 0.05389] |
| `geth` | 825 | 0.8748 | 0.04294 | 1.00e-03 | [0.04113, 0.04476] |
| `nethermind` | 220 | 0.9656 | 0.05588 | 1.00e-03 | [0.05081, 0.0607] |
| `reth` | 55 | 0.8437 | 0.08764 | 1.00e-03 | [0.07391, 0.1038] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.885
Model:                  NNLS                    Adj. R-squared:          0.884
No. Observations:       550                               RMSE:          22.09
Df Residuals:           547                                MAE:          18.43
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     43.2803      3.3375       0.001     37.1079     49.7297
       opcount      0.0517      0.0012       0.001      0.0492      0.0539
     num_pairs      0.0338      0.0006       0.001      0.0325      0.0350
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__regression.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__bootstrap.png)

![](figs/runtime/ECPAIRING__test_ec_pairing__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.875
Model:                  NNLS                    Adj. R-squared:          0.875
No. Observations:       825                               RMSE:          24.73
Df Residuals:           822                                MAE:          20.48
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.2404      2.9563       0.001     42.0421     53.9883
       opcount      0.0429      0.0010       0.001      0.0411      0.0448
     num_pairs      0.0399      0.0006       0.001      0.0388      0.0410
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
Dep. Variable:          test_runtime_ms              R-squared:          0.966
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       220                               RMSE:          34.87
Df Residuals:           217                                MAE:          27.19
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     83.0606      7.9058       0.001     67.6223     97.6628
       opcount      0.0559      0.0026       0.001      0.0508      0.0607
     num_pairs      0.1191      0.0017       0.001      0.1159      0.1225
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
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.838
No. Observations:       55                                RMSE:          46.18
Df Residuals:           52                                 MAE:          38.30
Df Model:               2      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    103.4828     23.7322       0.001     58.2760    152.9596
       opcount      0.0876      0.0076       0.001      0.0739      0.1038
     num_pairs      0.0604      0.0042       0.001      0.0525      0.0689
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
| `besu` | 110 | 0.8183 | 0.1729 | 1.00e-03 | [0.1543, 0.1914] |
| `geth` | 165 | 0.8389 | 0.1997 | 1.00e-03 | [0.1845, 0.2136] |
| `nethermind` | 44 | 0.9534 | 0.228 | 1.00e-03 | [0.2107, 0.2448] |
| `reth` | 11 | 0.8351 | 0.1944 | 1.00e-03 | [0.1419, 0.2528] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.818
Model:                  NNLS                    Adj. R-squared:          0.817
No. Observations:       110                               RMSE:         103.18
Df Residuals:           108                                MAE:          83.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    438.0000     41.1363       0.001    360.5598    519.6851
       opcount      0.1729      0.0098       0.001      0.1543      0.1914
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.839
Model:                  NNLS                    Adj. R-squared:          0.838
No. Observations:       165                               RMSE:         110.84
Df Residuals:           163                                MAE:          94.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    232.0398     32.8952       0.001    172.9437    299.0556
       opcount      0.1997      0.0074       0.001      0.1845      0.2136
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
Dep. Variable:          test_runtime_ms              R-squared:          0.953
Model:                  NNLS                    Adj. R-squared:          0.952
No. Observations:       44                                RMSE:          63.86
Df Residuals:           42                                 MAE:          55.09
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    186.3428     41.3435       0.001    106.9303    268.3020
       opcount      0.2280      0.0087       0.001      0.2107      0.2448
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
Dep. Variable:          test_runtime_ms              R-squared:          0.835
Model:                  NNLS                    Adj. R-squared:          0.817
No. Observations:       11                                RMSE:         109.41
Df Residuals:           9                                  MAE:          93.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    239.4412    129.2485       0.035      0.0000    485.4976
       opcount      0.1944      0.0299       0.001      0.1419      0.2528
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
| `besu` | 110 | 0.8362 | 0.2142 | 1.00e-03 | [0.1949, 0.2318] |
| `geth` | 165 | 0.8494 | 0.1964 | 1.00e-03 | [0.1834, 0.2109] |
| `nethermind` | 44 | 0.9412 | 0.2518 | 1.00e-03 | [0.2295, 0.2733] |
| `reth` | 11 | 0.822 | 0.1925 | 1.00e-03 | [0.1407, 0.2515] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.836
Model:                  NNLS                    Adj. R-squared:          0.835
No. Observations:       110                               RMSE:         112.24
Df Residuals:           108                                MAE:          96.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    212.2147     37.8824       0.001    144.5157    288.5825
       opcount      0.2142      0.0096       0.001      0.1949      0.2318
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__regression.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__bootstrap.png)

![](figs/runtime/POINT_EVALUATION__test_point_evaluation_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.849
Model:                  NNLS                    Adj. R-squared:          0.848
No. Observations:       165                               RMSE:          97.90
Df Residuals:           163                                MAE:          82.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    189.8109     28.2186       0.001    131.3737    243.6496
       opcount      0.1964      0.0069       0.001      0.1834      0.2109
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
Dep. Variable:          test_runtime_ms              R-squared:          0.941
Model:                  NNLS                    Adj. R-squared:          0.940
No. Observations:       44                                RMSE:          74.48
Df Residuals:           42                                 MAE:          59.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    125.3111     44.6423       0.001     41.9872    217.4718
       opcount      0.2518      0.0114       0.001      0.2295      0.2733
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
Dep. Variable:          test_runtime_ms              R-squared:          0.822
Model:                  NNLS                    Adj. R-squared:          0.802
No. Observations:       11                                RMSE:         106.03
Df Residuals:           9                                  MAE:          88.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    236.5538    122.1172       0.022      4.4362    462.9998
       opcount      0.1925      0.0297       0.001      0.1407      0.2515
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
| `besu` | 110 | 0.8412 | 0.008487 | 1.00e-03 | [0.007774, 0.009158] |
| `geth` | 165 | 0.8396 | 0.01211 | 1.00e-03 | [0.01128, 0.013] |
| `nethermind` | 44 | 0.9529 | 0.009257 | 1.00e-03 | [0.008447, 0.00997] |
| `reth` | 11 | 0.7765 | 0.0079 | 1.00e-03 | [0.005403, 0.0107] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.841
Model:                  NNLS                    Adj. R-squared:          0.840
No. Observations:       110                               RMSE:          33.21
Df Residuals:           108                                MAE:          28.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     77.5096     10.6147       0.001     56.4341     98.9148
       opcount      0.0085      0.0004       0.001      0.0078      0.0092
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.840
Model:                  NNLS                    Adj. R-squared:          0.839
No. Observations:       165                               RMSE:          47.68
Df Residuals:           163                                MAE:          40.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.2172     12.9964       0.001     60.4807    110.5834
       opcount      0.0121      0.0004       0.001      0.0113      0.0130
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
Dep. Variable:          test_runtime_ms              R-squared:          0.953
Model:                  NNLS                    Adj. R-squared:          0.952
No. Observations:       44                                RMSE:          18.54
Df Residuals:           42                                 MAE:          16.12
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     52.9676     12.1013       0.001     29.3111     76.0622
       opcount      0.0093      0.0004       0.001      0.0084      0.0100
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
Dep. Variable:          test_runtime_ms              R-squared:          0.776
Model:                  NNLS                    Adj. R-squared:          0.752
No. Observations:       11                                RMSE:          38.17
Df Residuals:           9                                  MAE:          35.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     79.1004     42.8966       0.044      0.0000    156.3218
       opcount      0.0079      0.0014       0.001      0.0054      0.0107
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
| `besu` | 110 | 0.8944 | 0.01113 | 1.00e-03 | [0.01036, 0.01183] |
| `geth` | 165 | 0.8355 | 0.01201 | 1.00e-03 | [0.01114, 0.01288] |
| `nethermind` | 44 | 0.9551 | 0.009407 | 1.00e-03 | [0.008622, 0.0101] |
| `reth` | 11 | 0.9207 | 0.008502 | 1.00e-03 | [0.00667, 0.01001] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.894
Model:                  NNLS                    Adj. R-squared:          0.893
No. Observations:       110                               RMSE:          34.21
Df Residuals:           108                                MAE:          27.99
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     24.7037     10.6930       0.014      2.9976     46.0385
       opcount      0.0111      0.0004       0.001      0.0104      0.0118
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__besu__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.835
Model:                  NNLS                    Adj. R-squared:          0.834
No. Observations:       165                               RMSE:          47.68
Df Residuals:           163                                MAE:          40.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.3477     13.8441       0.001     64.8622    118.9507
       opcount      0.0120      0.0005       0.001      0.0111      0.0129
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
Dep. Variable:          test_runtime_ms              R-squared:          0.955
Model:                  NNLS                    Adj. R-squared:          0.954
No. Observations:       44                                RMSE:          18.24
Df Residuals:           42                                 MAE:          15.17
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     50.7271     12.4522       0.001     27.9928     76.0464
       opcount      0.0094      0.0004       0.001      0.0086      0.0101
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
Dep. Variable:          test_runtime_ms              R-squared:          0.921
Model:                  NNLS                    Adj. R-squared:          0.912
No. Observations:       11                                RMSE:          22.33
Df Residuals:           9                                  MAE:          20.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     73.4584     23.3954       0.001     28.0535    119.9872
       opcount      0.0085      0.0008       0.001      0.0067      0.0100
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__regression.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__bootstrap.png)

![](figs/runtime/P256VERIFY__test_p256verify_uncachable__all__reth__diagnostics.png)

</details>

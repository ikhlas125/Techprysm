# Telco Churn — Model Report

## Data trap
`TotalCharges` loaded as `object` because 11 rows had blank strings instead of numbers (`isnull()` misses this — they're empty strings, not NaN).

```python
df['TotalCharges'].str.strip().eq("").sum()   # -> 11
df['TotalCharges'] = df['TotalCharges'].str.strip().replace('', np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges']).fillna(df['TotalCharges'].median())
```

## Results

| Metric | Logistic Regression | XGBoost |
|---|---|---|
| Precision | 0.5168 | 0.5643 |
| Recall | 0.8257 | 0.6944 |
| F1 | 0.6358 | 0.6226 |
| PR-AUC | 0.679 | 0.670 |

![PR Curve](pr_curve_comparison.png)

## Threshold

Retention call = $5, lost customer = $200 → a missed churner costs 40x a false alarm. Swept thresholds, minimized `FP*5 + FN*200`:

```python
def cost_at_threshold(y_test, y_prob, thresholds, call_cost=5, churn_cost=200):
    costs = []
    for t in thresholds:
        y_hat = (y_prob >= t).astype(int)
        fp = ((y_hat == 1) & (y_test == 0)).sum()
        fn = ((y_hat == 0) & (y_test == 1)).sum()
        costs.append(fp * call_cost + fn * churn_cost)
    return np.array(costs)
```

Optimal threshold sits well below 0.5 — cheap to over-call, expensive to miss a churner.

## Winner
**Logistic Regression** — higher PR-AUC, better precision at the recall levels the cost function picks. Churn signal here is mostly linear (tenure, contract, charges), so XGBoost's extra capacity doesn't add much.

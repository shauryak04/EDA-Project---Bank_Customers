# Bank Customers – Exploratory Data Analysis

Understand a bank's customer base — demographics, income, balances and credit scores — and how these relate to loan status.

## Dataset

**File:** `data/bank_customers.csv`

Key columns used:

- Age
- Gender
- City
- AccountType – Savings / Current
- Income
- Balance
- CreditScore
- LoanStatus

## What the analysis does

1. Inspect structure and summary statistics
2. Check for missing values and duplicate rows
3. Univariate analysis of customer demographics and finances
4. Bivariate analysis against loan status
5. Correlation of numeric features
6. Average income by city

## Visualisations

| Chart | Type |
|-------|------|
| Age Distribution | Histogram |
| Gender Distribution | Bar chart |
| Savings vs Current | Pie chart of account types |
| Income Distribution | Box plot |
| Balance vs Credit Score | Scatter plot |
| Loan Status by Income | Box plot |
| Loan Status by Credit Score | Box plot |
| Correlation Heatmap | Heatmap of numeric features |
| Average Income per City | Bar chart |

## Questions explored

- Do customers with approved loans have higher income or credit scores?
- Is account balance related to credit score?
- Which cities have the highest average income?

## Key insights

<!-- Run the script and write 3–5 findings here, e.g. "Customers in X had the highest ..." -->

- _Add your findings here_

## How to run

From the root of the repository:

```bash
pip install -r requirements.txt
python 03_bank_customers_eda/bank_customers_eda.py
```

Make sure `bank_customers.csv` is in the `data/` folder. Each chart opens in a window; close it to see the next one.

## Tools

Python · pandas · matplotlib · seaborn

---
[← Back to all projects](../README.md)

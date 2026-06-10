# Data Dictionary

## Project

Mutual Fund Analytics Platform

## Purpose

This document describes the datasets used in the project, including column definitions, data types, business meanings, and source references.

---

# 1. Fund Master Dataset

**Source:** 01_fund_master.csv

| Column             | Data Type | Description                         |
| ------------------ | --------- | ----------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier       |
| fund_house         | String    | Asset Management Company (AMC)      |
| scheme_name        | String    | Mutual fund scheme name             |
| category           | String    | Fund category (Equity, Debt)        |
| sub_category       | String    | Specific scheme classification      |
| plan               | String    | Direct or Regular plan              |
| launch_date        | Date      | Scheme launch date                  |
| benchmark          | String    | Benchmark index used for comparison |
| expense_ratio_pct  | Float     | Annual expense ratio percentage     |
| exit_load_pct      | Float     | Exit load charged on redemption     |
| min_sip_amount     | Integer   | Minimum SIP investment amount       |
| min_lumpsum_amount | Integer   | Minimum lump sum investment         |
| fund_manager       | String    | Fund manager name                   |
| risk_category      | String    | Risk classification                 |
| sebi_category_code | String    | SEBI category code                  |

---

# 2. NAV History Dataset

**Source:** 02_nav_history.csv

| Column    | Data Type | Description              |
| --------- | --------- | ------------------------ |
| amfi_code | Integer   | Unique scheme identifier |
| date      | Date      | NAV date                 |
| nav       | Float     | Net Asset Value per unit |

---

# 3. AUM Dataset

**Source:** 03_aum_by_fund_house.csv

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | Date      | Reporting date            |
| fund_house     | String    | Asset Management Company  |
| aum_lakh_crore | Float     | Total AUM in lakh crore   |
| aum_crore      | Integer   | Total AUM in crore        |
| num_schemes    | Integer   | Number of schemes managed |

---

# 4. SIP Dataset

**Source:** 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                          |
| ------------------------- | --------- | ------------------------------------ |
| month                     | Date      | Reporting month                      |
| sip_inflow_crore          | Integer   | Monthly SIP inflow in crore          |
| active_sip_accounts_crore | Float     | Active SIP accounts in crore         |
| new_sip_accounts_lakh     | Float     | New SIP accounts opened              |
| sip_aum_lakh_crore        | Float     | SIP assets under management          |
| yoy_growth_pct            | Float     | Year-over-Year SIP growth percentage |

---

# 5. Category Inflows Dataset

**Source:** 05_category_inflows.csv

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| month            | Date      | Reporting month            |
| category         | String    | Mutual fund category       |
| net_inflow_crore | Float     | Net inflow amount in crore |

---

# 6. Industry Folio Dataset

**Source:** 06_industry_folio_count.csv

| Column              | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | Date      | Reporting month       |
| total_folios_crore  | Float     | Total folios in crore |
| equity_folios_crore | Float     | Equity fund folios    |
| debt_folios_crore   | Float     | Debt fund folios      |
| hybrid_folios_crore | Float     | Hybrid fund folios    |
| others_folios_crore | Float     | Other category folios |

---

# 7. Scheme Performance Dataset

**Source:** 07_scheme_performance.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Scheme identifier             |
| scheme_name        | String    | Scheme name                   |
| fund_house         | String    | Fund house                    |
| category           | String    | Fund category                 |
| plan               | String    | Plan type                     |
| return_1yr_pct     | Float     | 1-year return percentage      |
| return_3yr_pct     | Float     | 3-year return percentage      |
| return_5yr_pct     | Float     | 5-year return percentage      |
| benchmark_3yr_pct  | Float     | Benchmark return              |
| alpha              | Float     | Excess return over benchmark  |
| beta               | Float     | Market sensitivity            |
| sharpe_ratio       | Float     | Risk-adjusted return metric   |
| sortino_ratio      | Float     | Downside-risk-adjusted return |
| std_dev_ann_pct    | Float     | Annualized volatility         |
| max_drawdown_pct   | Float     | Maximum historical drawdown   |
| aum_crore          | Integer   | Scheme AUM in crore           |
| expense_ratio_pct  | Float     | Expense ratio                 |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | String    | Risk grade                    |

---

# 8. Investor Transactions Dataset

**Source:** 08_investor_transactions.csv

| Column             | Data Type | Description                           |
| ------------------ | --------- | ------------------------------------- |
| investor_id        | String    | Unique investor identifier            |
| transaction_date   | Date      | Transaction date                      |
| amfi_code          | Integer   | Scheme identifier                     |
| transaction_type   | String    | SIP, Lumpsum, Redemption              |
| amount_inr         | Integer   | Transaction amount in INR             |
| state              | String    | Investor state                        |
| city               | String    | Investor city                         |
| city_tier          | String    | Tier 1, Tier 2, Tier 3 classification |
| age_group          | String    | Investor age category                 |
| gender             | String    | Investor gender                       |
| annual_income_lakh | Float     | Annual income in lakh INR             |
| payment_mode       | String    | Payment method                        |
| kyc_status         | String    | KYC verification status               |

---

# 9. Portfolio Holdings Dataset

**Source:** 09_portfolio_holdings.csv

| Column            | Data Type | Description                 |
| ----------------- | --------- | --------------------------- |
| amfi_code         | Integer   | Scheme identifier           |
| stock_symbol      | String    | Stock ticker symbol         |
| stock_name        | String    | Company name                |
| sector            | String    | Industry sector             |
| weight_pct        | Float     | Portfolio weight percentage |
| market_value_cr   | Float     | Market value in crore       |
| current_price_inr | Float     | Current stock price         |
| portfolio_date    | Date      | Portfolio reporting date    |

---

# 10. Benchmark Indices Dataset

**Source:** 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Index date           |
| index_name  | String    | Benchmark index name |
| close_value | Float     | Closing index value  |

---

# Notes

- All dates are stored in YYYY-MM-DD format after cleaning.
- AMFI Code acts as the primary key for scheme-level analysis.
- AUM values are reported in both crore and lakh crore units and should not be mixed.
- NAV data is forward-filled after reindexing to handle weekends and market holidays.
- All monetary values are expressed in Indian Rupees unless otherwise specified.

# Data Dictionary

## Project

Bluestock Fintech — Mutual Fund Analytics Platform

---

# 1. 01_fund_master.csv

| Column Name        | Data Type | Description                                  |
| ------------------ | --------- | -------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI mutual fund scheme code          |
| fund_house         | TEXT      | Mutual fund company name                     |
| scheme_name        | TEXT      | Official scheme name                         |
| category           | TEXT      | Fund category (Equity/Debt/Hybrid)           |
| sub_category       | TEXT      | Fund sub-category (Large Cap, Mid Cap, etc.) |
| plan               | TEXT      | Regular or Direct plan                       |
| launch_date        | DATE      | Scheme launch date                           |
| benchmark          | TEXT      | Benchmark index used by the fund             |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage              |
| exit_load_pct      | REAL      | Exit load percentage                         |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount                |
| min_lumpsum_amount | INTEGER   | Minimum lump sum investment                  |
| fund_manager       | TEXT      | Name of fund manager                         |
| risk_category      | TEXT      | Risk level of scheme                         |
| sebi_category_code | TEXT      | SEBI category classification code            |

---

# 2. 02_nav_history.csv

| Column Name | Data Type | Description                |
| ----------- | --------- | -------------------------- |
| amfi_code   | INTEGER   | Foreign key to fund_master |
| date        | DATE      | NAV date                   |
| nav         | REAL      | Net Asset Value of scheme  |

---

# 3. 03_aum_by_fund_house.csv

| Column Name    | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Quarterly reporting date  |
| fund_house     | TEXT      | Fund house name           |
| aum_lakh_crore | REAL      | AUM in lakh crore         |
| aum_crore      | INTEGER   | AUM in crore rupees       |
| num_schemes    | INTEGER   | Number of schemes managed |

---

# 4. 04_monthly_sip_inflows.csv

| Column Name               | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | TEXT      | Month in YYYY-MM format          |
| sip_inflow_crore          | INTEGER   | Monthly SIP inflow amount        |
| active_sip_accounts_crore | REAL      | Active SIP accounts in crore     |
| new_sip_accounts_lakh     | REAL      | New SIP registrations in lakh    |
| sip_aum_lakh_crore        | REAL      | SIP AUM in lakh crore            |
| yoy_growth_pct            | REAL      | Year-over-year growth percentage |

---

# 5. 05_category_inflows.csv

| Column Name      | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| month            | TEXT      | Reporting month            |
| category         | TEXT      | Mutual fund category       |
| net_inflow_crore | REAL      | Net inflow in crore rupees |

---

# 6. 06_industry_folio_count.csv

| Column Name         | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | TEXT      | Reporting month       |
| total_folios_crore  | REAL      | Total folios in crore |
| equity_folios_crore | REAL      | Equity folios count   |
| debt_folios_crore   | REAL      | Debt folios count     |
| hybrid_folios_crore | REAL      | Hybrid folios count   |
| others_folios_crore | REAL      | Other folios count    |

---

# 7. 07_scheme_performance.csv

| Column Name        | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | INTEGER   | Scheme code                   |
| scheme_name        | TEXT      | Scheme name                   |
| fund_house         | TEXT      | Fund house                    |
| category           | TEXT      | Fund category                 |
| return_1yr_pct     | REAL      | 1-year return percentage      |
| return_3yr_pct     | REAL      | 3-year CAGR                   |
| return_5yr_pct     | REAL      | 5-year CAGR                   |
| alpha              | REAL      | Alpha metric                  |
| beta               | REAL      | Beta metric                   |
| sharpe_ratio       | REAL      | Sharpe ratio                  |
| sortino_ratio      | REAL      | Sortino ratio                 |
| std_dev_ann_pct    | REAL      | Annualized standard deviation |
| max_drawdown_pct   | REAL      | Maximum drawdown percentage   |
| aum_crore          | INTEGER   | Assets under management       |
| expense_ratio_pct  | REAL      | Expense ratio                 |
| morningstar_rating | INTEGER   | Morningstar rating            |
| risk_grade         | TEXT      | Risk classification           |

---

# 8. 08_investor_transactions.csv

| Column Name        | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | TEXT      | Unique investor identifier  |
| transaction_date   | DATE      | Transaction date            |
| amfi_code          | INTEGER   | Mutual fund scheme code     |
| transaction_type   | TEXT      | SIP/Lumpsum/Redemption      |
| amount_inr         | INTEGER   | Transaction amount in INR   |
| state              | TEXT      | Investor state              |
| city               | TEXT      | Investor city               |
| city_tier          | TEXT      | T30/B30 city classification |
| age_group          | TEXT      | Investor age group          |
| gender             | TEXT      | Investor gender             |
| annual_income_lakh | REAL      | Annual income in lakh       |
| payment_mode       | TEXT      | Payment method              |
| kyc_status         | TEXT      | KYC verification status     |

---

# 9. 09_portfolio_holdings.csv

| Column Name       | Data Type | Description                 |
| ----------------- | --------- | --------------------------- |
| amfi_code         | INTEGER   | Scheme code                 |
| stock_symbol      | TEXT      | Stock ticker symbol         |
| stock_name        | TEXT      | Company name                |
| sector            | TEXT      | Business sector             |
| weight_pct        | REAL      | Portfolio weight percentage |
| market_value_cr   | REAL      | Market value in crore       |
| current_price_inr | REAL      | Current stock price         |
| portfolio_date    | DATE      | Portfolio snapshot date     |

---

# 10. 10_benchmark_indices.csv

| Column Name | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Daily closing value  |

# Data Dictionary

## 1. Fund Master
**Source:** 01_fund_master.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Scheme name |
| category | Text | Fund category |
| sub_category | Text | Sub category |
| plan | Text | Direct/Regular |
| launch_date | Date | Launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio (%) |
| exit_load_pct | Float | Exit load (%) |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lump sum |
| fund_manager | Text | Fund manager |
| risk_category | Text | Risk category |
| sebi_category_code | Text | SEBI category code |

---

## 2. NAV History

**Source:** 02_nav_history.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 3. AUM by Fund House

Source: 03_aum_by_fund_house.csv

---

## 4. Monthly SIP Inflows

Source: 04_monthly_sip_inflows.csv

---

## 5. Category Inflows

Source: 05_category_inflows.csv

---

## 6. Industry Folio Count

Source: 06_industry_folio_count.csv

---

## 7. Scheme Performance

Source: 07_scheme_performance.csv

---

## 8. Investor Transactions

Source: 08_investor_transactions.csv

---

## 9. Portfolio Holdings

Source: 09_portfolio_holdings.csv

---

## 10. Benchmark Indices

Source: 10_benchmark_indices.csv
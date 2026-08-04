# Data Dictionary

## 1. Fund Master

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Name of Scheme |
| category | Text | Equity / Debt |
| sub_category | Text | Fund Category |
| plan | Text | Direct / Regular |
| launch_date | Date | Scheme Launch Date |
| benchmark | Text | Benchmark Index |
| expense_ratio_pct | Float | Expense Ratio (%) |
| exit_load_pct | Float | Exit Load (%) |
| min_sip_amount | Integer | Minimum SIP Amount |
| min_lumpsum_amount | Integer | Minimum Lumpsum Amount |
| fund_manager | Text | Fund Manager Name |
| risk_category | Text | Risk Level |
| sebi_category_code | Text | SEBI Category Code |

---

## 2. NAV History

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 3. Investor Transactions

| Column | Data Type | Description |
|---------|----------|-------------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Scheme Code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Integer | Transaction Amount |
| state | Text | State |
| city | Text | City |
| city_tier | Text | T30 / B30 |
| age_group | Text | Investor Age Group |
| gender | Text | Gender |
| annual_income_lakh | Float | Annual Income |
| payment_mode | Text | Payment Method |
| kyc_status | Text | KYC Status |

---

## Source

Dataset provided by Bluestock Fintech Internship Assignment.
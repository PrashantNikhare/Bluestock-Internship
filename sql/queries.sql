-- Total Investors

SELECT COUNT(DISTINCT investor_id) AS total_investors
FROM investor_transactions;

-- Total Investment Amount

SELECT
SUM(amount_inr) AS total_investment
FROM investor_transactions;

-- Transaction Type Distribution

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- Average Investment Amount

SELECT
AVG(amount_inr) AS avg_investment
FROM investor_transactions;

-- Top 10 States by Investment

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

-- Top 10 Cities by Investment

SELECT
    city,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;

-- Gender-wise Investment

SELECT
    gender,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY gender;

-- KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS total_users
FROM investor_transactions
GROUP BY kyc_status;

-- Transactions by Payment Mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;

-- Top 10 Funds by Investment

SELECT
    amfi_code,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY amfi_code
ORDER BY total_investment DESC
LIMIT 10;
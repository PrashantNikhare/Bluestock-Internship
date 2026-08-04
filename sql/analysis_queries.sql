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
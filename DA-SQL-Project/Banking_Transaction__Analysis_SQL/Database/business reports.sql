USE banking_transaction_analysis;

SHOW TABLES;

DESCRIBE customers;
DESCRIBE accounts;
DESCRIBE transactions;
DESCRIBE transaction_types;

USE banking_transaction_analysis;

-- ==========================================
-- BANKING TRANSACTION ANALYSIS
-- BUSINESS REPORTS
-- ==========================================

-- 1. Total number of customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 2. Total number of accounts
SELECT COUNT(*) AS total_accounts
FROM accounts;

-- 3. Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- 4. Total transaction amount
SELECT SUM(amount) AS total_transaction_amount
FROM transactions;

-- 5. Average transaction amount
SELECT AVG(amount) AS average_transaction_amount
FROM transactions;

-- 6. Highest transaction amount
SELECT MAX(amount) AS highest_transaction
FROM transactions;

-- 7. Lowest transaction amount
SELECT MIN(amount) AS lowest_transaction
FROM transactions;

-- 8. Second highest distinct transaction amount
SELECT MAX(amount) AS second_highest_amount
FROM transactions
WHERE amount < (
    SELECT MAX(amount)
    FROM transactions
);

-- 9. Top 5 highest transactions
SELECT
    transaction_id,
    account_id,
    amount,
    transaction_date
FROM transactions
ORDER BY amount DESC
LIMIT 5;

-- 10. Monthly transaction report
SELECT
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY year, month;

-- 11. Yearly transaction report
SELECT
    YEAR(transaction_date) AS year,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY YEAR(transaction_date)
ORDER BY year;

-- 12. Daily transaction report
SELECT
    DATE(transaction_date) AS transaction_day,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY DATE(transaction_date)
ORDER BY transaction_day;

-- 13. Completed transactions
SELECT
    transaction_id,
    account_id,
    amount,
    status
FROM transactions
WHERE status = 'Completed';

-- 14. Pending transactions
SELECT
    transaction_id,
    account_id,
    amount,
    status
FROM transactions
WHERE status = 'Pending';

-- 15. Failed transactions
SELECT
    transaction_id,
    account_id,
    amount,
    status
FROM transactions
WHERE status = 'Failed';

-- 16. Transaction status summary
SELECT
    status,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY status;

-- 17. Account-wise transaction summary
SELECT
    account_id,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY account_id
ORDER BY total_amount DESC;

-- 18. Top 5 customers by transaction amount
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_amount
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_amount DESC
LIMIT 5;

-- 19. Customers with no transactions
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM accounts a
    JOIN transactions t
    ON a.account_id = t.account_id
    WHERE a.customer_id = c.customer_id
);

-- 20. Customers having more than 3 transactions
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(t.transaction_id) AS total_transactions
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(t.transaction_id) > 3;

-- 21. Accounts with highest balance
SELECT
    account_id,
    customer_id,
    balance
FROM accounts
ORDER BY balance DESC
LIMIT 5;

-- 22. Accounts with lowest balance
SELECT
    account_id,
    customer_id,
    balance
FROM accounts
ORDER BY balance ASC
LIMIT 5;

-- 23. Total balance across all accounts
SELECT
    SUM(balance) AS total_account_balance
FROM accounts;

-- 24. Average account balance
SELECT
    AVG(balance) AS average_account_balance
FROM accounts;

-- 25. Transaction type-wise summary
SELECT
    tt.type_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_amount
FROM transaction_types tt
LEFT JOIN transactions t
ON tt.transaction_type_id = t.transaction_type_id
GROUP BY tt.transaction_type_id, tt.type_name
ORDER BY total_transactions DESC;

-- 26. Most frequently used transaction type
SELECT
    tt.type_name,
    COUNT(t.transaction_id) AS usage_count
FROM transaction_types tt
JOIN transactions t
ON tt.transaction_type_id = t.transaction_type_id
GROUP BY tt.transaction_type_id, tt.type_name
ORDER BY usage_count DESC
LIMIT 1;

-- 27. High-value transactions
SELECT
    transaction_id,
    account_id,
    amount,
    transaction_date
FROM transactions
WHERE amount > 50000
ORDER BY amount DESC;

-- 28. Transactions above average amount
SELECT
    transaction_id,
    account_id,
    amount
FROM transactions
WHERE amount > (
    SELECT AVG(amount)
    FROM transactions
);

-- 29. Monthly completed transaction report
SELECT
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    COUNT(*) AS completed_count,
    SUM(amount) AS completed_amount
FROM transactions
WHERE status = 'Completed'
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY year, month;

-- 30. Monthly pending transaction report
SELECT
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    COUNT(*) AS pending_count,
    SUM(amount) AS pending_amount
FROM transactions
WHERE status = 'Pending'
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY year, month;

-- 31. Customer-wise account count
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(a.account_id) AS total_accounts
FROM customers c
LEFT JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_accounts DESC;

-- 32. Customers with multiple accounts
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(a.account_id) AS total_accounts
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(a.account_id) > 1;

-- 33. Percentage of completed transactions
SELECT
    ROUND(
        100.0 * SUM(
            CASE WHEN status = 'Completed'
            THEN 1 ELSE 0 END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS completion_percentage
FROM transactions;

-- 34. Percentage of failed transactions
SELECT
    ROUND(
        100.0 * SUM(
            CASE WHEN status = 'Failed'
            THEN 1 ELSE 0 END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS failure_percentage
FROM transactions;

-- 35. Rank accounts by transaction amount
SELECT
    account_id,
    total_amount,
    DENSE_RANK() OVER (
        ORDER BY total_amount DESC
    ) AS transaction_rank
FROM (
    SELECT
        account_id,
        SUM(amount) AS total_amount
    FROM transactions
    GROUP BY account_id
) AS account_summary;

-- ==========================================
-- END OF BUSINESS REPORTS
-- ==========================================

USE banking_transaction_analysis;

SHOW COLUMNS FROM transactions;
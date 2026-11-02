-- Query 1: Display all customers
SELECT customer_id, first_name, last_name, email, phone, city
FROM customers;
-- Query 2: Display all active bank accounts
SELECT account_number, customer_id, balance, account_status
FROM accounts
WHERE account_status = 'Active';
-- Query 3: Find customers from Hyderabad
SELECT customer_id, first_name, last_name, city
FROM customers
WHERE city = 'Hyderabad';
-- Query 4: Display unique cities where customers live
SELECT DISTINCT city
FROM customers
ORDER BY city;
-- Query 5: Find the five accounts with the highest balances
SELECT account_number, balance
FROM accounts
ORDER BY balance DESC
LIMIT 5;
-- Query 6: Find transactions between ₹1,000 and ₹5,000
SELECT reference_number, amount, transaction_date
FROM transactions
WHERE amount BETWEEN 1000 AND 5000
ORDER BY amount DESC;
-- Query 7: Find UPI transactions
SELECT reference_number, amount, transaction_date
FROM transactions t
JOIN transaction_types tt
    ON t.transaction_type_id = tt.transaction_type_id
WHERE tt.transaction_type_name = 'UPI';
-- Query 8: Find customers whose first name starts with 'S'
SELECT customer_id, first_name, last_name
FROM customers
WHERE first_name LIKE 'S%';
-- Query 9: Find transactions that are pending
SELECT t.reference_number, t.amount, t.transaction_date
FROM transactions t
JOIN transaction_statuses ts
    ON t.status_id = ts.status_id
WHERE ts.status_name = 'Pending';
-- Query 10: Display the second page of accounts
SELECT account_id, account_number, balance
FROM accounts
ORDER BY account_id
LIMIT 5 OFFSET 5;
-- Query 11: Calculate the total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;
-- Query 12: Calculate the total value of completed transactions
SELECT SUM(t.amount) AS total_completed_amount
FROM transactions t
JOIN transaction_statuses ts
    ON t.status_id = ts.status_id
WHERE ts.status_name = 'Completed';
-- Query 13: Calculate the average transaction amount
SELECT ROUND(AVG(amount), 2) AS average_transaction_amount
FROM transactions;
-- Query 14: Find the highest and lowest transaction amounts
SELECT
    MAX(amount) AS highest_amount,
    MIN(amount) AS lowest_amount
FROM transactions;
-- Query 15: Count transactions by transaction type
SELECT
    tt.transaction_type_name,
    COUNT(t.transaction_id) AS total_transactions
FROM transaction_types tt
LEFT JOIN transactions t
    ON tt.transaction_type_id = t.transaction_type_id
GROUP BY tt.transaction_type_name
ORDER BY total_transactions DESC;
-- Query 16: Calculate monthly transaction volume
SELECT
    DATE_FORMAT(transaction_date, '%Y-%m') AS transaction_month,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_transaction_amount
FROM transactions
GROUP BY DATE_FORMAT(transaction_date, '%Y-%m')
ORDER BY transaction_month;
-- Query 17: Find transaction statuses and their counts
SELECT
    ts.status_name,
    COUNT(t.transaction_id) AS total_transactions
FROM transaction_statuses ts
LEFT JOIN transactions t
    ON ts.status_id = t.status_id
GROUP BY ts.status_name;
-- Query 18: Find transaction types with total amounts above ₹10,000
SELECT
    tt.transaction_type_name,
    SUM(t.amount) AS total_amount
FROM transactions t
JOIN transaction_types tt
    ON t.transaction_type_id = tt.transaction_type_id
GROUP BY tt.transaction_type_name
HAVING SUM(t.amount) > 10000;
-- Query 19: Display customer names with their bank accounts
SELECT
    c.first_name,
    c.last_name,
    a.account_number,
    a.balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id;
    -- Query 20: Display account details with branch names
    SELECT
    a.account_number,
    c.first_name,
    c.last_name,
    b.branch_name,
    b.branch_city,
    a.balance
FROM accounts a
JOIN customers c
    ON a.customer_id = c.customer_id
JOIN branches b
    ON a.branch_id = b.branch_id;
    -- Query 21: Find the total account balance at each branch
    SELECT
    b.branch_name,
    b.branch_city,
    SUM(a.balance) AS total_branch_balance
FROM branches b
JOIN accounts a
    ON b.branch_id = a.branch_id
GROUP BY b.branch_id, b.branch_name, b.branch_city
ORDER BY total_branch_balance DESC;
-- Query 22: Display customer account types
SELECT
    c.first_name,
    c.last_name,
    a.account_number,
    at.account_type_name
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN account_types at
    ON a.account_type_id = at.account_type_id;
    -- Query 23: Display transactions with sender and receiver account numbers
    SELECT
    t.reference_number,
    sender.account_number AS sender_account,
    receiver.account_number AS receiver_account,
    tt.transaction_type_name,
    t.amount
FROM transactions t
LEFT JOIN accounts sender
    ON t.sender_account_id = sender.account_id
LEFT JOIN accounts receiver
    ON t.receiver_account_id = receiver.account_id
JOIN transaction_types tt
    ON t.transaction_type_id = tt.transaction_type_id;
    -- Query 24: Find customers who have loans
    SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    l.loan_type,
    l.loan_amount,
    l.loan_status
FROM customers c
JOIN loans l
    ON c.customer_id = l.customer_id;
    -- Query 25: Display cards with customer and account detail
    SELECT
    c.first_name,
    c.last_name,
    a.account_number,
    cd.card_type,
    cd.card_status,
    cd.expiry_date
FROM cards cd
JOIN accounts a
    ON cd.account_id = a.account_id
JOIN customers c
    ON a.customer_id = c.customer_id;
    -- Query 26: Find accounts with balances above the average
    SELECT account_number, balance
FROM accounts
WHERE balance > (
    SELECT AVG(balance)
    FROM accounts
);
-- Query 27: Find the second-highest account balance
SELECT MAX(balance) AS second_highest_balance
FROM accounts
WHERE balance < (
    SELECT MAX(balance)
    FROM accounts
);
-- Query 28: Find customers who have no loans
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM loans l
    WHERE l.customer_id = c.customer_id
);
-- Query 29: Find accounts with no recorded transactions
SELECT a.account_id, a.account_number
FROM accounts a
WHERE NOT EXISTS (
    SELECT 1
    FROM transactions t
    WHERE t.sender_account_id = a.account_id
       OR t.receiver_account_id = a.account_id
);
-- Query 30: Categorize transactions by amount
SELECT
    reference_number,
    amount,
    CASE
        WHEN amount >= 10000 THEN 'High Value'
        WHEN amount >= 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS transaction_category
FROM transactions;
-- Find the top three customers by total transaction activity
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(t.amount) AS transaction_activity
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.sender_account_id
    OR a.account_id = t.receiver_account_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY transaction_activity DESC
LIMIT 3;
-- Query 32: Calculate total approved loans by loan type
SELECT
    loan_type,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount
FROM loans
WHERE loan_status = 'Approved'
GROUP BY loan_type;
-- Query 33: Find branches with more than one account
SELECT
    b.branch_name,
    COUNT(a.account_id) AS total_accounts
FROM branches b
JOIN accounts a
    ON b.branch_id = a.branch_id
GROUP BY b.branch_id, b.branch_name
HAVING COUNT(a.account_id) > 1;
-- Query 34: Find customers with multiple beneficiaries
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(b.beneficiary_id) AS total_beneficiaries
FROM customers c
JOIN beneficiaries b
    ON c.customer_id = b.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(b.beneficiary_id) > 1;
-- Query 35: Display transactions with a missing sender or receiver account
SELECT
    reference_number,
    sender_account_id,
    receiver_account_id,
    amount
FROM transactions
WHERE sender_account_id IS NULL
   OR receiver_account_id IS NULL;

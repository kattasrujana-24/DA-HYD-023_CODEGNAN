-- View 1: Customer account details

CREATE OR REPLACE VIEW vw_customer_accounts AS
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    c.phone,
    a.account_id,
    a.account_number,
    at.account_type_name,
    a.balance,
    a.account_status
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN account_types at
    ON a.account_type_id = at.account_type_id;
    SELECT * FROM vw_customer_accounts;
  -- View 2: Transaction Summary
  
CREATE OR REPLACE VIEW vw_transaction_summary AS
SELECT
    t.transaction_id,
    t.reference_number,
    t.sender_account_id,
    sa.account_number AS sender_account_number,
    t.receiver_account_id,
    ra.account_number AS receiver_account_number,
    tt.transaction_type_name,
    ts.status_name AS transaction_status,
    t.amount,
    t.transaction_date,
    t.description
FROM transactions t
LEFT JOIN accounts sa
    ON t.sender_account_id = sa.account_id
LEFT JOIN accounts ra
    ON t.receiver_account_id = ra.account_id
JOIN transaction_types tt
    ON t.transaction_type_id = tt.transaction_type_id
JOIN transaction_statuses ts
    ON t.status_id = ts.status_id;
    SELECT * FROM vw_transaction_summary;
-- View 3: Monthly Transaction Report

CREATE OR REPLACE VIEW vw_monthly_transaction_report AS
SELECT
    YEAR(transaction_date) AS transaction_year,
    MONTH(transaction_date) AS transaction_month,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date);
SELECT * FROM vw_monthly_transaction_report;
-- View 4: Unsuccessful Transactions

CREATE OR REPLACE VIEW vw_unsuccessful_transactions AS
SELECT
    t.transaction_id,
    t.reference_number,
    t.sender_account_id,
    t.receiver_account_id,
    tt.transaction_type_name,
    ts.status_name AS transaction_status,
    t.amount,
    t.transaction_date,
    t.description
FROM transactions t
JOIN transaction_types tt
    ON t.transaction_type_id = tt.transaction_type_id
JOIN transaction_statuses ts
    ON t.status_id = ts.status_id
WHERE ts.status_name IN ('Failed', 'Pending', 'Reversed');
SELECT * FROM vw_unsuccessful_transactions;
-- View 5: Branch Account Summary

CREATE OR REPLACE VIEW vw_branch_account_summary AS
SELECT
    b.branch_id,
    b.branch_name,
    b.branch_city,
    b.branch_state,
    COUNT(a.account_id) AS total_accounts,
    COALESCE(SUM(a.balance), 0) AS total_balance
FROM branches b
LEFT JOIN accounts a
    ON b.branch_id = a.branch_id
GROUP BY
    b.branch_id,
    b.branch_name,
    b.branch_city,
    b.branch_state;
SELECT * FROM vw_branch_account_summary;

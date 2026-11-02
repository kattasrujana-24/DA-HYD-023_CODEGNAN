-- 1. Create index on customer name
CREATE INDEX idx_customer_name
ON customers(customer_name);

EXPLAIN
SELECT transaction_id, amount
FROM transactions
WHERE amount > 50000;


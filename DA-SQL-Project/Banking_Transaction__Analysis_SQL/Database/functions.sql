-- 1. Function to categorize transactions
USE Banking_Transaction_Analysis;

DROP FUNCTION IF EXISTS fn_transaction_category;

DELIMITER //

CREATE FUNCTION fn_transaction_category(p_amount DECIMAL(15,2))
RETURNS VARCHAR(30)
DETERMINISTIC
BEGIN
    IF p_amount >= 10000 THEN
        RETURN 'High Value';
    ELSEIF p_amount >= 5000 THEN
        RETURN 'Medium Value';
    ELSE
        RETURN 'Low Value';
    END IF;
END //

DELIMITER ;
SELECT fn_transaction_category(2000);
SELECT fn_transaction_category(7000);
SELECT fn_transaction_category(15000);
-- 2. Function to calculate transaction fee
DROP FUNCTION IF EXISTS fn_transaction_fee;

DELIMITER //

CREATE FUNCTION fn_transaction_fee(p_amount DECIMAL(15,2))
RETURNS DECIMAL(15,2)
DETERMINISTIC
BEGIN
    RETURN p_amount * 0.02;
END //

DELIMITER ;
SELECT fn_transaction_fee(5000);
-- 3. Function to calculate average transaction amount
DROP FUNCTION IF EXISTS fn_average_transaction;

DELIMITER //

CREATE FUNCTION fn_average_transaction(p_account_id INT)
RETURNS DECIMAL(15,2)
READS SQL DATA
BEGIN
    DECLARE v_average DECIMAL(15,2);

    SELECT AVG(amount)
    INTO v_average
    FROM transactions
    WHERE account_id = p_account_id;

    RETURN COALESCE(v_average, 0);
END //

DELIMITER ;
SELECT fn_average_transaction(1);
-- 4. Function to count transactions
DROP FUNCTION IF EXISTS fn_total_transactions;

DELIMITER //

CREATE FUNCTION fn_total_transactions(p_account_id INT)
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE v_count INT;

    SELECT COUNT(*)
    INTO v_count
    FROM transactions
    WHERE account_id = p_account_id;

    RETURN v_count;
END //

DELIMITER ;
SELECT fn_total_transactions(1);

-- 5. Function to calculate completed transaction amount
DROP FUNCTION IF EXISTS fn_successful_amount;

DELIMITER //

CREATE FUNCTION fn_successful_amount(p_account_id INT)
RETURNS DECIMAL(15,2)
READS SQL DATA
BEGIN
    DECLARE v_total DECIMAL(15,2);

    SELECT COALESCE(SUM(amount), 0)
    INTO v_total
    FROM transactions
    WHERE account_id = p_account_id
      AND transaction_status = 'Completed';

    RETURN v_total;
END //

DELIMITER ;
SHOW FUNCTION STATUS
WHERE Db = 'Banking_Transaction_Analysis'
AND Name = 'fn_successful_amount';
-- 6. Function to find highest transaction amount
DROP FUNCTION IF EXISTS fn_successful_amount;

DELIMITER //

CREATE FUNCTION fn_successful_amount(p_account_id INT)
RETURNS DECIMAL(15,2)
READS SQL DATA
BEGIN
    DECLARE total_amount DECIMAL(15,2) DEFAULT 0;

    SELECT COALESCE(SUM(amount), 0)
    INTO total_amount
    FROM transactions
    WHERE account_id = p_account_id
      AND transaction_status = 'Completed';

    RETURN total_amount;
END //

DELIMITER ;
USE Banking_Transaction_Analysis;

SHOW FUNCTION STATUS
WHERE Name = 'fn_successful_amount';


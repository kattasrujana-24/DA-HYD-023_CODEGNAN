-- Procedure 1: Get transactions by account ID

USE Banking_Transaction_Analysis;

DELIMITER //

DROP PROCEDURE IF EXISTS sp_account_transactions //

CREATE PROCEDURE sp_account_transactions(
    IN p_account_id INT
)
BEGIN
    SELECT
        transaction_id,
        account_id,
        transaction_type,
        amount,
        transaction_date,
        transaction_status
    FROM transactions
    WHERE account_id = p_account_id
    ORDER BY transaction_date DESC;
END //

DELIMITER ;
CALL sp_account_transactions(1);
-- Procedure 2: Get transactions above a specified amount

DELIMITER //

DROP PROCEDURE IF EXISTS sp_transactions_above_amount //

CREATE PROCEDURE sp_transactions_above_amount(
    IN p_min_amount DECIMAL(15,2)
)
BEGIN
    SELECT
        transaction_id,
        account_id,
        transaction_type,
        amount,
        transaction_date,
        transaction_status
    FROM transactions
    WHERE amount >= p_min_amount
    ORDER BY amount DESC;
END //

DELIMITER ;
CALL sp_transactions_above_amount(5000);

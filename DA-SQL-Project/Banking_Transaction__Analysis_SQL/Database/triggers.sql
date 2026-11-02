-- 1. Trigger to validate transaction amount
USE Banking_Transaction_Analysis;

DROP TRIGGER IF EXISTS trg_validate_transaction;

DELIMITER //

CREATE TRIGGER trg_validate_transaction
BEFORE INSERT ON transactions
FOR EACH ROW
BEGIN
    IF NEW.amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Transaction amount must be greater than zero';
    END IF;
END //

DELIMITER ;
-- 2. Trigger to validate account balance
DROP TRIGGER IF EXISTS trg_check_account_balance;

DELIMITER //

CREATE TRIGGER trg_check_account_balance
BEFORE UPDATE ON accounts
FOR EACH ROW
BEGIN
    IF NEW.balance < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Account balance cannot be negative';
    END IF;
END //

DELIMITER ;
-- DELIMITER ;


-- 3. Trigger to validate transaction updates
DROP TRIGGER IF EXISTS trg_validate_transaction_update;

DELIMITER //

CREATE TRIGGER trg_validate_transaction_update
BEFORE UPDATE ON transactions
FOR EACH ROW
BEGIN
    IF NEW.amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Updated transaction amount must be greater than zero';
    END IF;
END //

DELIMITER ;
-- 4. Prevent transaction deletion
DROP TRIGGER IF EXISTS trg_prevent_transaction_delete;

DELIMITER //

CREATE TRIGGER trg_prevent_transaction_delete
BEFORE DELETE ON transactions
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Transaction records cannot be deleted';
END //

DELIMITER ;
--  5. Prevent negative balance during account insertion
DROP TRIGGER IF EXISTS trg_check_balance_insert;

DELIMITER //

CREATE TRIGGER trg_check_balance_insert
BEFORE INSERT ON accounts
FOR EACH ROW
BEGIN
    IF NEW.balance < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Initial account balance cannot be negative';
    END IF;
END //

DELIMITER ;

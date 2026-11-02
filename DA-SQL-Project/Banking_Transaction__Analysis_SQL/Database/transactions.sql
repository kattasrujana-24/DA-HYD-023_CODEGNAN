
USE banking_transaction_analysis;

-- ==========================================
-- BANKING TRANSACTION ANALYSIS
-- TRANSACTION MANAGEMENT
-- ==========================================

-- 1. Create a demo table
DROP TABLE IF EXISTS transaction_demo;

CREATE TABLE transaction_demo (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(100),
    balance DECIMAL(12,2) NOT NULL
        CHECK (balance >= 0)
) ENGINE = InnoDB;

-- 2. Insert sample records
INSERT INTO transaction_demo
(account_id, account_name, balance)
VALUES
(1, 'Rahul', 50000),
(2, 'Priya', 30000),
(3, 'Kiran', 40000),
(4, 'Sneha', 60000),
(5, 'Ravi', 25000);

-- 3. Display accounts
SELECT * FROM transaction_demo;

-- ==========================================
-- 4. START TRANSACTION AND COMMIT
-- ==========================================

START TRANSACTION;

UPDATE transaction_demo
SET balance = balance + 5000
WHERE account_id = 1;

COMMIT;

SELECT * FROM transaction_demo;

-- ==========================================
-- 5. ROLLBACK
-- ==========================================

START TRANSACTION;

UPDATE transaction_demo
SET balance = balance - 2000
WHERE account_id = 2;

ROLLBACK;

SELECT * FROM transaction_demo;

-- ==========================================
-- 6. SAVEPOINT
-- ==========================================

START TRANSACTION;

UPDATE transaction_demo
SET balance = balance + 1000
WHERE account_id = 1;

SAVEPOINT sp1;

UPDATE transaction_demo
SET balance = balance + 2000
WHERE account_id = 2;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;

SELECT * FROM transaction_demo;

-- ==========================================
-- 7. MULTIPLE SAVEPOINTS
-- ==========================================

START TRANSACTION;

UPDATE transaction_demo
SET balance = balance + 1000
WHERE account_id = 1;

SAVEPOINT sp1;

UPDATE transaction_demo
SET balance = balance + 2000
WHERE account_id = 2;

SAVEPOINT sp2;

UPDATE transaction_demo
SET balance = balance + 3000
WHERE account_id = 3;

ROLLBACK TO SAVEPOINT sp2;

COMMIT;

SELECT * FROM transaction_demo;

-- ==========================================
-- 8. RELEASE SAVEPOINT
-- ==========================================

START TRANSACTION;

SAVEPOINT sp3;

RELEASE SAVEPOINT sp3;

COMMIT;

-- ==========================================
-- 9. BANK TRANSFER WITH ERROR HANDLING
-- ==========================================

DROP PROCEDURE IF EXISTS demo_bank_transfer;

DELIMITER $$

CREATE PROCEDURE demo_bank_transfer(
    IN p_sender INT,
    IN p_receiver INT,
    IN p_amount DECIMAL(12,2)
)
BEGIN
    DECLARE v_sender_balance DECIMAL(12,2);
    DECLARE v_receiver_balance DECIMAL(12,2);
    DECLARE v_sender_count INT DEFAULT 0;
    DECLARE v_receiver_count INT DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    IF p_amount IS NULL OR p_amount <= 0
       OR p_sender = p_receiver THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid transfer';
    END IF;

    SELECT COUNT(*) INTO v_sender_count
    FROM transaction_demo
    WHERE account_id = p_sender;

    SELECT COUNT(*) INTO v_receiver_count
    FROM transaction_demo
    WHERE account_id = p_receiver;

    IF v_sender_count = 0 OR v_receiver_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Account not found';
    END IF;

    -- Lock both accounts in a consistent order
    SELECT balance INTO v_sender_balance
    FROM transaction_demo
    WHERE account_id = LEAST(p_sender, p_receiver)
    FOR UPDATE;

    SELECT balance INTO v_receiver_balance
    FROM transaction_demo
    WHERE account_id = GREATEST(p_sender, p_receiver)
    FOR UPDATE;

    SELECT balance INTO v_sender_balance
    FROM transaction_demo
    WHERE account_id = p_sender;

    IF v_sender_balance < p_amount THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient balance';
    END IF;

    UPDATE transaction_demo
    SET balance = balance - p_amount
    WHERE account_id = p_sender;

    UPDATE transaction_demo
    SET balance = balance + p_amount
    WHERE account_id = p_receiver;

    COMMIT;
END$$

DELIMITER ;

-- 10. Transfer 3000 from Rahul to Priya
CALL demo_bank_transfer(1, 2, 3000);

-- 11. Check updated balances
SELECT * FROM transaction_demo;

-- ==========================================
-- 12. READ ONLY TRANSACTION
-- ==========================================

START TRANSACTION READ ONLY;

SELECT account_id, account_name, balance
FROM transaction_demo;

COMMIT;

-- ==========================================
-- 13. TRANSACTION ISOLATION LEVEL
-- ==========================================

SET SESSION TRANSACTION ISOLATION LEVEL
READ COMMITTED;

-- ==========================================
-- 14. FIND HIGHEST ACCOUNT BALANCE
-- ==========================================

SELECT account_id, account_name, balance
FROM transaction_demo
ORDER BY balance DESC
LIMIT 1;

-- ==========================================
-- 15. FIND LOWEST ACCOUNT BALANCE
-- ==========================================

SELECT account_id, account_name, balance
FROM transaction_demo
ORDER BY balance ASC
LIMIT 1;

-- ==========================================
-- 16. TOTAL ACCOUNT BALANCE
-- ==========================================

SELECT SUM(balance) AS total_balance
FROM transaction_demo;

-- ==========================================
-- 17. AVERAGE ACCOUNT BALANCE
-- ==========================================

SELECT AVG(balance) AS average_balance
FROM transaction_demo;

-- ==========================================
-- 18. ACCOUNTS WITH BALANCE > 30000
-- ==========================================

SELECT account_id, account_name, balance
FROM transaction_demo
WHERE balance > 30000;

-- ==========================================
-- 19. DISPLAY FINAL ACCOUNT DETAILS
-- ==========================================

SELECT
    account_id,
    account_name,
    balance
FROM transaction_demo
ORDER BY account_id;

-- ==========================================
-- END OF TRANSACTION MANAGEMENT
-- ==========================================

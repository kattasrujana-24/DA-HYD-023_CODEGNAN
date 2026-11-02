-- Table 1: branches
 CREATE TABLE branches (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL,
    ifsc_code VARCHAR(11) NOT NULL UNIQUE,
    branch_city VARCHAR(100) NOT NULL,
    branch_state VARCHAR(100) NOT NULL,
    branch_address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Table 2: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL UNIQUE,
    date_of_birth DATE,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Table 3: account_types
CREATE TABLE account_types (
    account_type_id INT PRIMARY KEY AUTO_INCREMENT,
    account_type_name VARCHAR(30) NOT NULL UNIQUE,
    minimum_balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    description VARCHAR(255),
    CHECK (minimum_balance >= 0)
);
-- Table 4: accounts
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(20) NOT NULL UNIQUE,
    customer_id INT NOT NULL,
    branch_id INT NOT NULL,
    account_type_id INT NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    account_status VARCHAR(20) NOT NULL DEFAULT 'Active',
    opened_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id),
    FOREIGN KEY (account_type_id) REFERENCES account_types(account_type_id),
    CHECK (balance >= 0),
    CHECK (account_status IN ('Active', 'Inactive', 'Closed'))
);
-- Table 5: transaction_types
CREATE TABLE transaction_types (
    transaction_type_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_type_name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(255)
);
-- Table 6: transaction_statuses
CREATE TABLE transaction_statuses (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(255)
);
-- );


-- Table 7: transactions
CREATE TABLE transactions (
    transaction_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    reference_number VARCHAR(40) NOT NULL UNIQUE,
    sender_account_id INT,
    receiver_account_id INT,
    transaction_type_id INT NOT NULL,
    status_id INT NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    transaction_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    FOREIGN KEY (sender_account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (receiver_account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (transaction_type_id) REFERENCES transaction_types(transaction_type_id),
    FOREIGN KEY (status_id) REFERENCES transaction_statuses(status_id),
    CHECK (amount > 0),
    CHECK (sender_account_id IS NOT NULL OR receiver_account_id IS NOT NULL),
    CHECK (sender_account_id IS NULL OR receiver_account_id IS NULL OR sender_account_id <> receiver_account_id)
);
-- Table 8: beneficiaries
CREATE TABLE beneficiaries (
    beneficiary_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    beneficiary_name VARCHAR(100) NOT NULL,
    beneficiary_account_number VARCHAR(30) NOT NULL,
    beneficiary_ifsc VARCHAR(11),
    bank_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
-- Table 9: cards
CREATE TABLE cards (
    card_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    card_number VARCHAR(25) NOT NULL UNIQUE,
    card_type VARCHAR(20) NOT NULL,
    expiry_date DATE NOT NULL,
    card_status VARCHAR(20) NOT NULL DEFAULT 'Active',
    issued_date DATE NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id),
    CHECK (card_type IN ('Debit', 'Credit')),
    CHECK (card_status IN ('Active', 'Blocked', 'Expired'))
);
-- Table 10: loans
CREATE TABLE loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    branch_id INT NOT NULL,
    loan_type VARCHAR(50) NOT NULL,
    loan_amount DECIMAL(15,2) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    loan_status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id),
    CHECK (loan_amount > 0),
    CHECK (interest_rate >= 0 AND interest_rate <= 100),
    CHECK (end_date IS NULL OR end_date >= start_date),
    CHECK (loan_status IN ('Pending', 'Approved', 'Rejected', 'Closed'))
);

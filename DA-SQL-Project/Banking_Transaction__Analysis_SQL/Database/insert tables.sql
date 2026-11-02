--- 1. Insert data into branches
INSERT INTO branches
(branch_name, ifsc_code, branch_city, branch_state, branch_address)
VALUES
('Main Branch', 'SBIN0001001', 'Hyderabad', 'Telangana', 'Abids'),
('City Branch', 'SBIN0001002', 'Warangal', 'Telangana', 'Hanamkonda'),
('Central Branch', 'SBIN0001003', 'Karimnagar', 'Telangana', 'Tower Circle'),
('North Branch', 'SBIN0001004', 'Secunderabad', 'Telangana', 'Paradise'),
('South Branch', 'SBIN0001005', 'Vijayawada', 'Andhra Pradesh', 'MG Road'),
('East Branch', 'SBIN0001006', 'Visakhapatnam', 'Andhra Pradesh', 'Dwaraka Nagar'),
('West Branch', 'SBIN0001007', 'Mumbai', 'Maharashtra', 'Andheri'),
('Metro Branch', 'SBIN0001008', 'Bengaluru', 'Karnataka', 'Indiranagar'),
('Lake Branch', 'SBIN0001009', 'Chennai', 'Tamil Nadu', 'T Nagar'),
('Park Branch', 'SBIN0001010', 'Pune', 'Maharashtra', 'Shivaji Nagar');
-- 2. Insert data into customers
INSERT INTO customers
(first_name, last_name, email, phone, date_of_birth, address, city, state)
VALUES
('Rahul', 'Sharma', 'rahul@example.com', '9000000001', '1998-05-12', 'Ameerpet', 'Hyderabad', 'Telangana'),
('Priya', 'Reddy', 'priya@example.com', '9000000002', '2000-08-20', 'Kukatpally', 'Hyderabad', 'Telangana'),
('Arjun', 'Kumar', 'arjun@example.com', '9000000003', '1997-02-15', 'Madhapur', 'Hyderabad', 'Telangana'),
('Sneha', 'Patel', 'sneha@example.com', '9000000004', '1999-11-03', 'Banjara Hills', 'Hyderabad', 'Telangana'),
('Kiran', 'Rao', 'kiran@example.com', '9000000005', '1996-07-25', 'Hanamkonda', 'Warangal', 'Telangana'),
('Ananya', 'Das', 'ananya@example.com', '9000000006', '2001-04-18', 'MG Road', 'Bengaluru', 'Karnataka'),
('Vikram', 'Singh', 'vikram@example.com', '9000000007', '1995-09-09', 'Andheri', 'Mumbai', 'Maharashtra'),
('Divya', 'Nair', 'divya@example.com', '9000000008', '2000-12-14', 'T Nagar', 'Chennai', 'Tamil Nadu'),
('Rohit', 'Verma', 'rohit@example.com', '9000000009', '1998-03-30', 'Dwaraka Nagar', 'Visakhapatnam', 'Andhra Pradesh'),
('Meena', 'Joshi', 'meena@example.com', '9000000010', '1997-06-21', 'Shivaji Nagar', 'Pune', 'Maharashtra');
-- 3. Insert data into account_types
INSERT INTO account_types
(account_type_name, minimum_balance, description)
VALUES
('Savings', 1000.00, 'Personal savings account'),
('Current', 5000.00, 'Business current account'),
('Salary', 0.00, 'Salary account'),
('Fixed Deposit', 10000.00, 'Fixed deposit account'),
('Recurring Deposit', 500.00, 'Recurring deposit account'),
('Student', 0.00, 'Student banking account'),
('Senior Citizen', 1000.00, 'Account for senior citizens'),
('NRI', 10000.00, 'Non-resident Indian account'),
('Joint', 1000.00, 'Joint bank account'),
('Premium', 25000.00, 'Premium banking account');
-- 4. Insert data into accounts
INSERT INTO accounts
(account_number, customer_id, branch_id, account_type_id, balance, account_status, opened_date)
VALUES
('BA100001', 1, 1, 1, 25000.00, 'Active', '2024-01-10'),
('BA100002', 2, 1, 3, 18000.00, 'Active', '2024-02-15'),
('BA100003', 3, 2, 2, 75000.00, 'Active', '2024-03-20'),
('BA100004', 4, 3, 1, 12000.00, 'Active', '2024-04-05'),
('BA100005', 5, 3, 5, 30000.00, 'Active', '2024-05-12'),
('BA100006', 6, 8, 6, 8000.00, 'Active', '2024-06-18'),
('BA100007', 7, 7, 2, 95000.00, 'Active', '2024-07-22'),
('BA100008', 8, 9, 1, 15000.00, 'Inactive', '2024-08-09'),
('BA100009', 9, 6, 3, 22000.00, 'Active', '2024-09-14'),
('BA100010', 10, 10, 10, 150000.00, 'Active', '2024-10-25');
-- 5. Insert data into transaction_types
INSERT INTO transaction_types
(transaction_type_name, description)
VALUES
('Deposit', 'Money deposited into an account'),
('Withdrawal', 'Money withdrawn from an account'),
('Transfer', 'Money transferred between accounts'),
('UPI', 'Unified Payments Interface transaction'),
('NEFT', 'National Electronic Funds Transfer'),
('IMPS', 'Immediate Payment Service'),
('RTGS', 'Real Time Gross Settlement'),
('ATM', 'ATM cash transaction'),
('Online Payment', 'Online purchase or bill payment'),
('Fee', 'Bank service fee');
-- 6. Insert data into transaction_statuses
INSERT INTO transaction_statuses
(status_name, description)
VALUES
('Completed', 'Transaction completed successfully'),
('Pending', 'Transaction awaiting processing'),
('Failed', 'Transaction was unsuccessful'),
('Reversed', 'Transaction amount was reversed'),
('Cancelled', 'Transaction was cancelled');
-- 7. Insert data into transactions
INSERT INTO transactions
(reference_number, sender_account_id, receiver_account_id,
 transaction_type_id, status_id, amount, transaction_date, description)
VALUES
('TXN1001', NULL, 1, 1, 1, 10000.00, '2026-01-05 09:30:00', 'Cash deposit'),
('TXN1002', 1, NULL, 2, 1, 2000.00, '2026-01-06 10:15:00', 'Cash withdrawal'),
('TXN1003', 1, 2, 3, 1, 1500.00, '2026-01-08 11:00:00', 'Account transfer'),
('TXN1004', 2, 3, 4, 1, 2500.00, '2026-01-10 12:30:00', 'UPI payment'),
('TXN1005', 3, NULL, 2, 1, 5000.00, '2026-01-12 14:00:00', 'ATM withdrawal'),
('TXN1006', NULL, 4, 1, 1, 8000.00, '2026-01-15 09:00:00', 'Branch deposit'),
('TXN1007', 4, 5, 5, 2, 3500.00, '2026-01-18 15:20:00', 'NEFT transfer'),
('TXN1008', 5, 1, 6, 1, 1200.00, '2026-01-20 16:00:00', 'IMPS transfer'),
('TXN1009', 6, NULL, 8, 3, 1000.00, '2026-02-02 10:45:00', 'ATM transaction failed'),
('TXN1010', NULL, 7, 1, 1, 20000.00, '2026-02-04 11:30:00', 'Cash deposit'),
('TXN1011', 7, 8, 3, 1, 7500.00, '2026-02-06 13:00:00', 'Account transfer'),
('TXN1012', 8, NULL, 9, 1, 2200.00, '2026-02-08 17:15:00', 'Online bill payment'),
('TXN1013', 9, 10, 7, 1, 15000.00, '2026-02-10 12:00:00', 'RTGS transfer'),
('TXN1014', 10, NULL, 10, 1, 500.00, '2026-02-12 08:30:00', 'Bank service fee'),
('TXN1015', NULL, 2, 1, 1, 6000.00, '2026-02-15 09:45:00', 'Cash deposit'),
('TXN1016', 2, 5, 4, 2, 1800.00, '2026-02-18 14:30:00', 'UPI payment pending'),
('TXN1017', 3, NULL, 2, 1, 3000.00, '2026-03-01 10:00:00', 'Cash withdrawal'),
('TXN1018', 5, 6, 3, 4, 2500.00, '2026-03-05 11:15:00', 'Transfer reversed'),
('TXN1019', NULL, 9, 1, 1, 4500.00, '2026-03-10 12:45:00', 'Cash deposit'),
('TXN1020', 1, 10, 4, 5, 900.00, '2026-03-15 16:30:00', 'UPI transaction cancelled');
-- 8. Insert data into beneficiaries
INSERT INTO beneficiaries
(customer_id, beneficiary_name, beneficiary_account_number, beneficiary_ifsc, bank_name)
VALUES
(1, 'Amit Sharma', 'EXT200001', 'SBIN0002001', 'State Bank'),
(2, 'Ravi Kumar', 'EXT200002', 'HDFC0002002', 'HDFC Bank'),
(3, 'Pooja Reddy', 'EXT200003', 'ICIC0002003', 'ICICI Bank'),
(4, 'Neha Patel', 'EXT200004', 'SBIN0002004', 'State Bank'),
(5, 'Suresh Rao', 'EXT200005', 'HDFC0002005', 'HDFC Bank'),
(6, 'Kavya Das', 'EXT200006', 'ICIC0002006', 'ICICI Bank'),
(7, 'Manoj Singh', 'EXT200007', 'SBIN0002007', 'State Bank'),
(8, 'Asha Nair', 'EXT200008', 'HDFC0002008', 'HDFC Bank'),
(9, 'Vijay Verma', 'EXT200009', 'ICIC0002009', 'ICICI Bank'),
(10, 'Ritu Joshi', 'EXT200010', 'SBIN0002010', 'State Bank');
-- 9. Insert data into cards
INSERT INTO cards
(account_id, card_number, card_type, expiry_date, card_status, issued_date)
VALUES
(1, 'CARD300001', 'Debit', '2029-12-31', 'Active', '2024-01-15'),
(2, 'CARD300002', 'Debit', '2029-12-31', 'Active', '2024-02-20'),
(3, 'CARD300003', 'Credit', '2028-11-30', 'Active', '2024-03-25'),
(4, 'CARD300004', 'Debit', '2029-10-31', 'Active', '2024-04-10'),
(5, 'CARD300005', 'Debit', '2029-09-30', 'Blocked', '2024-05-15'),
(6, 'CARD300006', 'Debit', '2029-08-31', 'Active', '2024-06-20'),
(7, 'CARD300007', 'Credit', '2028-07-31', 'Active', '2024-07-25'),
(8, 'CARD300008', 'Debit', '2028-06-30', 'Expired', '2023-06-10'),
(9, 'CARD300009', 'Debit', '2029-05-31', 'Active', '2024-09-20'),
(10, 'CARD300010', 'Credit', '2028-04-30', 'Active', '2024-10-30');
-- 10. Insert data into loans
INSERT INTO loans
(customer_id, branch_id, loan_type, loan_amount, interest_rate, start_date, end_date, loan_status)
VALUES
(1, 1, 'Personal Loan', 200000.00, 10.50, '2025-01-01', '2028-01-01', 'Approved'),
(2, 1, 'Education Loan', 500000.00, 8.50, '2025-02-01', '2030-02-01', 'Approved'),
(3, 2, 'Home Loan', 2500000.00, 8.25, '2025-03-01', '2040-03-01', 'Approved'),
(4, 3, 'Vehicle Loan', 600000.00, 9.00, '2025-04-01', '2030-04-01', 'Pending'),
(5, 3, 'Personal Loan', 150000.00, 11.00, '2025-05-01', '2028-05-01', 'Approved'),
(6, 8, 'Education Loan', 300000.00, 8.00, '2025-06-01', '2030-06-01', 'Pending'),
(7, 7, 'Home Loan', 3000000.00, 8.75, '2025-07-01', '2040-07-01', 'Approved'),
(8, 9, 'Vehicle Loan', 450000.00, 9.25, '2025-08-01', '2030-08-01', 'Rejected'),
(9, 6, 'Personal Loan', 100000.00, 12.00, '2025-09-01', '2028-09-01', 'Approved'),
(10, 10, 'Business Loan', 1000000.00, 10.00, '2025-10-01', '2030-10-01', 'Pending');

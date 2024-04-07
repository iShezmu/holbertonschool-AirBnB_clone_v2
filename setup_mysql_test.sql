#!/usr/bin/python3

-- Check if the database hbnb_dev_db already exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user hbnb_test with the password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant USAGE privilege to the user hbnb_test ON all databases and tables
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- Grant privileges to the user hbnb_test on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to the user hbnb_test on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Update PRIVILEGES
FLUSH PRIVILEGES;

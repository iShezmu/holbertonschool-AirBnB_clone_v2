#!/usr/bin/python3

-- Check if the database hbnb_dev_db already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user hbnb_dev with the password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant USAGE privilege to the user hbnb_dev ON all databases and tables
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant privileges to the user hbnb_dev on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege to the user hbnb_dev on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Update PRIVILEGES
FLUSH PRIVILEGES;

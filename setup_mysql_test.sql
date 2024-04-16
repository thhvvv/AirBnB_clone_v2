-- this script prepares MySQL server
-- craetes a project testing database with the name: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user named: hbnb_test with all privildges on hbnb_test_db
-- with the password: hbnb_test_pwd if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

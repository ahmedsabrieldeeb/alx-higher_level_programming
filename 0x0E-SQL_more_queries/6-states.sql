-- This script creates a new database and table
-- AUTO_INCREMENT constraint
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
	(id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
	 name VARCHAR(256));


-- This script creates new table on the server
-- UNIQUE, DEFAULT together
CREATE TABLE IF NOT EXISTS unique_id
	(id INT DEFAULT '1' UNIQUE, name VARCHAR(256));


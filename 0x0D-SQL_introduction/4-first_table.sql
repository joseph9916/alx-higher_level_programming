-- creates a table called first_table in the current database in your MySQL
-- first_table description:
--	id INT
--	name VARCHAR(256)
DROP TABLE IF EXISTS (SELECT *
	FROM INFORMATION_SCHEMA.TABLES
	WHERE TABLE_SCHEMA='TheSchema'
	AND TABLE_NAME='first_table');
CREATE TABLE first_table (
	id INT,
	name VARCHAR(256)
);

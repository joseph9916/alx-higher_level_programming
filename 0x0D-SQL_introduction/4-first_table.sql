-- creates a table called first_table in the current database in your MySQL
-- first_table description:
--	id INT
--	name VARCHAR(256)
DROP TABLE IF first_table EXISTS
CREATE TABLE first_table (
	id INT,
	name VARCHAR(256)
);

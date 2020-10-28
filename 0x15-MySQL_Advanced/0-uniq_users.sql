-- creates a table users following requirements
CREATE TABLE IF NOT EXISTS unique_id(
       id INT UNIQUE NOT NULL AUTO_INCREMENT,
       EMAIL CHAR(255) UNIQUE NOT NULL,
       name CHAR(255)
       PRIMARY KEY (ID));

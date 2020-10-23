-- creates the MySQL server user user_0d_1
-- creates user if it doesn't already exists, sets psw
-- grants all privilegs to user
    CREATE DATABASE IF NOT EXISTS hbtn_0d_0;
    CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
     GRANT SELECT
        ON hbtn_0d_0.*
        TO user_0d_2@localhost;
 

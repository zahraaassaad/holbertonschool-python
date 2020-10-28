-- Creates trigger to reset the attribute valid_email 
-- Only when the email has been changed

DELIMITER $$
CREATE TRIGGER 
validate_email
BEFORE UPDATE 
ON users FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;

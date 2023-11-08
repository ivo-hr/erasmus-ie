-- Trigger to check if a supplier with matching information already exists
CREATE OR REPLACE FUNCTION check_duplicate_supplier_update()
RETURNS TRIGGER AS
$$
BEGIN
 -- Check if another supplier exists with the updated information
    IF EXISTS (
        SELECT 1
        FROM supplier
        -- If the id is different, check if the name, address, or phone number matches
        WHERE supplier_id <> NEW.supplier_id
        AND (supplier_name = NEW.supplier_name
        OR supplier_address = NEW.supplier_address
        OR supplier_phone = NEW.supplier_phone)
    ) THEN
    -- If a supplier with any matching information exists, raise an exception
        RAISE EXCEPTION 'Another supplier with the same information already exists';
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

-- Create the trigger to check for duplicate suppliers before updating a supplier
CREATE TRIGGER before_update_supplier
BEFORE UPDATE ON supplier
FOR EACH ROW
EXECUTE FUNCTION check_duplicate_supplier_update();

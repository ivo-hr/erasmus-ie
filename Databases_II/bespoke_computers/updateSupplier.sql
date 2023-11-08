--Function to edit supplier information
CREATE OR REPLACE FUNCTION update_supplier(
    supplier_id INTEGER,
    new_supplier_name VARCHAR(255),
    new_supplier_address VARCHAR(255),
    new_supplier_phone VARCHAR(255)
) RETURNS VOID AS
$$
BEGIN
    -- Update the supplier's information.
    UPDATE bespoke_computers.supplier
    SET supplier_name = new_supplier_name,
        supplier_address = new_supplier_address,
        supplier_phone = new_supplier_phone
    WHERE bespoke_computers.supplier.supplier_id = update_supplier.supplier_id;
END;
$$
LANGUAGE plpgsql;

-- We do not need to check for duplicate suppliers here, because the trigger will do that for us.




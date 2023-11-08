import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password",
    "host": "your_host",
    "port": "your_port",
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)

    # Create a cursor
    cursor = connection.cursor()

    # Prompt the user for supplier information
    supplier_id = int(input("Enter the supplier ID: "))
    new_supplier_name = input("Enter the new supplier name: ")
    new_supplier_address = input("Enter the new supplier address: ")
    new_supplier_phone = input("Enter the new supplier phone: ")

    # SQL statement to call the update_supplier function
    update_supplier_sql = """
    SELECT update_supplier(
        %s,
        %s,
        %s,
        %s
    );
    """

    # Execute the update_supplier function
    cursor.execute(update_supplier_sql, (supplier_id, new_supplier_name, new_supplier_address, new_supplier_phone))

    # Commit the transaction
    connection.commit()

    print("Supplier information updated successfully.")

except (psycopg2.Error, Exception) as error:
    print("Error: {}".format(error))

finally:
    if connection:
        cursor.close()
        connection.close()

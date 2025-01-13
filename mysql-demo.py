import mysql.connector
from mysql.connector import Error
import json
from utilities.configurations import *

# Initialize variables
conn = None
cursor = None

try:
    # Connect to the MySQL server
    conn = connect_database()

    if conn.is_connected():
        # Get a cursor
        cursor = conn.cursor()

        # Execute the query to fetch data from the 'books' table
        cursor.execute("SELECT * FROM books")

        # Fetch and print the first row with remaining ...
        first_row = cursor.fetchone()
        print(f"\nBook data first row: {first_row}, type {type(first_row)}")

        # Get column names from cursor.description
        columns = [desc[0] for desc in cursor.description]
        print(f"Book columns: {columns}")

        # Convert the first row to JSON format
        if first_row is not None:
            first_row_dict = dict(zip(columns, first_row))
            first_row_json = json.dumps(first_row_dict, indent=2)
            print("\nFirst row in JSON format:")
            print(first_row_json)
        else:
            print("\nNo data found in the 'books' table.")

        remaining_rows = cursor.fetchall()

        # Restart cursor for the 'books' table
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        print("\nBooks data (restarted cursor):")
        for row in rows:
            print(row)

        # Execute the query to fetch data from the 'customerinfo' table
        cursor.execute("SELECT * FROM customerinfo")

        # Fetch all results
        rows = cursor.fetchall()
        print("\nCustomer info data:")
        for row in rows:
            print(row)

        # Update record 'Jmeter'
        print("\nUpdate Jmeter:")
        query = "update customerInfo set Location = %s where CourseName = %s"
        data = ('UK', 'Jmeter')
        cursor.execute(query, data)
        conn.commit()
        print("Jmeter record updated successfully.")

        # Insert WebService
        print("\nInsert WebService:")
        query = "INSERT INTO CustomerInfo values(%s,CURRENT_DATE(),%s,%s)"
        data = ('WebServices',21,'Asia')
        cursor.execute(query, data)
        conn.commit()
        print("WebServices record inserted successfully.")

        # Delete WebService
        print("\nDelete WebService:")
        safe_update = "SET sql_safe_updates = 0"
        cursor.execute(safe_update)

        delete_query = "DELETE FROM customerInfo WHERE CourseName = %s"
        delete_data = ('WebServices',)
        cursor.execute(delete_query, delete_data)
        conn.commit()
        print("WebServices record deleted successfully.")

except Error as e:
    print(f"Error occurred: {e}")

finally:
    # Ensure the cursor is closed
    print('\n')
    if cursor is not None:
        cursor.close()
        print("Cursor closed.")

    # Ensure the connection is closed
    if conn is not None and conn.is_connected():
        conn.close()
        print("MySQL connection closed.")

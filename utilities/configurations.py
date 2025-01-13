import configparser
import mysql.connector
from mysql.connector import Error

def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

def connect_database():
    try:
        # Fetch database configuration from properties file
        db_config = {
            'host': get_config()['SQL']['host'],
            'port': int(get_config()['SQL']['port']),  # Ensure port is an integer
            'database': get_config()['SQL']['database'],
            'user': get_config()['SQL']['user'],
            'password': get_config()['SQL']['password'],
        }

        # Connect to the MySQL server
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print(f"Connected to the database {db_config['database']} on {db_config['host']}:{db_config['port']}")

        return connection

    except Error as e:
        print(f"Error while connecting to database: {e}")
        return None

def get_query(query):
    try:
        # Connect to the MySQL server
        conn = connect_database()
        if conn and conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            first_row = cursor.fetchone()
            conn.close()
            return first_row
        else:
            print("Connection to database failed.")
            return None

    except Error as e:
        print(f"Error while executing query: {e}")
        return None

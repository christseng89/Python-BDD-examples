import configparser
import mysql.connector
from mysql.connector import Error

def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

db_config = {
    'host': get_config()['SQL']['host'],
    'port': int(get_config()['SQL']['port']),  # Ensure port is an integer
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
}

def connect_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print(f"Connected to the database {db_config['database']} on {db_config['host']}:{db_config['port']}")

        return connection

    except Error as e:
        print(f"Error while connecting to database: {e}")
        return None

import json

import mysql.connector
from mysql.connector import Error

from lib.src.core.factories.mysql.constants.mysql_constants import MySqlConstants


class MySqlFactory:
    def __init__(self):
        self.config_path = MySqlConstants.config_path
        self.connection = None

    def connect(self):
        try:
            with open(self.config_path, "r") as config_file:
                config = json.load(config_file)

            self.connection = mysql.connector.connect(
                host=config["host"],
                database=config["database"],
                user=config["user"],
                password=config["password"],
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def get_cursor(self):
        """Returns a cursor object using the current connection."""
        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)
        else:
            print("Connection is not established. Call connect() first.")
            return None

    def close_connection(self):
        """Closes the connection to the database."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed.")

    def commit(self):
        """Commits the current transaction."""
        if self.connection and self.connection.is_connected():
            self.connection.commit()
        else:
            print("Connection is not established. Call connect() first.")

import pyodbc
import configparser

class Database:

    def __init__(self):
        self.connection_string = self.get_connection_string()

    def check_connection(self):
        try:
            connection = pyodbc.connect(self.connection_string)
            connection.close()
            return "Connected"
        except pyodbc.Error as e:
            return f"Error connecting to the database: {e}"

    def get_connection_string(self):
        config = configparser.ConfigParser()
        config.read('conf/configuration.ini')
        server = config.get('dbconnection', 'server')
        database = config.get('dbconnection', 'database')
        username = config.get('dbconnection', 'username')
        password = config.get('dbconnection', 'password')
        return (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )
    
    def execute(self, query, values=None):
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def execute_with_data(self, query, values):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            if values:
                data = cursor.execute(query, values)
                result = data.fetchall()
                connection.commit()
            else:
                data = cursor.execute(query)
                result = data.fetchall()
                connection.commit()
            return result
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()
            connection.close()


    def create_database(self):
        pass

    def drop_database(self):
        pass


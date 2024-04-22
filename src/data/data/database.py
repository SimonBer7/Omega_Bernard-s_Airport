"""
Class: Database

This class provides methods for interacting with a SQL Server database using pyodbc. It includes methods for executing queries, checking the connection status, creating and dropping database tables, and retrieving connection strings from a configuration file.

Attributes:
- log_writer (Log_writer): An instance of Log_writer class for logging database-related activities.
- connection_string (str): The connection string used to connect to the SQL Server database.

Methods:
- __init__(self): Initializes a new Database object.
- check_connection(self): Checks the connection status with the database.
- get_connection_string(self): Retrieves the connection string from the configuration file.
- execute(self, query, values=None): Executes a SQL query without returning any data.
- execute_with_data(self, query, values): Executes a SQL query and returns the result set.
- execute_for_arg(self, query, values): Executes a SQL query and returns a single value.
- create_database(self): Creates the database schema with predefined tables.
- drop_database(self): Drops all tables in the database.

"""

import pyodbc
import configparser
from src.logic.log_writter import Log_writter


class Database:
    """
    A class for interacting with a SQL Server database using pyodbc.

    Attributes:
    - log_writer (Log_writer): An instance of Log_writer class for logging database-related activities.
    - connection_string (str): The connection string used to connect to the SQL Server database.
    """

    def __init__(self):
        """
        Initializes a new Database object.
        """
        self.log_writer = Log_writter()
        self.connection_string = self.get_connection_string()

    def check_connection(self):
        """
        Checks the connection status with the database.

        Returns:
        - str: A message indicating the connection status.
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            connection.close()
            return "Connected"
        except pyodbc.Error as e:
            self.log_writer.write_to_log(f"Error connecting to the database: {e}")

    def get_connection_string(self):
        """
        Retrieves the connection string from the configuration file.

        Returns:
        - str: The connection string.
        """
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
        """
        Executes a SQL query without returning any data.

        Parameters:
        - query (str): The SQL query to execute.
        - values (tuple): Optional parameter containing parameterized values for the query.
        """
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
        """
        Executes a SQL query and returns the result set.

        Parameters:
        - query (str): The SQL query to execute.
        - values (tuple): Parameterized values for the query.

        Returns:
        - list: The result set returned by the query.
        """
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
            self.log_writer.write_to_log(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def execute_for_agr(self, query, values):
        """
        Executes a SQL query and returns a single value.

        Parameters:
        - query (str): The SQL query to execute.
        - values (tuple): Parameterized values for the query.

        Returns:
        - any: The single value returned by the query.
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            if values:
                data = cursor.execute(query, values)
                result = data.fetchone()[0]
            else:
                data = cursor.execute(query)
                result = data.fetchone()[0]
            connection.commit()
            return result
        except Exception as e:
            self.log_writer.write_to_log(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def create_database(self):
        """
        Creates the database schema with predefined tables.
        """
        sql_statement = """
        BEGIN TRANSACTION;
        create table passenger(
            id int primary key identity(1,1),
            name varchar(50) not null,
            email varchar(150) not null check(email like '%@%'),
            password varchar(255) not null,
            phone_num varchar(15) not null,
            pin varchar(11) not null check(pin like '%/%') unique
        );

        create table pilot(
            id int primary key identity(1,1),
            name varchar(50) not null,
            age int not null check(age > 28),
            email varchar(150) not null check(email like '%@%'),
            phone_num varchar(15) not null
        );

        create table plane(
            id int primary key identity(1,1),
            name varchar(100) not null,
            type varchar(100) not null check(type in ('private', 'public')), 
            capacity int not null check(capacity > 0),
            active char(1) not null
        );

        create table destination(
            id int primary key identity(1,1),
            country varchar(50) not null,
            capital varchar(50) not null,
            avg_temp float not null
        );

        create table flight(
            id int primary key identity(1,1),
            fly_number int not null check(fly_number > 0) unique,
            destination_id int foreign key references destination(id),
            plane_id int foreign key references plane(id),
            pilot_id int foreign key references pilot(id),
            date_leaving date not null,
            date_arriving date not null,
            price int not null check(price > 0)
        );

        create table reservation(
            id int primary key identity(1,1),
            pin int not null check(pin > 0) unique,
            passenger_id int foreign key references passenger(id),
            flight_id int foreign key references flight(id),
            date datetime not null,
            price int not null check(price > 0)
        );
        COMMIT	
        """
        self.execute(sql_statement)
        self.log_writer.write_to_log("Database was created.")

    def drop_database(self):
        """
        Drops all tables in the database.
        """
        sql_statements = """drop table reservation;
                                    drop table flight;
                                    drop table destination;
                                    drop table plane;
                                    drop table pilot;
                                    drop table passenger;"""
        self.execute(sql_statements)
        self.log_writer.write_to_log("Database was deleted.")

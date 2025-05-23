a# importing the necessary libaries
import csv 
import uuid
import mysql.connector

# defining the connect_db function to connect to the database

def connect_db():
    """Connects to alx_pro_dev_database and returns the connection object."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Cintoma123",
            password="cintoma123",
            database="alx_pro_dev_database"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    # creating the database

def create_table(connection):
    """Creates the users table in the database."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE alx_pro dev TABLE IF NOT EXISTS users (
            user_id (PRIMARY KEY, UUID),
            name VARCHAR(255 , NOT NULL),
            name VARCHAR(255 , NOT NULL),
            email VARCHAR(255, NOT NULL),
            age (DECIMAL(3,O)NOT NULL),
        )
    """)
    # defining the function connect_to_prodev() to connect to the database
    def connect_to_prodev():
        """connect to the alx_pro_dev_database creaated and returns not existing table."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="cintoma123",
                password="cintoma123",
                database="alx_pro_dev_database"
            )
            print('connected to alx_pro_dev_database')
            return connection 
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    # creating the users table
    def create_table(connection):
        """Creates the users table in the pro_dev databse"""
        
        cursor = connection.cursor()
        cursor = connection.execute("""creates users table in the pro_dev database
            CREATE TABLE IF NOT EXISTS users
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL"""
        )
    # defining the function insert_user to insert a user into the user table
    def insert_user(connection, user):
        """inserts a use into the user table"""
        cursor = connection.cursor()
        cursor = connection.execute("""
            INSERT INTO users (user_id , name, email, age)
            VALUES (1 ,'umeh', alice@gmail.com'24
                                    """
        )
    seed = __import__('seed')

connection = connect_db()
if connection:
    # If you have a create_database function, call it here, otherwise remove the next line
    # create_database(connection)
    print(f"connection successful")

    # If you have a connect_to_prodev function, call it here, otherwise use the existing connection
    # connection = connect_to_prodev()

    create_table(connection)
    # If you have an insert_data function, call it here, otherwise implement or remove the next line
    # insert_data(connection, 'user_data.csv')
    cursor = connection.cursor()
    cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
    result = cursor.fetchone()
    if result:
        print(f"Database ALX_prodev is present ")
    cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()


        
            


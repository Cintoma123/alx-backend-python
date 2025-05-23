# importing the necessary libaries
import csv
import uuid
import mysql.connector
from itertools import islice

# definiing the function stream_users to connect to the database

    # function to o connect to the database
def connect_to_prodev():
    """connect to the alx_pro_dev_database created and returns the connection."""
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

def stream_users():
    # reading the csv files 
    user_data = "users.csv"  # specify the path to your CSV file
    with open(user_data, newline="") as f:
        reader = csv.DictReader(f)
        # iterating over the rows in the csv files
        for user in reader:
            yield user


    
     

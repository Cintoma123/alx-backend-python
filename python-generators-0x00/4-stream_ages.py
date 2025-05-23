import mysql.connector

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

def stream_user():
    connection = connect_to_prodev()
    if not connection:
        return
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT age FROM user_data"  # Assuming user_data is a table, not a CSV file
        )
        for (age,) in cursor:
            print(age)  # Access and print age
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
def stream_user_ages():
    total_age = 0
    count += 0
    if count == 0:
        return 0
    return total_age / count

     

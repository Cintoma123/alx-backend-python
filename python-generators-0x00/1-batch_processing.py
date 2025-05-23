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
    
def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    batch_size = 200 # Define your desired batch size
    if not connection:
        return
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM user_data"  # Assuming user_data is a table, not a CSV file
        )
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except mysql.connector.Error as err:
        print(f"Error during batch processing: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    
def batch_processing(batch_size):
    """To batch process users in batches of given size"""
    try:
        for batch in stream_users_in_batches(batch_size):
            filtered_users_inbatch = [user for user in batch if user[3] > 25]
            yield filtered_users_inbatch
    except Exception as e:
        print(f"Error in batch_processing: {e}")

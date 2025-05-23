import sqlite3
import logging
from functools import wraps
from typing import Callable , Any , Tuple , List 
from datetime import datetime

logg_er = logging.getLogger('transaction_db')
logg_er.setLevel(logging.INFO)
file_handler = logging.FileHandler('transaction.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(message)s'))

def db_connection(db_name : str):
   conn = None 
   try:
      conn = sqlite3.connect(db_name, check_same_thread = True)
      logg_er.info(f'opened connected to {db_name}')
      yield conn 
   except sqlite3.Error as e:
      logg_er.error(f'connection error{e}')
      raise
   finally:
      if conn:
         conn.close()
         logg_er.info(f'closed connection to {db_name}')

def with_db_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with db_connection ('users.db') as conn:
            return func(*args , **kwargs)
        return wrapper

@with_db_connection 
def get_user_by_id(connection, user_id): 
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    result = cursor.fetchone()
    cursor.close()
    return result

#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)

import logging 
def transactIon(func):
    def wrapper(con, *args , **kwargs):
           try:
            con.commit()
            result = func(*args, **kwargs)
            logging.info('transaction sucessfully')
            return result
           except Exception as e:
               logging.info(f'Tranasaction rolled back : {e}')
               raise 
    return wrapper

def update_user_email(conn, user_id, new_email): 
cursor = connection.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
               

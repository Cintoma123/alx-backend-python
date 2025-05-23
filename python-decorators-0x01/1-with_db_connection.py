import sqlite3
import logging
from functools import wraps
from typing import Callable , Any , Tuple , List 
from datetime import datetime

logg_er = logging.getLogger('db.connection')
logg_er.setLevel(logging.INFO)
file_handler = logging.FileHandler('connection.log')
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

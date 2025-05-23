import sqlite3
import logging
from functools import wraps
from typing import Callable , Any , Tuple , List 
from datetime import datetime

logg_er = logging.getLogger('db_retry')
logg_er.setLevel(logging.INFO)
file_handler = logging.FileHandler('retry.log')
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

def re_try (retries = 2 ,delay = 2 ):
  def decorator_retry(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
       tries = 0 
       while tries < retries:
           try:
             return func(*args, **kwargs)
           except Exception as e:
             tries +=1
             if tries == retries:
                raise e 
                timee.sleep(delay_second)
             return wrapper
     
def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)




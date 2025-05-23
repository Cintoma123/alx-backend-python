import sqlite3
import logging
from functools import wraps
from typing import Callable , Any , Tuple , List 
from datetime import datetime

logg_er = logging.getLogger('db_cache')
logg_er.setLevel(logging.INFO)
file_handler = logging.FileHandler('cache.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(message)s'))

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
    
def cache_query(func):
        query_cache = {}
        def wrapper(*args):
            if args in query_cache:
                return query_cache[args]
            else:
                result = func(*args)
                query_cache[args] = result 
                return result
        return wrapper
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")



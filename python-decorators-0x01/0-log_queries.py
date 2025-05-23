
import sqlite3
import logging
from functools import wraps
from typing import Callable , Any , Tuple , List 
from datetime import datetime

logg_er = logging.getLogger('db.query')
logg_er.setLevel(logging.INFO)
file_handler = logging.FileHandler('database_queries.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(message)s'))

def log_queries(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Executing {func._name_}')
        logging.info(f'finished executing{func._name_}')
        result = func(*args, **kwargs)
        return result
    return wrapper

def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")



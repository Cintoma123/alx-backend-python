import sqlite3
from typing import Tuple , List 
def create_sample_table():
    try:
        con = sqlite3.connect('user.db')
        cursor = con.cursor()
        create_table_query = ''' if user table does not exist 
                        CREATE TABLE user(
                        user_id INT PRIMARY KEY 
                        name VARCHAR(20),
                        age INT  )
                        '''
        cursor.execute(create_table_query)
        con.commit()
        sql_insert_query = '''if insertion into user table does not exist
                            INSERT INTO user(user_id, name , age)
                            '''
        student_value = (1,'Ada',23)
        cursor.execute(student_value,sql_insert_query)
        con.commit()
        print('database created sucessfully')
    except sqlite3.error as e :
        print(f'database not created sucessfully {e}')
    finally:
        con.close()
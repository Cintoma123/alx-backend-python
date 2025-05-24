import sqlite3
import logging



class ExecuteQuery:
    def __init__(self, db_name : str, query:str):
        self.db_name = db_name
        self.conn = None
    def __enter__(self):
        try:
            self.connection = self.sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.error as e :
            print('database not connected sucessfully {e}')
            raise

        return self 
    def __exist__(self , exc_type ,exc_val , exc_tb):
        if exc_val is not None:
            print(f'error occured:{exc_val}')

    def fetch_all_data():
            with ExecuteQuery('users.db') as connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute('''
                                   SELECT * FROM users WHERE age > ?,
                                   ''',(25,))
                    connection.commit()
                except sqlite3 as e:
                    print(f'database not sucessfully selected{e}')
                finally:
                    connection.close()

    if __name__ == '__main__':
                result = fetch_all_data()
                print('users in database')
                for users in result:
                 print(users)



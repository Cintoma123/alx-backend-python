import sqlite3


class DatabaseConnection:
    def __init__(self, db_name : str):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.connection = self.sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self 
    
    def __exit__(self , exc_type ,exc_val , exc_tb):
        if exc_val is not None:
            print(f'error occured:{exc_val}')

    
    def create_table():
       result = 'users.db'
       with DatabaseConnection('users.db') as connection:
        try:
               cursor = connection.cursor() 
               cursor.execute('''CREATE TABLE IF NOT EXIST users
                              user_id INT PRIMARY KEY,
                              first_name VARCHAR(100),
                              last_name VARCHAR(100)
                              age INT
                              ''')
               connection.commit()
        except sqlite3.error as e :
               print(f'database not sucessfully created {e}')
        finally:
            connection.close()
            return result

        def insert_table():
            with DatabaseConnection('user.db') as connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(''' Insert table if it does not exist
                                   INSERT INTO users (user_id, first_name , last_name , age )
                                   VALUES(1,'ada','obi',40)
                                   ''')
                    connection.commit()
                except sqlite3 as e:
                    print(f'database not sucessfully creatd {e}')
                finally:
                    connection.close()

        def fetch_all_data():
            with DatabaseConnection('user.db') as connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute('''
                                   SELECT * FROM users''')
                                   
                    connection.commit()
                except sqlite3 as e:
                    print(f'database not sucessfully selected{e}')
                finally:
                    connection.close()
        if __name__ == '__main__':
            result  = fetch_all_data()
            print('users in database')
            for users in result:
                print(result)




            







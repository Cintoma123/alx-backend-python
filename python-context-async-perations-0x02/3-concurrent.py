import asyncio
import logging
import aiosqlite

logging.basicConfig(level=logging.INFO)

async def create_database(db_name: str = 'users.db'):
    try:
        async with aiosqlite.connect(db_name) as connection:
            await connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            ''')
            await connection.commit()
            await connection.execute('''
                INSERT INTO users (name, age)
                VALUES ('ada', 30)
            ''')
            await connection.commit()
            logging.info(f'Database {db_name} created and table users initialized.')
    except Exception as e:
        logging.error(f"Error creating database: {e}")

async def async_fetch_users(db_name: str):
    result = []
    try:
        async with aiosqlite.connect(db_name) as connection:
            cursor = await connection.execute('SELECT * FROM users')
            result = await cursor.fetchall()
            logging.info('fetching all users')
    except Exception as e:
        logging.error(f'an error occurred as {e}')
    return result

async def async_fetch_older_users(db_name: str, age: int = 40):
    result = []
    try:
        async with aiosqlite.connect(db_name) as connection:
            cursor = await connection.execute('SELECT * FROM users WHERE age > ?', (age,))
            result = await cursor.fetchall()
            logging.info('fetching older users')
    except Exception as e:
        logging.error(f'an error occurred as {e}')
    return result

async def fetch_concurrently():
    result = await asyncio.gather(
        async_fetch_users('users.db'),
        async_fetch_older_users('users.db', 40)
    )
    return result

if __name__ == '__main__':
    asyncio.run(create_database())
    try:
        all_data, data_gathering = asyncio.run(fetch_concurrently())
        for user in all_data:
            print(user)
        for user in data_gathering:
            print(user)
    except aiosqlite.Error as e:
        print(f'error occurred in {e}')

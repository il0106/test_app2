from base64 import b64encode
from secrets import token_bytes
import psycopg2
import pandas as pd

# Данные для подключения
db_host = 'localhost'  # Или IP-адрес хоста Docker
db_port = '5433'       # Порт, который используется на вашем Docker хосте
db_name = 'db_'
db_user = 'user_'
db_password = 'password_'

# Попытка подключения
try:
    connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port, 
        options="-c client_encoding=UTF8"
    )

    cursor = connection.cursor()

    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Вы подключены к - {db_version}\n")

    
    q = """
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public';
    """

    print(pd.read_sql_query(q, connection))

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Ошибка подключения к базе данных: {error}")

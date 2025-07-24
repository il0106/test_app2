import sqlite3
import pandas as pd


conn = sqlite3.connect('volume/test.db') 
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
    
print("Таблицы в базе данных:")
print(tables)

def delete_all_users():
    """Удаляет все строки из таблицы users"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user")
    conn.commit()
    print(f"Удалено {cursor.rowcount} строк из таблицы user")
    cursor.close()

# Вызов функции для удаления всех пользователей
delete_all_users()

print(pd.read_sql_query("select * FROM user",conn))

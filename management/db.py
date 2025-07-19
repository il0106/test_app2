import sqlite3
import pandas as pd


conn = sqlite3.connect('volume/test.db') 
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
    
print("Таблицы в базе данных:")
print(tables)


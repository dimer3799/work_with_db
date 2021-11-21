import psycopg2
from config import *

con = ""

try:
    # Connect database
    con = psycopg2.connect(host=host, user=user, password=password, database=db_name)
    # cursor = con.cursor()
    with con.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")
except Exception as _ex:
    print(f"[ERROR] Произошла ошибка: {_ex}")
finally:
    if con:
        con.close()
        print("[INFO] Database connection close")

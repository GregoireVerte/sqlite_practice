
import sqlite3
from sqlite3 import Error




def create_connection(dbtask_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(dbtask_file)
       print(f"Connected to {dbtask_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()




def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

if __name__ == '__main__':
   create_connection(r"dbtask_file.db")
   create_connection_in_memory()




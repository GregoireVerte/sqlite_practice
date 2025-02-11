

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Tworzy połączenie z bazą SQLite """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None

def execute_sql(conn, sql):
    """ Wykonuje zapytanie SQL """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_raw_material_sql = """
    CREATE TABLE IF NOT EXISTS raw_material (
       id integer PRIMARY KEY,
       name text NOT NULL,
       application text,
       exp_date text
    );
    """

    create_lab_test_sql = """
    CREATE TABLE IF NOT EXISTS lab_test (
       id integer PRIMARY KEY,
       mat_id integer NOT NULL,
       name VARCHAR(250) NOT NULL,
       description TEXT,
       status VARCHAR(15) NOT NULL,
       start_date text NOT NULL,
       end_date text NOT NULL,
       FOREIGN KEY (mat_id) REFERENCES raw_material (id)
    );
    """

    db_file = "dbtask_file.db"

    # Używamy context managera, połączenie do bazy danych zamknie się automatycznie, gdy kod wyjdzie z bloku with
    with create_connection(db_file) as conn:
        if conn is not None:
            execute_sql(conn, create_lab_test_sql)
            execute_sql(conn, create_raw_material_sql)





import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


conn = create_connection("dbtask_file.db")


def select_lab_test_by_status(conn, status):
    """
    Query lab_test by status
    :param conn: the Connection object
    :param status:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM lab_test WHERE status=?", (status,))

    rows = cur.fetchall()
    return rows


def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the Connection object
    :param table: table name
    :return: list of rows
    """
    cur = conn.cursor() # Tworzy kursor do wykonywania zapytań SQL
    cur.execute(f"SELECT * FROM {table}") # Wykonuje zapytanie SQL: pobiera wszystko z tabeli
    rows = cur.fetchall() # Pobiera wszystkie wyniki zapytania jako listę krotek

    return rows # Zwraca listę wierszy z tabeli


def select_where(conn, table, **query):
    """
    Query rows from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return: list of rows
    """
    cur = conn.cursor() # Tworzy kursor do wykonywania zapytań SQL

    qs = [] # Lista przechowująca fragmenty zapytania SQL
    values = () # Krotka przechowująca wartości warunków

    # Tworzenie warunków WHERE na podstawie słownika query
    for k, v in query.items(): # Iteracja po parach klucz-wartość w slowniku query
        qs.append(f"{k}=?") # Tworzy warunek np. "nazwa=?"
        values += (v,) # Dodaje wartość do krotki values
    q = " AND ".join(qs) # Łączy warunki z operatorem AND, np. "nazwa=? AND status=?"
    # Wykonuje zapytanie SQL z warunkami
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall() # Pobiera wszystkie dopasowane wiersze
    return rows # Zwraca listę wyników


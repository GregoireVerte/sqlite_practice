## Delete

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file) # Nawiązuje połączenie z bazą danych
    except Error as e:
        print(e) ## Jeśli wystąpi błąd, wyświetlamy go na ekranie

    return conn  ## Zwraca obiekt połączenia lub None w przypadku błędu



def delete_where(conn, table, **kwargs):
    """
    Delete from table where attributes from kwargs match
    :param conn:  Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values (warunki usuwania)
    :return:
    """
    qs = [] # Lista przechowująca fragmenty zapytania SQL
    values = tuple() # Krotka przechowująca wartości warunków
    for k, v in kwargs.items(): # Iteracja po parach klucz-wartość w slowniku powstalym z kwargs (parametrow nazwanych)
        qs.append(f"{k}=?") # Tworzy warunek np. "nazwa=?"
        values += (v,) # Dodaje wartość do krotki values
    q = " AND ".join(qs) # Łączy warunki, np. "nazwa=? AND status=?"

    sql = f'DELETE FROM {table} WHERE {q}' # Tworzymy dynamiczne warunki WHERE np.: DELETE FROM lab_test WHERE id=? AND status=?
    cur = conn.cursor() # Tworzymy kursor – obiekt do operacji na bazie danych
    cur.execute(sql, values) # Wykonujemy zapytanie SQL z podanymi wartościami
    conn.commit() #zatwierdza zmiany w bazie danych
    print("DELETED FOREVER!")

def delete_all(conn, table):
    """
    Delete all rows from table
    :param conn: Connection to the SQLite database
    :param table: table name
    :return:
    """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("DELETED FOREVER!")

if __name__ == "__main__":
    conn = create_connection("dbtask_file.db") # Łączymy się z bazą/plikiem
    delete_where(conn, "lab_test", id=2)
    delete_all(conn, "raw_material")

















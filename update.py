## UPDATE

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

def update(conn, table, id, **kwargs):
    """
    update for example status, start_date, and end_date of a lab_test
    :param conn: obiekt połączenia z bazą danych
    :param table: table name
    :param id: row id - identyfikator wiersza do aktualizacji
    :param kwargs: wartości do aktualizacji w formie klucz=wartość
    :return:
    """
    parameters = [f"{k} = ?" for k in kwargs] ## Dla każdej pary klucz=wartość w kwargs tworzymy ciąg/listę nazwa_kolumny = ? np.: ['status = ?', 'end_date = ?']
    parameters = ", ".join(parameters)  ## Łączymy elementy listy w pojedynczy string - Teraz parameters to: 'status = ?, end_date = ?'
    values = tuple(v for v in kwargs.values())  ## Tworzymy krotkę wartości - Pobieramy wartości kwargs.values() i dodajemy id na końcu:
    values += (id, )

### Tworzymy dynamiczne zapytanie SQL (np.: SET status = ?, end_date = ?)
    sql = f""" UPDATE {table}
            SET {parameters}
            WHERE id = ?"""
    try:
        cur = conn.cursor() #Tworzymy kursor do obsługi bazy danych
        cur.execute(sql, values) #Wykonujemy zapytanie SQL z dynamicznymi wartościami
        conn.commit() ## Zatwierdzamy zmiany w bazie danych
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

if __name__ == "__main__":
    conn = create_connection("dbtask_file.db") # Nawiązujemy połączenie z bazą/plikiem
    update(conn, "lab_test", 1, status="ended")
    update(conn, "raw_material", 2, exp_date="2030-01-20 00:00:00")
    conn.close() #Zamykamy połączenie z bazą danych




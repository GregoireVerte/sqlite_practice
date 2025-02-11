
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

def add_raw_material(conn, raw_material):
    """
    Create a new raw material ant put it into the raw_material table
    :param conn:
    :param raw_material:
    :return: raw_material id
    """
    sql = """INSERT INTO raw_material(name, application, exp_date)
             VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, raw_material)
    conn.commit()
    return cur.lastrowid

def add_lab_test(conn, lab_test):
    """
    Create a new laboratory test into the lab_test table
    :param conn:
    :param lab_test:
    :return: lab_test id
    """
    sql = """INSERT INTO lab_test(mat_id, name, description, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, lab_test)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    raw_material = ("Surowiec 1", "Zastosowanie 1", "2026-01-20 00:00:00")

    conn = create_connection("dbtask_file.db")
    mat_id = add_raw_material(conn, raw_material)

    lab_test = (
        mat_id,
        "Badanie 1",
        "Opis 1",
        "started",
        "2024-06-11 12:00:00",
        "2025-01-11 15:00:00"
    )

    lab_test_id = add_lab_test(conn, lab_test)

    print(mat_id, lab_test_id)

    raw_material_sec = ("Surowiec 2", "Zastosowanie 2", "2027-01-20 00:00:00")

    mat_id_sec = add_raw_material(conn, raw_material_sec)

    lab_test_sec = (
        mat_id_sec,
        "Badanie 2",
        "Opis 2",
        "ended",
        "2025-06-11 12:00:00",
        "2025-12-30 15:00:00"
    )

    lab_test_id_sec = add_lab_test(conn, lab_test_sec)

    print(mat_id_sec, lab_test_id_sec)


    conn.commit()




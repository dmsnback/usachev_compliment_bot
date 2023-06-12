import sqlite3
from random import randint


def number_rows_database():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''
        SELECT COUNT(*)
        FROM compliments;
    ''')

    for result in cur:
        return result[0]

    con.close()


def compliment():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'''
        SELECT compliment
        FROM compliments
        WHERE id == {randint(1, number_rows_database())};
    ''')

    for result in cur:
        return result

    con.close()

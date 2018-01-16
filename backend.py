#!/usr/bin/env python3
"""

Functions for managing Postgres database.


"""


import psycopg2


def create_table():
    '''Create table if it does not exist.'''
    conn = psycopg2.connect("dbname='your_db_name' user='your_user_name' password='your_secret_password' port='postgres_port' host='your_db_server'")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS your_db_name (
            id SERIAL PRIMARY KEY, 
            title TEXT, 
            alt_title TEXT, 
            duration INTEGER, 
            year INTEGER)""")
    conn.commit()
    conn.close()


def insert(title, alt_title, duration, year):
    '''Add an new entry into database.'''
    conn = psycopg2.connect("dbname='your_db_name'")
    cur = conn.cursor()
    cur.execute("INSERT INTO your_db_name (title, alt_title, duration, year) VALUES (%s, %s, %s, %s)", (title, alt_title, duration, year))
    conn.commit()
    conn.close()


def view_all():
    '''Query entire database.'''
    conn = psycopg2.connect("dbname='your_db_name'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_db_name")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title, alt_title, duration, year):
    '''Search the database for entries.'''
    conn = psycopg2.connect("dbname='your_db_name'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_db_name WHERE title=? OR alt_title=? OR duration=? OR year=?", (title, alt_title, duration, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    '''Delete items from database.'''
    conn = psycopg2.connect("dbname='your_db_name'")
    cur = conn.cursor()
    cur.execute("DELETE FROM your_db_name WHERE id=%s", (id,))
    conn.commit()
    conn.close()


def update(id, title, alt_title, duration, year):
    '''Update database records.'''
    conn = psycopg2.connect("dbname='your_db_name'")
    cur = conn.cursor()
    print(id, title, alt_title, duration, year)
    cur.execute("UPDATE your_db_name SET title=%s, alt_title=%s, duration=%s, year=%s WHERE id=%s", (title, alt_title, duration, year, id))
    conn.commit()
    conn.close()


create_table()

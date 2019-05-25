import sqlite3
import csv
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

database = "credit.db"
con = create_connection(database)
CreditCardCSV = "UCI_Credit_Card.csv"


def main():
    database = "credit.db"
 
    sql_create_credit_table = """CREATE TABLE credit_card_info (
                                        post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        limit_bal INTEGER NOT NULL,
                                        sex INTEGER NOT NULL,
                                        education INTEGER NOT NULL,
                                        marriage INTEGER NOT NULL,
                                        age INTEGER NOT NULL,
                                        pay_0 INTEGER NOT NULL,
                                        pay_1 INTEGER NOT NULL,
                                        pay_2 INTEGER NOT NULL,
                                        pay_3 INTEGER NOT NULL,
                                        pay_4 INTEGER NOT NULL,
                                        pay_6 INTEGER NOT NULL,
                                        bill_amt1 INTEGER NOT NULL,
                                        bill_amt2 INTEGER NOT NULL,
                                        bill_amt3 INTEGER NOT NULL,
                                        bill_amt4 INTEGER NOT NULL,
                                        bill_amt5 INTEGER NOT NULL,
                                        bill_amt6 INTEGER NOT NULL,
                                        pay_amt1 INTEGER NOT NULL,
                                        pay_amt2 INTEGER NOT NULL,
                                        pay_amt3 INTEGER NOT NULL,
                                        pay_amt4 INTEGER NOT NULL,
                                        pay_amt5 INTEGER NOT NULL,
                                        pay_amt6 INTEGER NOT NULL,
                                        default_payment_next_month INTEGER NOT NULL);"""
    if conn is not None:
        create_table(conn,sql_create_credit_table)
    else:
        print("Error: cannot create the database connection.")

def import_csv_SQLite(file):

SQL = """
    INSERT INTO credit_card_info()
    """
    with open(CreditCardCSV, 'rt') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with sqlite3.connect(database) as con:
            cursor = con.cursor()
            cursor.executemany(SQL, csv_reader)
import_csv_SQLite("UCI_Credit_card.csv")
import sqlite3
import sys
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
                                        pay_5 INTEGER NOT NULL.
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
    if con is not None:
        create_table(con,sql_create_credit_table)
    else:
        print("Error: cannot create the database connection.")

def import_csv_SQLite(file):
        stmt = '''
INSERT INTO credit_card_info (limit_bal,sex,education,marriage,age,pay_0,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,
bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6,default_payment_next_month)
VALUES(:limit_bal,:sex,education,:marriage,age,:pay_0,:pay_1,:pay_2,:pay_3,:pay_4,:pay_5,:pay_6,
:bill_amt1,:bill_amt2,:bill_amt3,:bill_amt4,:bill_amt5,:bill_amt6,:pay_amt1,:pay_amt2,:pay_amt3,:pay_amt4,:pay_amt5,:pay_amt6,:default_payment_next_month);
                '''

        with open(CreditCardCSV,'rt') as csv_file:
            csv_read = csv.DictReader(csv_file)

            with sqlite3.connect(database) as conn:
                curs = conn.cursor()
                curs.executemany(stmt,csv_read)
#main()
import_csv_SQLite("UCI_Credit_card.csv")
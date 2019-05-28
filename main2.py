import sqlite3, csv

create = '''
CREATE TABLE credit_card_info (
    id INTEGER,
    limit_bal INTEGER,
    sex INTEGER,
    education INTEGER,
    marriage INTEGER,
    age INTEGER,
    pay_0 INTEGER,
    pay_2 INTEGER,
    pay_3 INTEGER,
    pay_4 INTEGER,
    pay_5 INTEGER,
    pay_6 INTEGER,
    bill_amt1 INTEGER,
    bill_amt2 INTEGER,
    bill_amt3 INTEGER,
    bill_amt4 INTEGER,
    bill_amt5 INTEGER,
    bill_amt6 INTEGER,
    pay_amt1 INTEGER,
    pay_amt2 INTEGER,
    pay_amt3 INTEGER,
    pay_amt4 INTEGER,
    pay_amt5 INTEGER,
    pay_amt6 INTEGER,
    default_payment_next_month INTEGER);
'''
insert = '''
INSERT INTO credit_card_info 
(limit_bal,sex,education,marriage,age,
pay_0,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,
bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,
pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6,
default_payment_next_month)

VALUES(:limit_bal,:sex,:education,:marriage,:age,
:pay_0,:pay_1,:pay_2,:pay_3,:pay_4,:pay_5,:pay_6,
:bill_amt1,:bill_amt2,:bill_amt3,:bill_amt4,:bill_amt5,:bill_amt6,
:pay_amt1,:pay_amt2,:pay_amt3,:pay_amt4,:pay_amt5,:pay_amt6,
:default_payment_next_month);
                '''
con = sqlite3.connect("credit.db")
cur = con.cursor()
def loaddata():
    insert2 = '''
    INSERT INTO credit_card_info
    (id,limit_bal,sex,education,marriage,age,
    pay_0,pay_2,pay_3,pay_4,pay_5,pay_6,
    bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,
    pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6,
    default_payment_next_month)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''

    with open('UCI_Credit_Card.csv','r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['ID'],
        i['LIMIT_BAL'],
        i['SEX'],
        i['EDUCATION'],
        i['MARRIAGE'],
        i['AGE'],
        i['PAY_0'],
        i['PAY_2'],
        i['PAY_3'],
        i['PAY_4'],
        i['PAY_5'],
        i['PAY_6'],
        i['BILL_AMT1'],
        i['BILL_AMT2'],
        i['BILL_AMT3'],
        i['BILL_AMT4'],
        i['BILL_AMT5'],
        i['BILL_AMT6'],
        i['PAY_AMT1'],
        i['PAY_AMT2'],
        i['PAY_AMT3'],
        i['PAY_AMT4'],
        i['PAY_AMT5'],
        i['PAY_AMT6'],
        i['default.payment.next.month'])for i in dr]

    cur.executemany(insert2,to_db)
#cur.execute(create) #creates table
print("SQL statements executed")
#update marriage into single
cur.execute('UPDATE credit_card_info SET MARRIAGE = 2 WHERE MARRIAGE =3;')

#remove all negative BILL_AMT in 1-6
cur.execute('DELETE FROM credit_card_info WHERE BILL_AMT1 < 0 OR BILL_AMT2 < 0 OR BILL_AMT3 < 0 OR BILL_AMT4 < 0 OR BILL_AMT5 < 0 OR BILL_AMT6 < 0;')
#select and show first ten reocords in the table
cur.execute('SELECT * FROM credit_card_info LIMIT 9;')
[print(row) for row in cur.fetchall()]
#all records in bill_amt1 greater than 500k
cur.execute('SELECT * FROM credit_card_info WHERE BILL_AMT1 > 500000;')
[print(row) for row in cur.fetchall()]
#RECORDS FOR MARRIAGE 1,2
cur.execute('SELECT COUNT(*) FROM credit_card_info GROUP BY "MARRIAGE" HAVING "MARRIAGE" = 1 OR "MARRIAGE" = 2;')
[print(row) for row in cur.fetchall()]
#TOTAL NUMBER OF RECORDS
cur.execute('SELECT COUNT(*) FROM credit_card_info')
print(cur.fetchone())
#AVERAGE AGE
cur.execute('SELECT avg(AGE) FROM credit_card_info')
print(cur.fetchone())
#minimum limit bal
cur.execute('SELECT min(LIMIT_BAL) FROM credit_card_info')
print(cur.fetchone())
#Max limit bal
cur.execute('SELECT max(LIMIT_BAL) FROM credit_card_info')
print(cur.fetchone())
#payment_month 0 vs. payment_month = 1
cur.execute('SELECT Count(*) FROM credit_card_info GROUP BY "PAYMENT_MONTH";')
print (cur.fetchone())
#average age  in month 1 vs 2
cur.execute('SELECT avg(AGE) FROM credit_card_info GROUP BY "PAYMENT_MONTH";')
print (cur.fetchone())
#Min limit bal for payment month 0 vs 1
cur.execute('SELECT min(LIMIT_BAL) FROM credit_card_info GROUP BY "PAYMENT_MONTH";')
print (cur.fetchone())
#Max limit bal for payment month 0 vs 1
cur.execute('SELECT max(LIMIT_BAL) FROM credit_card_info GROUP BY "PAYMENT_MONTH";')
print (cur.fetchone())
#Average age for marriage groups 1,2
cur.execute('SELECT avg(AGE) FROM credit_card_info GROUP BY "MARRIAGE" = 1 OR "MARRIAGE" = 2')
print(cur.fetchone())
#Min limit bal for marriage 1,2
cur.execute('SELECT min(LIMIT_BAL) FROM credit_card_info GROUP BY "MARRIAGE" = 1 OR "MARRIAGE" = 2;')
print(cur.fetchone())
#Max limit bal for marriage 1,2
cur.execute('SELECT max(LIMIT_BAL) FROM credit_card_info GROUP BY "MARRIAGE" = 1 OR "MARRIAGE" = 2;')
print(cur.fetchone())
#defaulters in marriage group 1
cur.execute('SELECT Count(*) FROM credit_card_info WHERE "PAYMENT_MONTH" = 1 GROUP BY "MARRIAGE" HAVING "MARRIAGE" = 1 OR "MARRIAGE" = 2;')
print(cur.fetchone())
#defaulters in marriage group 0
cur.execute('SELECT Count(*) FROM credit_card_info WHERE "PAYMENT_MONTH" = 0 GROUP BY "MARRIAGE" HAVING "MARRIAGE" = 1 OR "MARRIAGE" = 2')
print(cur.fetchone())
con.commit()
cur.close()
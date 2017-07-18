import sqlite3
def insert_cauthu(CAUTHU):
    result = False
    conn = sqlite3.connect('quan_ly_ct.db')
    sql = "INSERT INTO CAUTHU()"
import sqlite3
conn = sqlite3.connect("quan_ly_ct.db")
sql = '''
       CREATE TABLE user(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
           );
        '''
sql1='''
       CREATE TABLE cauthu(
           id INTEGER PRIMARY KEY,
           ten TEXT NOT NULL,
           vitri TEXT NOT NULL,
           nam_gia_nhap INTEGER NOT NULL,
           gia REAL NOT NULL,
           hinh TEXT
       );'''
sql2='''
       INSERT INTO user(username,password) VALUES ('kientt','123456');
'''
conn.execute(sql2)
conn.execute(sql1)
conn.close()

class CAUTHU(object):
    def __init__(self,ten,vitri,nam_gia_nhap,gia,hinh):
        self.ten = ten
        self.vitri = vitri
        self.nam_gia_nhap = nam_gia_nhap
        self.gia = gia
        self.hinh = hinh
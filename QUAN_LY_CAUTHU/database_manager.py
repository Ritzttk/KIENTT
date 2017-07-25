import sqlite3

def insert_cauthu(CAUTHU):
    result = False
    conn = sqlite3.connect('quan_ly_ct.db')
    sql = "INSERT INTO cauthu(id,ten,vitri,nam_gia_nhap,gia,hinh) \
          VALUES (?,?,?,?,?,?)"
    if conn.execute(sql,(CAUTHU.ten,CAUTHU.vitri,CAUTHU.nam_gia_nhap,CAUTHU.gia,CAUTHU.hinh)):
        print("ADD successfully")
        result = True
    conn.commit()
    conn.close()
    return result

def insert_user(username,password):
    conn = sqlite3.connect("quan_ly_ct.db")
    sql = "NSERT INTO user(username,password) VALUES (?,?)"
    conn.execute(sql)
    conn.close()

def select_cauthu(CAUTHU):
    conn = sqlite3.connect("quan_ly_ct.db")
    listct = []
    cursor = conn.execute("SELECT * from CD")
    for row in cursor:
        listct.append(row)
    conn.commit()
    conn.close()
    return listct

def delete_cauthu(id):
    conn = sqlite3.connect('quan_ly_ct.db')
    print("Opened database successfully")
    cur = conn.cursor()
    sql = '''delete from cauthu where id=?'''
    cur.execute(sql,(id))
    conn.commit()
    conn.close()

def update_cauthu(id,gia):
    conn = sqlite3.connect('quan_ly_ct.db')
    print("Opened database successfully")
    cur = conn.cursor()
    sql = '''UPDATE cauthu SET gia = ? WHERE id =?'''
    cur.execute(sql,(id,gia))
    conn.commit()
    conn.close()

def select_user():
    conn = sqlite3.connect("quan_ly_ct.db")
    print("Opened database successfully")
    list_users = []
    cursor = conn.execute("SELECT * from user")
    for row in cursor:
        list_users.append(row)
    print("Operation done successfully")
    conn.commit()
    conn.close()


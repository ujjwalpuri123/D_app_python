import sqlite3

def connect():
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs book (id INTEGER PRIMARY KEY,title text,auther text,year integer,price integer)")
    conn.commit()
    conn.close()

def insert(title,auther,year,price):
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,auther,year,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM BOOK")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",auther="",year="",price=""):
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR auther=? OR year=? OR price=?",(title,auther,year,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,auther,year,price):
    conn=sqlite3.connect("stationery.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,auther=?,year=?,price=? WHERE id=?",(title,auther,year,price,id))
    conn.commit()
    conn.close()



connect()
#insert("the sun","john smith",1943,46)
delete(7)
#update(4,"the moon","john smooth",1232,33)
#print(view())
#print(search(auther="john smith"))
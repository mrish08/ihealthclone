"""""
import sqlite3 as sql


def insertUser(email,password):
    con = sql.connect("bitbo.db")
    cur = con.cursor()
    cur.execute("INSERT INTO login_ihealth (email,password) VALUES (?,?)", (email,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database-1.c8punsklsimv.ap-southeast-1.rds.amazonaws.com")
	cur = con.cursor()
	cur.execute("SELECT email, password FROM login_ihealth")
	users = cur.fetchall()
	con.close()
	return users
"""    
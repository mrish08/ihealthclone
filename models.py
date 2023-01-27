import paramiko
import sqlite3 as sql

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('database-1.c8punsklsimv.ap-southeast-1.rds.amazonaws.com', username="postgres", password="wew123WEW") 
def insertUser(email,password):
    con = sql.connect("bms.db")
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
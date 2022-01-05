# -*- coding: utf-8 -*-
import sqlite3

def check_table():
	conn = sqlite3.connect('dtb_user.db')
	cur = conn.cursor()
				
	cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='utilisateur' ''')

	if cur.fetchone()[0]==1 : 
		print("La table utilisateur existe")
	
	else:
		print("La table utilisateur n'existe pas")

	conn.commit()
	conn.close()


def check_data():
	conn = sqlite3.connect('dtb_user.db')
	cur = conn.cursor()
	cur.execute(''' SELECT spublickey,LENGTH(spublickey) FROM utilisateur WHERE LENGTH(spublickey)>=1; ''')

	conn.commit()
	conn.close()

def logging():
	conn = sqlite3.connect('dtb_user.db')
	cur = conn.cursor()
	cur.execute(''' SELECT 1 FROM utilisateur where username = 'Jacques' and password = 'Jacques1$' ''') 
	[exists] = cur.fetchone()
   
   	if exists:
		print('Jacques / Jacques1$ valide')
	else:
		print("Jacques / Jacques1$ invalide")

	conn.commit()
	conn.close()

check_table()
check_data()
logging()
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



check_table()
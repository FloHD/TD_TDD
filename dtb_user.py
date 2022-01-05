# -*- coding: utf-8 -*-
import sqlite3


def connect_to():
    try:
        conn = sqlite3.connect('dtb_user.db')
        cur = conn.cursor()
        print("Base de données créée et correctement connectée à SQLite")
        sql = "SELECT sqlite_version();"
        cur.execute(sql)
        res = cur.fetchall()
        print("La version de SQLite est: ", res)
        cur.close()
        conn.close()
        print("La connexion SQLite est fermée")
    
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)

def create_table():
    try:
        conn = sqlite3.connect('dtb_user.db')
        
        sql = '''CREATE TABLE utilisateur (
                  username TEXT NOT NULL,
                  password TEXT NOT NULL,
                  spublickey TEXT NOT NULL,
                  sprivatekey TEXT NOT NULL,
                  epublickey TEXT NOT NULL,
                  eprivatekey TEXT NOT NULL
              );'''

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Table SQLite 'utilisateur' créée")
        cur.close()
        conn.close()
    
    except sqlite3.Error as error:
        print("Erreur lors de la création de la table SQLite", error)


def drop_table():
    try:
        conn = sqlite3.connect('dtb_user.db')
        
        sql = '''DROP TABLE utilisateur;'''

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Table SQLite 'utilisateur' supprimée")
        cur.close()
        conn.close()
    
    except sqlite3.Error as error:
        print("Erreur lors de la suppression de la table SQLite", error)


def insert_into(username, password, spublickey, sprivatekey, epublickey, eprivatekey):
    try:
        conn = sqlite3.connect('dtb_user.db')
        cur = conn.cursor()
        #print("Connexion réussie à SQLite")
        
        sql = "INSERT INTO utilisateur (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES (?, ?, ?, ?, ?, ?)"
        value = (username, password, spublickey, sprivatekey, epublickey, eprivatekey)
        
        cur.execute(sql, value)
        conn.commit()
        print("Champs insérés avec succès dans la table utilisateur")
        cur.close()
        conn.close()
        #print("Connexion SQLite est fermée")
      
    except sqlite3.Error as error:
       print("Erreur lors de l'insertion dans la table SQLite", error)




#connect_to()
create_table()
#drop_table()
insert_into('Jacques',
            'Jacques1$',
            '1000000000',
            '0000000000',
            '1000000000',
            '0000000000'
            )
# insert_into('Eveline',
#             'Eveline2€',
#             '0000000001',
#             '1000000000',
#             '0000000001',
#             '1000000000'
#             )
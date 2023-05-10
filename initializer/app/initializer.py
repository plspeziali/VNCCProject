import psycopg2
import os
import time
import requests
import socket

time.sleep(10)

# Configurazione della connessione al database
conn = psycopg2.connect(database="body-performance",host=socket.gethostbyname("db"), user="admin", password="admin", port="5432")

# Nome della tabella da controllare
table = "body_performance"

# Query per controllare se la tabella esiste e non è vuota
query = f"SELECT EXISTS(SELECT 1 FROM {table})"

# Esecuzione della query
try:
    with conn.cursor() as cur:
        cur.execute(query)

except:
    conn.commit()
    # Se la tabella non esiste o è vuota, esegui il file .sql
    sql_file = "init.sql"
    if os.path.exists(sql_file):
        with open(sql_file, 'r') as f:
            sql = f.read()
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
            response = requests.get('http://training:3002/train')


cur.close()
conn.close()

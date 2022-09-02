import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('california', 'California Hotel',4.3, 495.20, 'San Francisco')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()
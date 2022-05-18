import sqlite3

connection = sqlite3.connect('shortURL.db')


with open('url.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO shortURL (URL, shortURL) VALUES (?, ?)",
            ('www.google.co.uk', 'google.co.uk')
            )

connection.commit()
connection.close()


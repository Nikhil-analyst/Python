#Please download the database file database.db. The file contains a table with 50 country names along with their area in square km and population.
#Please use Python to print out those countries that have an area of greater than 2,000,000.
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

rows = cur.execute("SELECT * FROM countries WHERE area >= 2000000").fetchall()
conn.close()

for i in rows:
    print(i)

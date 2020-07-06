import sqlite3

connection = sqlite3.connect("chinook.db")

crtrk = connection.cursor()
crtrk.execute("SELECT * FROM tracks")
anstrk= crtrk.fetchall()
for i in anstrk:
    print(i[1])

crsr = connection.cursor()
crsr.execute("SELECT * FROM artists")
ans= crsr.fetchall()
#for i in ans:
#    print(i[1])

cremp = connection.cursor()
cremp.execute("SELECT * FROM employees")
ansemp= cremp.fetchall()
#for i in ansemp:
#    print(i)
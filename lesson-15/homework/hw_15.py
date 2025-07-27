import sqlite3
conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
cur.execute('drop table if exists Roster')
conn.commit()
conn.close()
print("Roster table dropped successfully.")


import sqlite3
conn = sqlite3.connect("my_database.db")
curr = conn.cursor()
curr.execute('delete from Roster')
conn.commit()
conn.close()
print("Roster table deleted successfully.")


import sqlite3
conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
cur.execute('''
create table if not exists Roster(
            Name text, 
            Species text, 
            Age integer) ''')
conn.commit()
conn.close()
print("Database and Roster table created successfully.")


import sqlite3
conn = sqlite3.connect('my_database.db')
curr = conn.cursor()
curr.execute("""
insert into Roster (Name, Species, Age)
values('Benjamin Sisko',	'Human',	40),
             ('Jadzia Dax',	'Trill',	300),
             ('Kira Nerys',	'Bajoran',	29)  """)

conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect('my_database.db')
curr = conn.cursor()

curr.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# O‘zgarishlarni saqlash
conn.commit()

# Jadvaldan barcha ma'lumotlarni ko‘rsatish
curr.execute("SELECT * FROM Roster")
rows = curr.fetchall()

for row in rows:
    print(row)

conn.close()



import sqlite3

# Bazaga ulanish
conn = sqlite3.connect('my_database.db')

# Cursor yaratish
cur = conn.cursor()

# SELECT buyrug‘i: jadvaldagi barcha maʼlumotlarni olish
cur.execute("SELECT Name, Age FROM Roster where Species='Bajoran'")

# Natijalarni olish
rows = cur.fetchall()

# Natijalarni ko‘rsatish
for row in rows:
    print(row)

# Ulanishni yopish
conn.close()




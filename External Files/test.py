import sqlite3

connection = sqlite3.connect('ex_database.db')

c = connection.cursor()

# c.execute('''CREATE TABLE people (
# first_name text,
# last_name text,
# email text,
# password text
# )''')

# c.execute("INSERT INTO people VALUES ('aarav', 'sonani', 'aaravsonaniatpython@gmail.com' , 'aaravsonani')")

# c.execute("INSERT INTO people VALUES ('prakash', 'sonani', 'prakashsonani@gmail.com' , 'jedirrkmjred')")

c.execute("SELECT * FROM people WHERE last_name='sonani'")

print(c.fetchall())
# print(c.fetchone())
# print(c.fetchmany(3))

connection.commit()
connection.close()
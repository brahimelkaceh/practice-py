import sqlite3

# Create Database and connection
db = sqlite3.connect('app.db')

cr = db.cursor()

# Create SKILLS Table 
cr.execute('CREATE TABLE if not exists skills(name text, progress integer , user_id text)')
cr.execute('CREATE TABLE if not exists users(name text, age integer , user_id text)')
cr.execute('CREATE TABLE if not exists members(name text , member_id integer)')

# Insert User into Users table
# cr.execute("insert into users (name, age, user_id ) values('Brahim', 26, '981204')")
# cr.execute("insert into users (name, age, user_id ) values('Saida', 20, '021112')")
# cr.execute("insert into users (name, age, user_id ) values('Yahya', 1, '270502')")

# Memebers list 
members = ['bob', 'Belka' , 'adam' , 'yaya']

# for key, member in enumerate( members):
#     cr.execute(f"insert into members (name, member_id) values('{member}', {key + 1})")


# Fetch Data from Database
cr.execute("SELECT * FROM members")
all_members = cr.fetchall()
print(f'Members: {all_members}')

# Save Changes
db.commit() 



# Close database
db.close()
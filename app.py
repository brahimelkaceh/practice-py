import sqlite3

message_input = '''
What do you want to do 
"a" => add new member
"u" => update member
"d" => delete member
"r" => read member
n  please choose your option: 
'''    
# Connect to database
conn = sqlite3.connect('app.db')

cursor = conn.cursor()




# Define CRUD functions
def add_member():
    if conn is not None:
        try:
            name = input('Enter name: ').strip().capitalize()
            member_id = int(input('Enter member_id: '))

            cursor.execute(f"SELECT member_id FROM members WHERE member_id = {member_id}")
            
            member = cursor.fetchone()
            print(member)
            
            if member :

                print('Sorry There are members already in the database with this member ID')
                return
            
            else :

                cursor.execute('CREATE TABLE IF NOT EXISTS members (name TEXT, member_id INTEGER)')
                cursor.execute("INSERT INTO members (name, member_id) VALUES (?, ?)", (name, member_id))
                conn.commit()
                print(f'Member added successfully')

        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
        finally:
            conn.close()
    else:
        print('Error occurred while connecting to database')

def update_member():
    if conn is not None:
        try:
            member_id = int(input('Enter member_id: '))
            cursor.execute(f"SELECT * FROM members WHERE member_id = {member_id}")
            member = cursor.fetchone()
            
            if member is None:
                print('There is no Member with the given ID not')
                return
            else:
                name = input('Enter your new name: ').strip().capitalize()
                cursor.execute(f"update members set name = '{name}' WHERE member_id = {member_id}")
                conn.commit()
                print(f'Member updated successfully')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
        finally:
            conn.close()
    else:
        print('Error occurred while connecting to database')

def delete_member():
    if conn is not None:
        try:
            member_id = int(input('Enter ID\'s member how you want to delete: '))

            cursor.execute("DELETE FROM members WHERE member_id = ?", (member_id,))
            conn.commit()
            print(f'Member deleted   successfully')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
        finally:
            conn.close()
    else:
        print('Error occurred while connecting to database')

def read_member():
    if conn is not None:
        try:
            
            # Fetch members information from the database
            cursor.execute("SELECT * FROM members")
            members = cursor.fetchall()

            if len(members) == 0:
                print('No members found')
            
            for i, member in enumerate(members):
                print(f"Member {i + 1}: {member}")

        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
        finally:
            conn.close()
    else:
        print('Error occurred while connecting to database')

user_input = input(message_input)

command_list = ['a', 'u', 'd', 'r', 'q']

if user_input in command_list:
    if user_input == 'a':    
        add_member()
    elif user_input == 'u':    
        update_member()
    elif user_input == 'd':
        delete_member()
    elif user_input == 'r':
        read_member()
    else:
        print('Goodbye')
else:
    print('Your command is incorrect')

import sqlite3

def get_connection():
    try:
        conn = sqlite3.connect('app.db')
        return conn, conn.cursor()
    except sqlite3.Error as e:
        print(f"Connection failed: {e}")
        return None, None

def fetch_members_data():
    conn, cursor = get_connection()
    if conn:
        try:
            # Fetch members information from the database
            cursor.execute("SELECT * FROM members")
            members = cursor.fetchall()
            
            for i, member in enumerate(members):
                print(f"Member {i + 1}: {member}")
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            conn.close()

def create_new_member(name, member_id):
    conn, cursor = get_connection()
    if conn:
        try:
            # Create table for member information in the database
            cursor.execute('CREATE TABLE IF NOT EXISTS members (name TEXT, member_id INTEGER)')
            
            # Insert member information
            cursor.execute("INSERT INTO members (name, member_id) VALUES (?, ?)", (name, member_id))
            conn.commit()
            print("New member information inserted successfully")
        except sqlite3.Error as e:
            print(f"Error inserting member: {e}")
        finally:
            conn.close()

def update_member(name, member_id):
    conn, cursor = get_connection()
    if conn:
        try:
            # Update member information in the database
            cursor.execute("UPDATE members SET name = ? WHERE member_id = ?", (name, member_id))
            conn.commit()
            print("Member information updated successfully")
        except sqlite3.Error as e:
            print(f"Error updating member: {e}")
        finally:
            conn.close()

def delete_member(member_id):
    conn, cursor = get_connection()
    if conn:
        try:
            # Delete member from the database
            cursor.execute("DELETE FROM members WHERE member_id = ?", (member_id,))
            conn.commit()
            print("Member deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting member: {e}")
        finally:
            conn.close()

# Test your CRUD operations here
fetch_members_data()

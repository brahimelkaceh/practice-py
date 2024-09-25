


message_input = '''
What do you want to do 
"a" => add new member
"u" => update member
"d" => delete member
"r" => read member
"q" => Quite the app
please choose your option: 
'''	

# Define CRUD functions
def add_member():
    print('adding member')

def update_member():
    print('updating member')

def delete_member():
    print('deleting member')

def read_member():
    print('reading member')

user_input = input(message_input)

command_list = ['a', 'u', 'd', 'r', 'q']

if user_input in command_list:
    print('your command is correct')

    if user_input == 'a':	
        read_member()
    if user_input == 'u':	
        update_member()
    if user_input == 'd':
        delete_member()
    if user_input == 'r':
        read_member()
        

else:
    print('your command is incorrect')

                
class Member:
    not_allowed_names = ['evel', 'hell' , 'shit']
    total_members = 10
     
    @classmethod
    def get_total_members(num_members):
        print(f'The average of all members is {num_members.total_members}')
        print('This is a static method')

    def __init__(self, name , age , description ):
       self.name = name
       self.age = age
       self.description = description
    
    def introduce_member(self):
        if self.name.lower() in Member.not_allowed_names:
            print('Sorry, this name is not allowed.')
            return
        else :
            print(f'Hello, my name is {self.name}. I am {self.age} years old. {self.description}')



# Member()


bob = Member('bob' , 26 , 'this is a description of bob')
alex = Member('alex' , 30 , 'this is a description of alex')
sam = Member('sam' , 18 , 'this is a description of sam')
hell = Member('hell' , 18 , 'this is a description of hell')

# bob.introduce_member()
# hell.introduce_member()
# alex.introduce_member()
# sam.introduce_member()

# Member.get_total_members()

# print(bob.__class__)
# print(bob.name , bob.age , bob.description)
# print(alex.name , alex.age , alex.description)
# print(sam.name , sam.age , sam.description)

class User():


    def __init__(self , username):
        self.username = username
        print(f'Hello, {self.username} from Base class')
    
    def show(self , username , age , gender):
        self.username = username
        self.age = age
        self.gender = gender

        if self.gender != 'man':
            print(f'Hey, I am a miss, my name is {self.username} and my age is {self.age}')
        else:
            print(f'Hey, I am a gentleman, my name is {self.username} and my age is {self.age}')
        # print('show from Base class')

class SubUser(User):
    def __init__(self , username , identity):
        
        super().__init__(username)
        self.identity = identity

        print(f'Hello, {username} with id : {self.identity} from derived class')


# user_one = User('bob')
# user = SubUser()
# user_tow = SubUser()
# user_three = SubUser()

# name = input('Please enter your name? :')
# age = input('Please enter your age: ')
# gender = input('Please enter your gender:')
# user.show(name, age, gender)


# user_tow.show('Brahim' , 26 , 'mr')
# user_three.show('Saida' , 20, 'miss')


user_two = SubUser('Brahim' ,1522)

class say_Hello(): 

    def __init__(self , username):
        self.__username = username
    
        print(f'Hello {self.__username} from Say_Hello class')\
    
    def get__username(self):
        return self.__username
    
    def set__username(self, new__username):
        self.__username = new__username


say_Hello('bob')

bob = say_Hello('bob')

print(bob.get__username())
bob.set__username('elkaceh')
print(bob.get__username())
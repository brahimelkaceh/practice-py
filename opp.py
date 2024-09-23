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

bob.introduce_member()
hell.introduce_member()
alex.introduce_member()
sam.introduce_member()

Member.get_total_members()
# print(bob.__class__)
# print(bob.name , bob.age , bob.description)
# print(alex.name , alex.age , alex.description)
# print(sam.name , sam.age , sam.description)
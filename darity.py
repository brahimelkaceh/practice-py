myName = 'bob'
myAge = 26
myRank = 10
# print('my name is %s, and my age is %d, my Rank is %.2f' %(myName , myAge , myRank))
# print('my name is {:s}, and my age is {:d}, my Rank is {:.2f}'.format(myName , myAge , myRank))

myAwsome = [101 , 12 , 31 , 24 , 65 , 206 , 71 , 88 , -129]

# print(myAwsome[2:5])
# myAwsome[0:3] =['one', 'tow' , 'three']

# myAwsome.extend(['one', 'tow', 'three'])
# print(myAwsome[11])
# myAwsome.remove('one')

myAwsome.sort(reverse=True)
myList = ['a', 'b', 'c', 'd', 'e', 'f' , 1  , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
myList.reverse()
# myList.clear ()

myCopyList = myList.copy()
myList.append('bob')
myList.insert(-1, 'elkaceh')
# print(myCopyList)
# print(myList)

myTuple = 'tuple1' , 'tuple2' , 'tuple3'
mySecondeTuple = 'tuple4' , 'tuple5' , 'tuple6'

# print(myTuple + mySecondeTuple)

mySet = {'apple', 'orange', 'banana', 'ananas' , 'peach'}
mySecondSet = {'apple', 'orange', 'banana'   }
# myNewSet = mySet.copy()
# mySet.add('hh')
# mySet.remove('b')
# mySet.pop()
# mySet.union(mySecondSet)

# mySet.clear()



# mySet.update({'apple', 'orange', 'banana'})
# mySet.update(mySecondSet)
# print(myNewSet)
# print(mySet | mySecondSet)
# print(mySet)
# mySet.difference_update(mySecondSet)
# mySet.intersection_update(mySecondSet)
# mySet.symmetric_difference_update(mySecondSet)
# mySet.symmetric_difference_update(mySecondSet)

# print(mySet.difference(mySecondSet))
# print(mySet.intersection(mySecondSet))
# print(mySet.symmetric_difference(mySecondSet))

# print(mySecondSet.issubset(mySet))
# print(f'my set {mySet}')

myDectionary = {
    'firstName' : 'bob',
    'lastName' : 'elkaceh',
    'languages' : {
        'lang1' : 'english',
        'lang2' : 'french',
    }
}

html = {
    'name' : 'hyper text narkup language',
    'year' : 2002
}

js = {
    'name' :'javascript',
    'year' : 2008
}

programmingLanguages = {
   'html' : html , 'js' : js
}

# myLanguages = programmingLanguages.copy()
# print(f'programming languages {programmingLanguages.items()}')
# print(myLanguages)

# x = 5    
# y = 20
# print(x , y)
# y //= x

# print(x , y)

# email = input('Please enter your Email address : ')

# index = email.index('@')

# userN = email[:index]
# userS = email[index + 1:]

# print(f'Hello {userN}, your website is : {userS}')


age = int(input('Please enter your age : '))

unit = input('Please enter your unit months, weeks, days, hours, minutes, seconds : ').strip().lower()

months = age * 12

weeks =  months * 4
days = age * 365

hours = days * 24

minutes = hours * 60

seconds = minutes * 60

if unit == 'months':
    print(f'your age by months is : {months}')
elif unit == 'weeks':
    print(f'your age by weeks is : {weeks}')
elif unit == 'days':
    print(f'your age by days is : {days}')
elif unit == 'hours':
    print(f'your age by hours is : {hours}')
elif unit == 'minutes':
    print(f'your age by minutes is : {minutes}')
elif unit == 'seconds':
    print(f'your age by seconds is : {seconds}')
else : print(f'the unit that you chose is not correct #{unit}# , please try again')



# print(f'your age by months : {months} /n by weeks : {weeks} /n by days : {days} /n by hours : {hours} /n by minutes : {minutes} /n by seconds : {seconds} ') 
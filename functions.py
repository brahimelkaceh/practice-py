

# def getFriends(*friends):
#     for friend in friends:
#         print(f'Hello {friend.capitalize()}')

# getFriends('mohamed' , 'bob', 'brahim')
# langs = ( 'python', 'java', 'c++')
# skills = {
#     'python': 90,
#     'java': 85,
#     'c++': 70,
#     'html': 80,
#     'css': 85,
#     'javascript': 75,
# }
# def getSkills(name = 'uknown', *skills , **kwargs ):

#     print(f'{name.capitalize()},\nHas the following skills:')
#     for skill in skills:
#         print(f'- {skill}')

#     print('Additional skills:')
#     for key, value in kwargs.items():
#         print(f'- {key}: {value}%')

# getSkills('mohamed', *langs, **skills)

from functools import reduce


def cleanWord(word):

    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])


word = 'fffddsskkslss'

# print(cleanWord(word))


hello = lambda x:  f'hello {x}'

# print(hello('world'))

numbers = [1, 2,-3, -4]
# if all(numbers): # all the items in the list are TRUE
#     print('All numbers are greater than 0')
# else: 
#     print('Not all numbers are greater than 0')

# print('#' * 50)

lsit = [False , [] , {} , 1]

# if any(lsit): # at least on item must be TRUE
#     print('There is at least one itme is true')

# else:
#     print('No item is true')


a = 1 
b = 2
# print(bin(a))
# print(id(a))

# print('#' * 50)

# print(sum( numbers , 0))

# print(list(range(0, 11 , 2))) 

# print(abs(sum( numbers)))
# print(pow(sum( numbers) , 4 ))
# print(min(numbers))
# print(numbers[slice(5)])



def formatNumber(number , two):
    return number + two




for number in map(lambda number : number * 10 , numbers): print(number)

print('#' * 50)

for number in filter(lambda number : number > 0 , numbers): print(number)

print('#' * 50)

friends = ['brahim' , 'John' , 'doe' , 'fred' , 'bill' , 'bob']

for person in filter(lambda n : n.startswith('b') , friends ) : print(person)

print('#' * 50)


result = reduce(lambda num1 , num2 : num1 * num2, numbers)
# print(result)



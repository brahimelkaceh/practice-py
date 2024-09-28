# list = ['a', 'b', 'c', 'd', 'e' , 'D', 'F', 'G', 'H', 'I', ]

# # print(next(iter(list)) , end=' ')
# # print(next(iter(list)) , end=' ')
# # print(next(iter(list)) , end=' ')
# # print(next(iter(list)) , end=' ')  

# import re 

# # Remove the vowels from the list

# vowels = ['a', 'e', 'i', 'o', 'u']
# list = [word for word in list if not re.search(r'[aeiouAEIOU]', word)]

# # Convert all remaining words to uppercase

# list = [word.upper() for word in list]


# print("\nList after removing vowels: ", list)

import logging

# print(dir(logging))

logging.basicConfig(filename='my_app.log', filemode='w' , format='logger = %(asctime)s %(name)s %(levelname)s %(message)s' , datefmt='%Y-%m-%d %H:%M')
logging.critical('This is a critical Message')
logging.error('This is a error Message')
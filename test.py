list = ['a', 'b', 'c', 'd', 'e' , 'D', 'F', 'G', 'H', 'I', ]

# print(next(iter(list)) , end=' ')
# print(next(iter(list)) , end=' ')
# print(next(iter(list)) , end=' ')
# print(next(iter(list)) , end=' ')  

import re 

# Remove the vowels from the list

vowels = ['a', 'e', 'i', 'o', 'u']
list = [word for word in list if not re.search(r'[aeiouAEIOU]', word)]

# Convert all remaining words to uppercase

list = [word.upper() for word in list]


print("\nList after removing vowels: ", list)
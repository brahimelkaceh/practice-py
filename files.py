import os 

print(os.getcwd())
file = open('practice-py\loop.py' , 'r')
file2 = open(r'practice-py\test.py' , 'a')

file2.write('test = 10 \n')
file2.write('print(test)\n')

# os.remove('practice-py\test.py')


# print(file.readlines(10))

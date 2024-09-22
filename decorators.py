def myDecorator(func):

    def nestedFunc(*numbers):
        print('Inside the decorator')

        for number in numbers:
            if number < 0:
                print('Negative numbers are not allowed')
            else:
                print(f'Processing {number}')
        
        func(*numbers)
        print(f'After the decorator ')
    return nestedFunc # return a decorator 

@myDecorator
def getNum1(n1 , n2 , n3 , n4):
    return n1 , n2 , n3 , n4

getNum1(10 , -12 , 13 , -5)

# @myDecorator
# def getNum2(n1):
#     return n1

# getNum2( 20)

try:
    number = int(input('Enter a number:  '))
except:
    raise ValueError('Invalid input. Please enter a number.')
else:
    print(f'You entered: {number}')
finally:
    print('This code block always executes.')
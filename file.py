def main():
# this is a comment
   var = input('What is your name ? ')
   print('welcome,',hello(var))


# Remove whitespace from the string
#    var = var.strip()

# Make the string Capitalized 
# var = var.capitalize()
# var = var.title()

# Remove whitespace from the string and make it capitalized
#    var = var.strip().title()




#print('hello,', var)
def hello(name):
    return name.strip().title()


main()
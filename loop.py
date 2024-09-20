# websites = []

# maximum_websites = 2

# while maximum_websites > 0:
#     website_name = input("Enter a website name: ")

#     websites.append(f'https://{website_name.strip().lower()}')

#     maximum_websites -= 1
#     print(f"Total websites added: {len(websites)}, total website left : {maximum_websites}")
#     print(websites)
    
# else : 
#     print("Maximum websites reached, no more websites can be added.")

# print('#' * 40)

# if (len(websites) > 0): 
#     index = 0 

#     while index < len(websites):
#         print(f"{index + 1}. {websites[index]}")

#         index += 1


# PASSWORD GUESSE 

# password = 'password'
# guess = input("Enter your password: ")

# tries = 4



# while guess != password:
#     print("Wrong password! Try again.")
#     tries -= 1
#     print(f'Try again, you have {"last" if  tries == 0 else tries} chance')
#     guess = input("Enter your password: ")
#     if tries == 0: 
#         print("You have no more tries left.")
#         break
# else :
#     print("Password correct!")

skills = {
    'skill 1' : 80,
    'skill 2' : 85,
    'skill 3' : 90,
}

for skill in skills : 
    print(f"Skill{skill} => {skills[skill]}")


for skill, progress in skills.items(): 
    print(f"Skill{skill} => {progress}")


mySkills = {
    'skill 1' : {
        'HTML' : 80,
        'CSS' : 85
    },
    'skill 2' : {
        'JS' : 70,
        'PY' : 68
    }
}

print('#' * 50)
for skill , language in mySkills.items():
    print(f"{skill}")
    for language, progress in language.items():
        print(f"{language} => {progress}%")
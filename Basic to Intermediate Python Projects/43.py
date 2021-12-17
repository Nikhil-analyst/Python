#Create a script that generates a file where all letters
# of English alphabet are listed two in each line


import string

c= [(letters) for letters in string.ascii_lowercase]

with open("nickletters", 'w') as file:
    for count in range(0, 25,1):
        file.write(c[count] + c[count+1] + "\n")

print(c)





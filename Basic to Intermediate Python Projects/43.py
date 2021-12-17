#Create a script that generates a file where all letters
# of English alphabet are listed two in each line


import string

c= [(letters) for letters in string.ascii_lowercase]

# with open("nicklettersthree", 'w') as file:
#     for count in range(0, 24,2):
#         file.write(c[count] + c[count+1] + c[count+2] + "\n")

print(c[0::3])




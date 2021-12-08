#Create a script that converts all items of the range to strings
# Expected output:
#
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
# '12', '13', '14', '15', '16', '17', '18', '19', '20']

my_range = range(1, 21)

#Ans:

print([str(x) for x in my_range])

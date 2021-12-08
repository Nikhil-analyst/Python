#Create a script that generates a list whose items are products of the
# original list items multiplied by 10
my_range = range(1, 21)

#Ans"
list_a = []

for x in my_range:
    list_a.append(int(x)*10)
print(list_a)


# ALternate

print([10 * x for x in my_range])


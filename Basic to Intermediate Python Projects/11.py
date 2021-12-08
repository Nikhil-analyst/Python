#Create a script that generates a list of numbers from 1 to 20. Do not create a list manually.



#Ans:
my_range = range(1, 21)
print(list(my_range))

#Alternate using for loop

list_a = []
for i in range(1,21):
    list_a.append(i)
print(list_a)

# range()  is a Python built-in function that generates a range of integers. However,
# range()  creates a Python range object. To get a real list object,
# you need to use the list() function to convert the range object into a list object.
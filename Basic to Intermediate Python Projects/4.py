#The script generates an error. Please add the appropriate code that adds variables a and b without an error.
#A: The script generates an error saying that an integer object cannot convert to string implicitly.
#Please try to convert the integer to a string explicitly then or the string to an integer.

# Question: Fix the last line so that it outputs the sum of 1 and 2.
# lease do not change the first two lines, only the last one
# a = "1"
# b = 2
# print(a + b)




# Ans:

a = "1"
b = 2
print(int(a) + b)

# Values in Python can be of different types. In this
# exercise, the value assigned to a  was of string type (i.e., text)
# while the value of b  was an integer (i.e., whole number),
# and you cannot add strings with integers. Therefore we
# needed to convert the string to an integer using the int()
# addition operation's built-in function to be possible.
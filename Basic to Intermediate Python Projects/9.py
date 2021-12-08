#Complete the script so that it prints out a list containing the last three elements of list letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#Ans:
print(letters[-3:])


# [-3:]  means from the item with index -3  (i.e. h ) to the very last item
# of the list. When you don't put any index to the colon's right,
# everything is included, and upper-bound exclusivity is ignored.
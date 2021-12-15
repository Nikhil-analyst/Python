#Create a function that takes a string and returns the number of words
def count_words(string):
    string_list = string.split(" ")
    return len(string_list)

print(count_words("Hey there it's me!"))


# def count_words(string):
#     return (len(string.split(" ")))
# string = input("Give name: ")
# print(count_words(string))
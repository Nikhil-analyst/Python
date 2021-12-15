#Create a function that takes a text file and returns the number of words
# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         strng = file.read()
#         strng_list = strng.split(" ")
#         return len(strng_list)
#
# print(count_words("words1.txt"))


def count_words(words):
    with open(words, 'r') as file:
        string = file.read()
        string_list = string.split(" ")
        return len(string_list)
words1= ("C:\\Users\\Nikhil Raj\\OneDrive\Desktop\\Study\\Python\\Basic to Intermediate Python Projects\\words1.txt")
words1 = words1.replace("\\", "/")
print(words1)
# print("Nick\\Raj")
print(count_words(words1))
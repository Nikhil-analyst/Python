#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(",", " ")
        string_list = string.split(" ")
        return len(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(",| ", string)
        return len(string_list)

print(count_words_re("words2.txt"))


## Other Solution

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
#Count how many a the text file has
# import requests
#
# response = requests.get("http://www.pythonhow.com/data/universe.txt")
# text = response.text
# count_a = text.count("a")
# print(count_a)

import requests

response = requests.get("https://www.w3schools.com/python/module_requests.asp.txt")
text = response.text
count = 0
for letter in text:
    if letter == "a":
        count += 1

print(count)
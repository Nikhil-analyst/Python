#Print out the text of this file www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.
import requests

response = requests.get("https://www.w3schools.com/python/module_requests.asp.txt")
text = response.text
print(text)

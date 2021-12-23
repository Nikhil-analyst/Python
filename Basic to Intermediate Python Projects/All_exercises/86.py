#Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file

checklist = ["Portugal", "Germany", "Munster", "Spain"]

# with open("countries_clean.txt", "r") as file:
#     content = file.readlines()
#
# content = [i.rstrip('\n') for i in content]
# checked = [i for i in content if i in checklist]
#
# print(checked)

countries = []
with open("countries_clean.txt", "r") as file:
    contents = file.readlines()
contents = [content.strip("\n") for content in contents if "\n" in content]
print(contents)

for content in contents:
    if content in checklist:
        countries.append(content)
print(countries)
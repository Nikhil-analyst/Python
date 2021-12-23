#Add the missing items to the file

checklist = ["Portugal", "Germany", "Spain"]
# checklist = [i + "\n" for i in checklist]
#
# with open("countries_missing.txt", "r") as file:
#     content = file.readlines()
# print(checklist + content)
#
# updated_list = sorted(checklist + content)
#
# with open("countries_missing_fixed.txt", "w") as file:
#     for i in updated_list:
#         file.write(i)


with open("countries_missing.txt", "r") as file:
    contents = file.readlines()
contents = [content.strip("\n") for content in contents if "\n" in content]



for country in checklist:
    if country not in contents:
        contents.append(country)


contents = sorted(contents)
with open("countries_missing_nick.txt", "w") as file:
    for i in contents:
        file.write(i+ "\n")

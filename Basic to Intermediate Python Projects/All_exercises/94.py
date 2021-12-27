#Clean each line by removing s from https and adding a slash

# with open("urls.txt", "r") as file:
#     lines = file.readlines()
#
# print(lines)
#
# with open("urls_corrected.txt", "w") as file:
#     for line in lines:
#         line_remove_s = line.replace("s", "", 1)
#         print(line_remove_s)
#         line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[6:]
#         print(line_remove_s_add_slash)
#         file.write(line_remove_s_add_slash)

with open("urls.txt", "r") as file:
    line = file.readlines()


with open("urls_corrected_nikhil.txt", "w") as file:
    for string in line:
        string=string.replace("s","",1)
        strings= string[:6] + "/" + string[6:]
        file.write(strings)
import operator

file = open("InputFile.txt", "r")
Input_file = file.read()
Input_file = Input_file.split(" ")

Output_dict = {}
Total_Words = 0
Unique_Words = 0
for word in (Input_file):
    word = (word.replace(",", ""))
    word = (word.replace(".", ""))
    word = (word.replace("-", ""))
    word = (word.replace("\n", ""))


    if word.lower() in Output_dict.keys():
        Total_Words += 1
        Output_dict[word.lower()] += 1
    else:
        Total_Words += 1
        Unique_Words += 1
        Output_dict[word.lower()] = 1


Output_dict = dict(sorted(Output_dict.items(), key = operator.itemgetter(1), reverse= True))

with open("OutputFile.txt", "w") as file:
    file.write(f"Total Words - {Total_Words}\nUnique Words - {Unique_Words}\n\n\n")
    for i in Output_dict:
        file.write(f"{i}: {Output_dict[i]} \n")
    file.close()


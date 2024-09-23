import os
list_of_name = list(file_name.split(".")[0] for file_name in os.listdir("./40sol"))
print(list_of_name)

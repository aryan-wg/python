import string
with open("three.txt","w") as file:
    for char_1,char_2,char_3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
        file.write(f"{char_1}{char_2}{char_3}\n")

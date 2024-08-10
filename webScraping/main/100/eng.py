file = open("abc.txt","w")
data = ""
for i in range(26):
    data+=f"{chr(97+i)}\n"
file.write(data)
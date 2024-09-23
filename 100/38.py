file = open("two_togather.txt","w")
st = ""
for i in range(0,26,2):
    st += f"{chr(97+i)}{chr(i+98)}\n" 

file.write(st)
file.close()

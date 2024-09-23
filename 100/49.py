# import requests
# headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# r = requests.get("http://www.pythonhow.com", headers = headers)
# print(r.text[:100])

# from datetime import datetime 
#
# print(datetime.now().weekday())

# import random 
# import string
# import math
# st = ""
#
# # print(len(string.printable))
# for i in range(6):
#     num = math.ceil(random.random()*100)
#     st+=string.printable[num]
#
# print(st)


# def has_nums(st):
#     return any(item.isdigit() for item in st)
# def has_upper(st):
#     return any(item.isupper() for item in st)
#
# global length
# global num
# global upper
# length = False
# num = False
# upper = False
# while True:
#     passwd = input("Enter your password")
#     if(len(passwd)>=5):
#         length = True
#     if(has_nums(passwd)):
#         num = True
#     if(has_upper(passwd)):
#         upper = True
#
#     if(upper and length and num):
#         print("Your password is good")
#         break
#
#     else :
#         print("Your password is not good")
#         
#

file = open("countries_by_area.txt","r")
lines = file.readlines()
lines = [line for line in lines if line != "\n"]
remove_tabs_newline = lambda x:x.replace("\t","").replace("\n","") 
lines = [remove_tabs_newline(line) for line in lines ]
lines = [line.split(",") for line in lines]
for i in range(1,len(lines)):
    line = lines[i] 
    line.append(float(int(line[3])/float(line[2])))
lines.pop(0)
lines.sort(key=lambda x:x[4],reverse = True)

for i in range(5):
    print(lines[i][1])

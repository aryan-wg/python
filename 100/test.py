# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
from pprint import pprint
# a, c, e, g, and i.
# print(letters[::2])
# dictionary = {"a":1,"b":2}
# dictionary["c"] = 3
# sum = 0
# for item in dictionary:
#     sum+=dictionary[item]

# dictionary = filter(lambda x:x[1]<=2,dictionary.items())
# for i in dictionary:
#     print(i)

# dictionary = {"a":[i for i in range(1,11)],"b":[i for i in range(11,21)],"c":[i for i in range(21,31)]}
# for i in dictionary:
#     print(i)
# pprint(dictionary)
# for i in dictionary.items():
#     print(i[0],"has values",i[1])
# for i in range(26):
#     print(chr(97+i))
# c = 1
# def foo():
#     return c
# c = 3
# print(foo())
words1 = open("words1.txt","r")
content = words1.read()
content = content.split(" ")
print(len(content))
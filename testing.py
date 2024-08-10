dict1 = {"aryan":[1,2,3,4,5],"kamboj":[3,4,5]}
dict_len = { item:len(dict1[item]) for item in dict1 }

print(dict_len)
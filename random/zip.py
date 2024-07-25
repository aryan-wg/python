# list_one = [1,2,3,4,5,6]
# list_two = ["a","b","c","d","e"]
# list_three= ["z","y","x","w","v"]
# list_final = zip(list_one,list_two,list_three)

# for item in list_final:
#     print(item)

# print(list(list_final))

arguments = ["aryan",21]

class testing_class:
    def __init__(*args,**kwargs):
        print(*args)
        # print(**kwargs)

obj = testing_class(arguments,"something")

# def firstDecorator(func):
#     def checker(*args):
#         print(args)
#         return func(*args)
#     return checker
#
# @firstDecorator
# def this_prints(n):
#     print("hello world",n)
# this_prints("aryan")

def sortedListDecorator(func):
    def listSoter(*args):
        args = list(args)
        args.sort()
        return func(args)
    return listSoter
@sortedListDecorator
def this_prints_a_list(list):
    print(list)

this_prints_a_list(9,4,3,6,5,2,1,7)
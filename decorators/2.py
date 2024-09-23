def uppercaseDecorator(func):
    def allCaps(*args,**kwargs):
        # print(args,"args")
        args = [string.upper() for string in args]
        return func(*args)
    return allCaps

@uppercaseDecorator
def printer(*args):
    print(args,"args inside")
printer("hello world","this is the first string","this is the second string")


class CounterTill100:
    def __init__(self):
        self.number = 0
    
    def __next__(self):
# any class that has the __next__ dunder method will be called a generator 
        if self.number < 100:
            current = self.number
            self.number +=1
            return current
        else:
            raise StopIteration()

my_generator = CounterTill100()
# a function on which we can call the next() function is an ITERATOR not an itrable
print(next(my_generator))
print(next(my_generator))
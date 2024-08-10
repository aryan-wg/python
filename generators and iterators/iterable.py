# an object that has the __iter__ or (__len__ and  __getitem__) method will be an iterable (we ca use them in a for loop)
class FistHund:
    def __iter__(self):
        return First
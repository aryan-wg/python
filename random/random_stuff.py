# def add(x,y=3):
#   return x+y

# print(add(2,5))
# print(add(2))
# print(add(y=2,x=9))
# print(add(2,x=9))

class Parent:
    def __init__(self,name,phone):
      self.name = name
      self.phone = phone
    
    def __str__(self):
      return (f"Name is {self.name} phone no is {self.phone}")
    
class Child(Parent):
   def __init__(self,name,phone,subject) :
    super().__init__(name,phone)
    self.subject  = subject

dave = Child("Dave","1234","math")

print(dave.subject)
print(dave.phone)
print(dave)
print(dave.name)


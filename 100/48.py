# password = input("Please enter your password: ") 

# print(type("Hey".replace("ey","i")[-1]))

# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s " % (firstname,secondname))

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
#
# d["employees"].append({"firstName":"aryan","lastName":"kamboj"})
#
# print(d)

import json
import pprint
file = open("company1.json","r") 
data = file.read()
file.close()

file = open("company1.json","w") 
parsed = json.loads(data)
parsed["employees"].append({"firstName":"aryan","lastName":"kamboj"})
parsed = json.dumps(parsed)
pprint.pprint(parsed,stream=file)

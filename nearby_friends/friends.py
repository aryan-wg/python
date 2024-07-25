# there are 2 files *friends.txt *nearby_friends.txt
# we ask the user to input 3 friend names
# for each of the 3 if a name is found in the frineds.txt file we put that into the nearby_friends.txt file

friends_file = open("friends.txt","r")
# all_friends_str2 = friends_file.read() #reads the entire file as a string
# friends_file.seek(0)
# all_friends_str = friends_file.read() #reads the entire file as a string
# friends_file.seek(0)
all_friends_list = friends_file.readlines() #reads the entire file as a string

print(all_friends_list)
for fr in all_friends_list:
    print(fr)


#print(all_friends_str + "str")
#print(all_friends_str2 )

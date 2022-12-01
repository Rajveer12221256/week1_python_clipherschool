#  ask a user for name 
# Example - Rajveer
# print count of each word 
# output:
#   R:1
#   A:2
#   J:3
#   V:4
#   E:5
#   E:6
#   R:7

# Using count through while loop

name = input("Please enetr your name: ")
x = ""
i = 0
while i < len(name):
    if name[i] not in x:
        x += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
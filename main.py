from random import randint

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

"""print(names_string)
print(names)
print(len(names))
"""
roulete = randint(0,len(names)-1)

print("Person who is going to pay for todays meal is:" , names[roulete])


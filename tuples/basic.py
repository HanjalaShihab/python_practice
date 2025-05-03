first = ("Amar", "nam", "shihab")
print(first)
print(type(first))

# #tuple allows duplicate values:
second = ("Amar", "nam", "shihab", "Amar")
print(second)

#single value tuple:
a = ("Hanjala",) #not a string
print(type(a))

a = ("Hanjala") #string
print(type(a))


#length of a tuple:
items = ("apple", 1,2, True, 3.1416)
print(len(items))


#tuple constructor:
myTuple = tuple(("apple", "banana", "cherry"))
print(myTuple)
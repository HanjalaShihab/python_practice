#Tuples are used to store multiple items in a single variable.

#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#A tuple is a collection which is ordered and unchangeable.



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
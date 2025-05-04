#A set is a collection which is unordered, unchangeable*, and unindexed.

#* Note: Set items are unchangeable, but you can remove items and add new items.

#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
set = {"apple", "banana", "cherry", "apple"}
print(thisset)


#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {True, 1, False, 0}
print(thisset)

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {False, 0, True, 1}
print(thisset)


#length:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#allows different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)


print(type(set1))


#Set constructor:
newSet = set(("apple", "mango", "lichi"))
print(newSet)

#Dictionaries are used to store data values in key:value pairs.
#it is ordered, changeable and does not allow duplicates.

firstDict = {
    "name": "Shihab",
    "age": 21,
    "Year": 2001
}
print(firstDict)



#duplicates are not allowed:
secondDict = {
    "newName": "Hanjala",
    "age": 22,
    "Year": 2002,
    "Year": 2004
}
print(secondDict)    ##it will take the last value of the 'year' key



#length:
print(len(firstDict))



#The values in a dictionary can be of any data type:
newDictionary = {
    "brand": "Ford",
    "electric": False,
    "Year": 1964,
    "colors": ["red", "white", "blue"]
}
print(newDictionary)



#can be printed values using key:
print(newDictionary["brand"])


#type:
print(type(newDictionary))



##**dic() constructor**:
kibolbo = dict(name = "Keona", age = 100, country = "Uganda", porichoy = "Jani na")
print(kibolbo)
dictionary = {
    "fname": "Hanjala",
    "lname": "Shihab",
    "age": 24
}
dictionary["profession"] = "Student"   #adding new key and value
print(dictionary)


#adding new key and value using update() method:

newDictionary = {
    "fname": "Mithila",
    "lname": "Richy",
    "age": 22
}

newDictionary.update({"profession": "Student"})
print(newDictionary)


#removing items:

#use of pop() method:
newDictionary.pop("age")
print(newDictionary)

newDictionary.update({"age": 22})
print(newDictionary)


#use of popitem() method:
#popitem() removes the last item with the specified key name:
newDictionary.popitem()
print(newDictionary)


#use of del function:
del dictionary["fname"]
print(dictionary)


#use of clear() method:
dictionary.clear() #this will remove all items from the dictionary
print(dictionary)
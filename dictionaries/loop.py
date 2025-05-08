thisDictionary = {
    "firstName": "Shihab",
    "lastName": "Hanjala",
    "age": 23,
    "from": "Bangladesh"
}
for x in thisDictionary:
    print(x) #prints the keys of the dictionary
    
    


for x in thisDictionary.keys():
    print(x)




for y in thisDictionary:
    print(thisDictionary[y])  #this will print the values
    


    
for z in thisDictionary.values():  #this will print the values
    print(z)
    
    
    
#looping through both keys and values:
for x, y in thisDictionary.items():
    print(x, y)
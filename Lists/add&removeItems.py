                               #Adding items

# Use of append function to add items into a list:
items = [1 ,2 ,4, 9, 10]
items.append(3)
print(items)


# Use of insert function to add items into a list:
items = [1, 2, 4, 9, 10]
items.insert(2, 3)  #insert function needs two arguments, first one is index and other one is the item itself
print(items)



# Use of extend function:
  
   #it is used to add one list to another list
items1 = [1, 2, 3]
items2 = [4, 5, 6]
items1.extend(items2)
print(items1)

                                #Removing items

# Use of remove function:
items = ["apple", "banana", "cherry"]
items.remove("banana")
print(items)


# Use of pop function:
items = ["apple", "banana", "cherry"]
items.pop(1)
print(items)

# Or if we don't specify the index in pop function, it will remove the last item:
items = ["apple", "banana", "cherry"]
items.pop()
print(items)


# Use of del function:
items = ["apple", "banana", "cherry"]
del items[2]
print(items)


# Use of clear function:
items = ["apple", "banana", "cherry"]
items.clear()
print(items)
items = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(items[0]) # Accessing the first item
print(items[1]) # Accessing the second item


# Accessing items from the first to fourth item:
print(items[0:4]) #Excluding the fifth item though the index is 4

# Accessing the last item:
print(items[-1])

# Acessing the second last item:
print(items[-2])

# Accessing the last three items:
print(items[-3:])


# Checking if an item is avaiable in the list:
newItems = ["Canada", "USA", "Bangladesh", "Pakistan", "Germany"]
if "Bangladesh" in newItems:
    print("Bangladesh is existing in the list.")
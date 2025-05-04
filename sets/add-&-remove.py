#we can't change the elements in a set, but we can add or remove them
thisSet = {1, 2, 3, 4, 5}
thisSet.add(6)
print(thisSet)



#to add items from another set into the current set, we can use the update() function
newSet = {"apple", "banana", "cherry"}
againNewSet = {"lichi", "mango", "jackfruit"}

newSet.update(againNewSet)




#remove
thisSet.remove(6)  #if the item is not present, it will raise an error
print(thisSet)


  #or
thisSet = {1, 2, 3, 4, 5}
thisSet.discard(5)  #it will not raise an error if the item is not present
print(thisSet)



#we ca use the pop() method.But it will remove a random item



#use of clear() method
thisSet.clear()
print(thisSet)



#use of del function
del newSet
print(newSet)
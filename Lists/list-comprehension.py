#if not list-comprehension we write this line of codes below:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    newlist.append(x)
    
print(newlist)


#now if we apply list-comprehension in the above code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


#using a filter(if):

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)



#making the newlist items upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)



#Or we can write this:
newlist = [ x for x in range(10)]
print(newlist)

  #or
newlist = [x for x in range(10) if x > 5]
print(newlist)



#we can set the outcome to whatever value or change the expression:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['shihab' for x in fruits]

print(newlist)


#if in list-comprehension works as a filter not as a condition.
#if we want to use if else condition we have to use this syntax(before for):
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x !="banana" else "kichuna" for x in fruits]
print(newlist)
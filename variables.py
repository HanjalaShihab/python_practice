x = 10
print(x)

y = "Shihab"
print(y)

#to specify the data type of a variable we can use type casting:
x = str(3) # x is string
y = int(2) # an integer
z = float(3) # a float

print(x,",",y,",",z)


#for strings double quotes or single quoter does not matter:
name = "Shihab"
name2 = 'Hanjala'
print(name)
print(name2)


#we can assign multiple values to multiple variables in just one line:
x, y, z = "10", "20", "30"
print(x)
print(y)
print(z)


#Unpack a collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



#Global variables:
x = "Shihab"

def myfunction():
    print("My name is", x)

myfunction()


#Local variables:
y = "Hanjala"

def myfunc():
    y = "Muhammad"
    print(y)
    
myfunc()
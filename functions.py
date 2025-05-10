#creating a function:
def myFunction():
    print("I am Shihab from Bangladesh.")
    


#calling the function to see the outcome:
myFunction()


#function with parameters:
def newFunction(name, age):
    print("My name is: ", name)
    print("My age is: ", age)
    print(" ")

newFunction("Shihab", 24)
newFunction("Richy", 22)
newFunction("Keona", 100)



#we can also send arguments with key = value syntax:
def onnoFunction(child3, child2, child1):
    print("The child name is: ", child3)

onnoFunction(child1 = "Hanjala", child2= "Muhammad", child3= "Shihab")



#default parameter value:
def myFunction(country = "Bangladesh"):
    print("I am from: ", country)
    
myFunction("Canada")
myFunction("Germany")
myFunction()   #default value will be printed here
myFunction("Palestine")



print(" ")



#passing a list as an argument:
def myFunction(food):
    for x in food:
        print(x)
        
        
fruits = ["apple", "banana", "cherry"]

myFunction(fruits)



print(" ")


#recursive function:
def factorial(n):
    if n == 0:
        result = 1
        return result
    else:
        result = n * factorial(n - 1)
        print(result)
        return result

factorial(5)

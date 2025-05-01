numbers = [ 1, 4, 6 ,7 ,8 ,9]
for x in numbers:
    print(x)
    


#Looping through a string:
name = "Muhammad"
for x in name:
    print(x)
    
    
 
# break statement:   
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
    
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    print(i)
    
    

# continue statement:
genre = ["pop", "rock", "jazz"]
for x in genre:
    if x == "rock":
        continue
    print(x)



# range() function:
for x in range(10):
    print(x)
    
    
for i in range(2, 12):
    print(i)
    

for y in range(3, 13, 3):
    print(y)
    


# else in for loop:
    #else in for loop is used to print a anything after the loop is finished.Like 'finally' in Java.
for x in range(6):
    print(x)
else:
    print("Finished!")
    
#if we use break statement in the loop, else will not be executed.
for x in range(7):
    if x == 4:
        break
    print(x)
else:
    print("Finished!")




# nested for loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    for y in fruits:
        print(x, y)

  #or
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i, j)
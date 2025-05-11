cars = ["Ford", "Volvo", "BMW"]

x = cars[0]   #Accessing elements of an array
print(x)


cars[1] = "Toyota"
print(cars)


y = len(cars)
print(y)


#adding new items:
cars.append("Honda")
print(cars)


#looping through an array:
for x in cars:
    print(x)
    
    
#removing items:

cars.pop()  #poping the last item
print(cars)


cars.remove("Ford")
print(cars)
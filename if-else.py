# Logical conditions:
   # x > y
   # x < y
   # x == y (equals)
   # x != y (not equals)
   # x >= y (greater than or equal to)
   # x <= y (less than or equal to)
  
  
a = 100
b = 50
if a > b:
    print("a is greater than b")
    
elif a == b:
    print("a is equal to b")
    
else:
    print("b is greater than a")
    
    

###
num = (input("Enter a number: "))   # we can use int(input(" ")) for integer input.Basically we can specify the data type of input
num = int(num)

if num > 0:
    print(num ,"is Positive number")
elif num == 0:
    print("zero")
else:
    print(num ,"is negative number")




###
Bangladesh = ["Dhaka", "Chittagong", "Khulna", "Cumilla", "Rajshahi"]
Pakistan = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
Germany = ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"]

Bangladesh = [city.lower() for city in Bangladesh]  #converting the uppercase to lowercase
Pakistan = [str.lower(city) for city in Pakistan]   #another way of convertion
Germany = [city.lower() for city in Germany]

city = input("Enter city name: ").lower()

if city in Bangladesh:
    print(city, "is a city in Bangladesh")
elif city in Pakistan:
    print(city, "is a city in Pakistan")
elif city in Germany:
    print(city, "is a city in Germany")
else:
    print(city, "is not in the list of cities")
#accessing by key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

#or

x = thisdict.get("model")
print(x)



x = thisdict.keys()
print(x)



x = thisdict.values()
print(x)



car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)

car["color"] = "white"

print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)

car["year"] = 2020
print(x)



#items() function:
x = thisdict.items()
print(x)



#if
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Model is one of the keys in the dictionary")
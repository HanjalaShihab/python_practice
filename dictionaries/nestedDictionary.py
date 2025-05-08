family = {
    "father": {
        "name": "Ferdaous",
        "profession": "Lecturer"
    },
    "mother": {
        "name": "Pervin",
        "profession": "Housewife"
    },
    "child": {
        "name": "Omar",
        "profession": "student"
    }
    
}

print(family)

#or we can write like this:
father = {
    "name": "Ferdaous miah",
    "age": 55
}
mother = {
    "name": "Pervin akter",
    "age": 50
}
child = {
    "name": "Tasnim omar",
    "age": 14
}

myFamily = {
    "Father": father,
    "Mother": mother,
    "Children": child
}

print(myFamily)


#accessing the items of nested dictionary:
print(myFamily["Father"]["name"])
print(myFamily["Children"]["name"],",age", myFamily["Children"]["age"])


#loop through:
for x, y in myFamily.items():
    print(x)
    
    for yy in y:
        print(yy, ":", y[yy])
thisTuple = (1, 2, 3, 4, 5)
print(thisTuple[1])


thisTuple = ("apple", "banana", "cherry","apple", "banana", "cherry")
print(thisTuple[3:5])  #excluding 5th index


thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-1])  #last item


thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-2])  #second last item



thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("There is an apple in the tuple")
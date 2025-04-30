# Use of sort function:
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

numbers = [100, 30, 40, 20, 60, 50]
numbers.sort()
print(numbers)

    #** Sort function is case sensitive.
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort() # Capital letters are sorted first
print(thisList)

  # So we can use str.lower function to sort the list in a case insensitive way:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort(key = str.lower)
print(thisList)



# Sorting a list in reverse order according to the alphabetical order:
items = ["orange", "mango", "kiwi", "pineapple", "banana"]
items.sort(reverse = True)
print(items)


# Sorting a list in reverse order using reverse() function.From the last one to the first one:
numbers = [100, 30, 40, 20, 60, 50]
numbers.sort()
numbers.reverse()
print(numbers)
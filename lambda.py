#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

myfunction = lambda a: a + 10

print(myfunction(5))


  #so in normal function we would write the above code like this:

def myfunction(a):
    return a + 10

print(myfunction(5))



#lambda within a function:
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))




nums = [5, 2, 9, 1]
sorted_nums = sorted(nums, key=lambda x: x)
print(sorted_nums)



words = ['apple', 'banana', 'kiwi']
# Sort by word length
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # ['kiwi', 'apple', 'banana']




#**sorting a list of dictionaries:
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Charlie', 'score': 70}
]

# Sort by score (descending)
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)

for student in sorted_students:
    print(student)

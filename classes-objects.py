class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
p1 = Person("Hanjala", 36)
print(p1.name)
print(p1.age)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def __str__(self):
        return f"Name: {self.name}({self.age})"
    
p1 = Person("Mithila Islam Richy", 22)
print(p1)

p2 = Person("Hanjala Muhammad Shihab", 24)
print(p2)



#we can change the variables values:
class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def __str__(self):
        return f"Name: {self.name} and department: {self.department}"

Student1 = Student("Hanjala Muhammad Shihab", "CSE")

print(Student1)

Student1.department = "SWE"

print(Student1)
#Creating a child class(Student), where parent class is Person:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    
    def printName(self):
        print(self.fname, self.lname)
    
class Student(Person):
    pass


x = Student("Hanjala", "Shihab")
x.printName()



#we can add the __init__ method in the Student class:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
        
    def printNames(self):
        print(self.fname, self.lname)
        
    
class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
        
x = Students("Mithila Islam", "Richy")
x.printNames()



#we can add properties and methods to the child class:
class parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        

class child(parent):
    def __init__(self, fname, lname, birthYear):
        super().__init__(fname, lname)
        self.birthYear = birthYear  #or we could directly declare the year like self.birhtYear = 2001 without the birthYear parameter
        
    def printDetails(self):
        print("Name: ", self.fname, self.lname , ",was born in", self.birthYear)
        
z = child("Hanjala", "Shihab", 2001)
z.printDetails()
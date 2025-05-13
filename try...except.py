try:
    print(x)  #x is not defined so it will generate an error
except:
    print("An exception occurred")
    
    

#to execute a special block of code for a special kind of error:
try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except:
    print("Something else went wrong.")
    
    

#else keyword to define a block of code to be executed if no error raised:
try:
    print("Shihab")
except:
    print("An erro occured")
else:
    print("Nothin happend!")
    
    

#try to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
    try:
        f.write("My name is shihab")
    except:
        print("Something went wrong when writing to the file!")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file.")  #this line will be printed because demofile.txt doesn't exist.
    
    
    

#we can raise an exception:
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")


  #or
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed.")
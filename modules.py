#modules is like importing another python file to an another file
#it can be built in or any common file we develop
#we can import partially anything from a file or the whole file

#importing 'platform' which is a built-in module.
import platform

x = platform.system()

print(x)


#to see the variabls and functions in a file we can use the dir() function in module
y = dir(platform)
print(y)
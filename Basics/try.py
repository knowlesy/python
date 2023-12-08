# this will create an error 
try:
    if name > 3:
        print("hello")

#this will catch the error 
try:
    if name > 3:
        print("hello")
except:
    print("ERROR: An error was dectected")

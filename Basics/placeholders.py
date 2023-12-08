name = "jim"
print (name + "is 30 years old")

# %d interger 
# %s string
name = "pete"
sentnece = "%s is 35 years old"
print (sentnece)

#correct way to print place holder  
print(sentnece % name)

sentence2 = "%s %s went to the factory"
print(sentence2 % ("John", "Doe"))

sentence3 = "%s is %d years old"
print(sentence3 % ("john", 40))

number = 20
sentence3 = "%s is %d years old"
print(sentence3 % ("john", number))

number = 23
name = "James"
sentence3 = "%s is %d years old"
print(sentence3 % (name, number))

name = "jake"
print (f"Hello, {name}")

x = 10
y = 99
print (f"The sum of x and y is {x+y}")

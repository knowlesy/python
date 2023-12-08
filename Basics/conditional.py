# == < > >= <= !=

if 3 < 2:
    print("hello")
else:
    print("oh ohhh")


if 3 > 2:
    print("hello")
else:
    print("oh ohhh")


# else if 
age = 20
if age <= 15:
    print("your at step 1")
elif age == 20:
    print("you hit the else if step 2!")
else:
    print("you hit step 3 and escaped the if and else if")

# and 
age = 20
if age <= 15:
    print("your at step 1")
elif age >=10 and age <=30:
    print("you hit the else if step 2!")
elif age == 21:
    print("you hit the else if step 3!")
else:
    print("you hit step 4 and escaped the if and else if's")

#or
age = 20
if age > 10 or age <30:
    print("hi")

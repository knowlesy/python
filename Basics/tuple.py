#lists but are immutable 
tup = ('oranges', 'apples', ' cherrys')
print (tup)
print (tup[0])

# wont work as it cant be modified 
tup[0] = 'milk'

#can print
tup = ('oranges', 'apples', ' cherrys')
print(tup[0])


tup2 = (11,13)
#can join 
tup3 = tup + tup2
print (tup3)

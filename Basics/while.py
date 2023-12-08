c = 0 
while c < 100:
    c = c + 1 
    print(c)

# break 
c = 0 
while c < 6:
    c = c + 1 
    if c == 2:
        break
    print(c)

# continue
c = 0 
while c < 5:
    c = c + 1 
    if c == 3:
        continue
    print(c)

# pass - A pass statement signals to a loop that there is “no code to execute here.” 
c = 0 
while c < 7:
    c = c + 1 
    if c == 5:
        pass
    print(c)

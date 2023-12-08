students = ['bob', 32, 'rachel', 30]
print(students)
print(students[2])

students2 = {'bob':32, 'rachel':35, 'emily':40}
print(students2)
#prints interger associated 
print(students2['rachel'])

#emily gets older
students2['emily'] = 41
print(students2)

#bob leaves
del students2['bob']
print(students2)

#treats these as unique so will print the last one in the dictionary 
students3 = {'bob':32, 'rachel':35, 'bob':40}
print(students3['bob'])

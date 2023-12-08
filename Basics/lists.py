item1 = 'apples'
item2 = 'pineapple'
print(item1,item2)

shopping_list = ['apples', 'pears', 'oranges', 'cheese']
print(shopping_list[0])
print(shopping_list[3])
#slicing
print(shopping_list[0:2])


#add items to the list
shopping_list.append('milk')
print(shopping_list)

#replaces apples 
shopping_list[0] = 'beer'
print(shopping_list)

#del an item, deletes pears 
del shopping_list[1]
print(shopping_list)


shopping_list2 = ['bread', 'jam']
print(shopping_list+shopping_list2)

print(shopping_list2 * 2)


list_num = (1,4,6,7,9, 1000, 20)
print(max(list_num))
print(min(list_num))

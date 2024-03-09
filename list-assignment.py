my_list = []
#append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#insert
my_list.insert(1,15)
print(my_list)
#extend list
addition = [50,60,70]
my_list.extend(addition)
print(my_list)
#remove last element
last_element = my_list.pop()
print(my_list)
#sort in ascending order
ascending = my_list.sort()
print(my_list)
#find index of value 30
search_item = 30
index = my_list.index(search_item)
print(f"The index of {search_item} is: {index}")

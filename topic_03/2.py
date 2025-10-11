print("Тестування функцій списків\n")

my_list = [1, 3, 5]
print("Початковий список:", my_list)

# append()
my_list.append(7)
print("append(7):", my_list)

# extend()
my_list.extend([9, 11])
print("extend([9, 11]):", my_list)

# insert()
my_list.insert(1, 2)
print("insert(1, 2):", my_list)

# remove()
my_list.remove(5)
print("remove(5):", my_list)

# sort()
my_list.sort()
print("sort():", my_list)

# reverse()
my_list.reverse()
print("reverse():", my_list)

# copy()
copy_list = my_list.copy()
print("copy():", copy_list)

# clear()
my_list.clear()
print("clear():", my_list)
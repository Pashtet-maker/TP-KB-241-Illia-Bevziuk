print("Тестування функцій словників\n")

my_dict = {'name': 'Anna', 'age': 20, 'city': 'Kyiv'}
print("Початковий словник:", my_dict)

# update()
my_dict.update({'age': 21, 'country': 'Ukraine'})
print("update({'age': 21, 'country': 'Ukraine'}):", my_dict)

# keys()
print("keys():", list(my_dict.keys()))

# values()
print("values():", list(my_dict.values()))

# items()
print("items():", list(my_dict.items()))

# del
del my_dict['city']
print("del my_dict['city']:", my_dict)

# clear()
my_dict.clear()
print("clear():", my_dict)
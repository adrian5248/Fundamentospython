# Colecciones en python
# Listas
# [item1, item2, item3]
my_list = [1, "dos", 3.14, False, []]
print(type(my_list))
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[-1])

my_list[3] = True

my_list.append("Hola") # Inserta al final
my_list.insert(0, [0, 0])

my_list.remove(3.14)
print(my_list)

num_list = [3, 5, 9, 1, 1, 3, 2, 5, 8]
print(num_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)

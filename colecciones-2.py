# Tuplas 
# (item1, item2, itemN)
# Inmutables
my_tuple = ("uno", 2, 3.1, False)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
# Error
# my_tuple[0] = "nuevo Valor"

# Conjuntos Set 
# {item1, item2, itemN}
# Coleccion sin índice y sin duplicados

my_set = {1, 2, 2, 2, 3, 4, "uno"}
print(type(my_set))
print(my_set)
my_set.add(5)

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Diccionarios 
# { item1: valor, item2: valor }

alumno = {
    "name": "Goku",
    "lname": "Sayayin",
    "age": 19,
    "genre": "H",
    "Calificaciones": [9, 9, 9]
}

print(type(alumno))
print(alumno)
print(alumno["name"], alumno["lname"])
if alumno["age"] < 18:
    print("Es menor de edad")
alumno["Calificaciones"].append(10)
print(alumno["Calificaciones"])
   
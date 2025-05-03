###Sets##
my_set=set()
print(type(my_set))

my_other_set = {'jairo','vargas',48}
print(type(my_other_set))


##Operaciones con sets###
print(len(my_other_set))

my_other_set.add('Bucaramanga')
print(my_other_set)  ## un set no tiene orden

my_other_set.add('Bucaramanga')
print(my_other_set) ## Un set no permite elementos duplicados

print('jairo' in my_other_set) ## Verificar si un elemento esta en el set
print('joiro' in my_other_set)

my_other_set.remove('vargas')
print(my_other_set)

my_other_set.clear()
print(my_other_set) ## Eliminar todos los elementos de un set

# del my_other_set ## Eliminar el set

"""
my_set= {'adriana','gualdron',42}
my_list =list(my_set) ## Convertir un set en una lista
print(my_list)
"""

my_set2={'jairo','vargas',48}
my_new_set = my_set2.union(my_other_set)
print(my_new_set)

print(my_set2.union({'programador'}))
print(my_set2.difference(my_set)) ## Diferencia entre dos sets


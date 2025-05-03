
###Tuplas###

mi_otrher_tuple=(2,1.80,'Bucaramanga','santander')


my_tupple= (48,1.70,'jairo','vargas')
print(my_tupple)
print(type(my_tupple))
print(my_tupple[0])
print(my_tupple[1])
print(my_tupple[-1])
print(my_tupple.count('jairo'))
print(my_tupple.index('vargas'))

my_sun_tuple = my_tupple + mi_otrher_tuple
print(my_sun_tuple)
print(my_sun_tuple[3:6])

my_tupple=list(my_tupple) ##volver la tupla lista
print(type(my_tupple))

del my_tupple ##borrar la tupla


###Listas###

my_other_list =[5,15,80,25,30]
print(my_other_list)
print(len(my_other_list))

my_list = [15,1.70,'jairo','vargas']
print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[1])
print(my_list[-2])
print(my_list[-1])
print(my_list.count(15)) #cuanto se rept el dato (en este caso 15)

edad,estatura,name,surname=my_list
print(name)

print(my_list + my_other_list)
#Error print(my_list - my_other_list)

my_list.append('jairodev') #agregar un Valor a la lista al final
print(my_list)

my_list.insert(1,'azul') #inserta un Valor en la posicion deseada
print(my_list)

my_list.remove('azul') #elimina un valor de la lista 
print(my_list)

my_list.pop()
print(my_list)

print(my_list.pop()) #muestra el valor borrado

print(my_list.pop(2))

my_pop_element = my_list.pop(-1)
print(my_pop_element)

del my_list[-1]  #Borrar un dato por indice 
print(my_list)


my_list.clear() #Borrar toda la lista.
print(my_list)

print(my_other_list)


print(my_other_list)


my_other_list.clear()
print(my_other_list)

my_new_list =my_other_list.copy()
print(my_new_list)

my_new_list.reverse()#devuelve datos en orden de ultimo a primero
print(my_new_list)

my_new_list.sort()
print(my_new_list)




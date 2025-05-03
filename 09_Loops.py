###Loops###

#while loop
#while se repite mientras tenga la condicion
"""
my_condition = 0


while my_condition < 10:
    print(my_condition)
    my_condition += 2
else : 
    print('El loop ha terminado')
print('La ejecucion continua')

"""
my_condition = 0

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print('se detiene la ejecucuion')
        break
    print(my_condition)
    
print('La ejecucion continua')
          

#For 
#For se repite por cada elemento de una lista

my_list =[35,24,62,52,30,30,17]
for element in my_list:
    print(element)
    
my_tupple= (48,1.70,'jairo','vargas')
for element in my_tupple:
    print(element)

my_set = {'jairo','vargas',48}
for element in my_set:
    print(element)

my_dict={'nombre':'Jairo','apellido':'Vargas','edad':48,1:'python'}
for element in my_dict:
    print(element)
    if element == 'apellido':
        break
    print('Se ejecuta')
else:
    print('El loop ha terminado')
    
print('La ejecucion continua')



###Dictionares###


my_dict = {}
print(type(my_dict))
my_other_dict ={}

my_other_dict={'nombre':'Jairo','apellido':'Vargas','edad':48,1:'python'}
print(my_other_dict)


my_dict={
    'nombre':'Jairo',
    'apellido':'Vargas',
    'edad':48,
    'Lenguejes':['Python','Java','C#'],
    'Cedula':91490735
    }
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))
print(my_dict['nombre'])

my_dict['nombre']='Adriana' ## Modificar un valor
print(my_dict['nombre'])

my_dict['Ciudad']='Bucaramanga' ## Agregar un nuevo valor
print(my_dict)

del my_dict['Ciudad'] ## Eliminar un valor
print(my_dict)

print('Vargas'in my_dict)
print('apellido'in my_dict) ##acceder al titulo
print('varas'in my_dict)

print(my_dict['apellido']) ##acceder a un elemento

print(my_dict.items())
print(my_dict.keys()) ##solo tae las llaves o titulos 
print(my_dict.values()) ## Trae los elementos

my_new_dict=my_other_dict.fromkeys(('nombre','apellido')) ##Crea un diccionario nuevo sin valores
print(my_new_dict)

my_new_dict=dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict=dict.fromkeys(my_dict,('adriana','gualdron'))
print(my_new_dict)

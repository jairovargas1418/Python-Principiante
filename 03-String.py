

###Strings###
casa ='Avenida el tejar'
municipio='Floridablanca'
print(casa + ' ' + municipio)

mi_nueva_sring ='este parrafo tiene salto de linea\ndebajo'
print(mi_nueva_sring)

mi_string_tabulacion='\testo es una Tabulacion '
print(mi_string_tabulacion)

mi_escape_string = '\tEste es un string\nescapado '
print(mi_escape_string)

#Formateo 1 forma
name,surname,age= 'jairo','Vargas',48
print('Mi nombre es: {} {} y mi edad es: {}'.format(name,surname,age))

#Formateo 2 forma 
print('Mi nombre es: %s %s y mi edad es: %d' %(name,surname,age))

#Formateo 3 forma y mas usada interpolacion
print(f'mi nombre es: {name} {surname} y mi edad es: {age}')

#Desempaquetado de caracteres
lenguaje ='Python'
a,b,c,d,e,f =lenguaje
print(a)
print(b)

#Division
lenguaje_slice =lenguaje [1:3]
print(lenguaje_slice)

lenguaje_slice =lenguaje [1:]
print(lenguaje_slice)

lenguaje_slice =lenguaje [-2]
print(lenguaje_slice)

reversed_lenguaje =lenguaje[::-1]
print(reversed_lenguaje)

lenguaje_slice =lenguaje [0:6:2]
print(lenguaje_slice)

#funciones
print(lenguaje.capitalize()) #MayusculaPrimera
print(lenguaje.upper()) #toda mayuscula
print(lenguaje.count('t'))#cuenta letras 
print(lenguaje.isnumeric())#pregunta si es numerico
print(lenguaje.lower()) #minuscula
print(lenguaje.upper().isupper()) #2 funciones concatenadas
print(lenguaje.startswith('py'))
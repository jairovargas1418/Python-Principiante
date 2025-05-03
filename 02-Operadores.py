

###Operadores Aritmeticos###
print(3+5) #Suma
print(3-5) #Resta
print(8*2) #Multiplicacion
print(9/3) #Division
print(10%2) #residuo de division
print(10//3) #Aproxima la division a un entero (flor Division)
print(2**3) #Calcular exponente
print('Jairo ' + 'Vargas ') #Concatenar string
print('Hola '+ str(5)) #P str pasa un entero a string
print(3+5*2/1) #Todos los signos se pueden combinar
print('Hola ' * 3) #Se multiplica la palabra Hola

###Operadores Comparativos###
# ≥,≤,!=

print(3>4)
print(2>=2 )
print(3==3)
print(3!=5)
print(3==5)
print(6>=4>2)

#Ordenacion Alfabetica

print('Hola'>'Python')
print('Hola'<'Python')
print('Hola'>='Python')
print('Hola'<='Python')
print('Hola'=='Python')
print('Hola'!='Python')
print(len('aaaa')>=len('aaaa')) #Cuenta caracteres 
print('aaaa'<'AAAA') #Ordenacion Alfabetica por Ascii


###Operadores Logicos###
print(3>4 and 'Hola'>'Python')
print(3>4 or 'Hola'>'Python')
print(not(3>4))



print('Suma: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2


# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

#Ejercicios
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3



#Example: Comparison Operators

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

#Operadores Logicos

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

#Ejercicio
Edad =20
print(Edad)

Peso=75.8
print(Peso)


peso=50
altura=180
imc= peso+altura
print('Indice: ',imc)


sistolica =180 
diastolica =90
tension =sistolica/diastolica
print ('La tension es: ', tension)


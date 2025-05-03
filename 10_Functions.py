###Functions###
def my_function():
    print('Esto es un funcion')
my_function()

def sum_two_values(fist_value,second_value):
    print( fist_value + second_value)
sum_two_values(25874, 325874)
sum_two_values(7, 9)
sum_two_values('1','2') #Concatena cadenas
sum_two_values(1.4,5.2) #Suma 


def sum_two_values_with_return(fist_value,second_value):
    return fist_value + second_value
my_result=sum_two_values_with_return(10,5)
print(my_result)

def print_name(name,surname):
    print(f'{name} {surname}')
print_name (surname='Vargas',name='Jairo')

def print_name_with_default(name,surname,alias='No tiene Alias'): ##Alias valor por defecto
    print(f'{name} {surname} {alias}')
print_name_with_default('Jairo','Vargas','Jairodev') #con parametro alias
print_name_with_default('Jairo','Vargas') #sin parametro alias


def print_texts(*text):  # *sirve para pasar varios parametros (dinamico)
    print(text)
print_texts('Bienvenido','python','Curso para aprender')

def print_upper_text(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_text('Jairo','Vargas','Jairodev') #Pasa a mayusculas

    
    
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function


def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()



###Clases###
class MyEmptyPerson:
    pass
print(MyEmptyPerson())

class Person:
    def __init__(self,name,surname):
        self.full_name =f'{name} {surname}'
        
    
my_Person = Person('jairo','Vargas')
print(my_Person.full_name)


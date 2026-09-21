class AdultException(Exception):
    def printError(self):
        print('Person is Adult.')

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18 :
            raise AdultException()
        else:
            return self.age

    def display(self):
        try:
            print(f'Age : {self.get_minor_age()}')
        except AdultException as e:
            e.printError()
        finally:
            print(f'Name : {self.name}')

x = Person('Abhi',18)
x.display()
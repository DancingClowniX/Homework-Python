import re
class Person:
    def __init__(self, name:str, age:int ,email):
        self.__name = self.validation_name(name)
        self.__age = self.validation_age(age)
        self.__email = email

    @staticmethod
    def validation_age(age):
        if age<18:
            raise 'человек должен быть совершеннолетним'
        if type(age)!= int:
            raise 'возраст должен принимать целочисленное значение'
        return age
    @staticmethod
    def validation_name(name):
        if type(name)!=str:
            raise "имя должно быть строковым значением"

        return name
    @property
    def age(self):
        return self.__age
    @property
    def email(self):
        return self.__email
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @age.setter
    def age(self,age):
        self.__age = age
    @email.setter
    def email(self,email):
        self.__email=email

man = Person("Alex",19,"alex@mail.com")

print(man.name)
print(man.age)
print(man.email)
man.name="sergo"
man.age=21
man.email="sergo@mail.com"
try:
    Person.validation_age(man.age)
    print("Валидный возраст")
except:
    print("Не валидный возраст")
print(man.name)
print(man.age)
print(man.email)
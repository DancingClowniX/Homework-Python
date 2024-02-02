#Создайте базовый класс "Сотрудник" с общими характеристиками (например, имя, зарплата).
#Затем создайте подклассы для различных типов сотрудников, таких как "Менеджер" и "Разработчик",
#добавляя уникальные свойства и методы для каждого типа.
#Реализуйте методы для подсчета общей зарплаты и вычисления премии.

class Employer: #делаем абстрактный класс
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def show_salary(self):
        print(self._salary)

    def show_name(self):
        print(self.name)

class Manager(Employer): #делаем класс Менеджера
    def __init__(self,name,salary):
        super().__init__(name,salary)#Обращаемся к Родительскому классу емплоер
        self.dict = []#Делаем список в который будем вносить подчинённых
        self.__quantity_developers = len(self.dict) #Указываем количество подчиненных = длина списка

    @property #декоратор, будет менять поведение зарплаты, и будет удобно обращаться когда будем расчитывать премию
    def salary(self):
        return self._salary

    @salary.setter #Задаем сеттер для свойств
    def salary(self,salary):
        self._salary = salary
    @property
    def quantity_developers(self):
        return self.__quantity_developers

    @quantity_developers.setter
    def quantity_developers(self):
        self.__quantity_developers = len(self.dict)

    def add_list_developers(self,developer): #Метод добавления разрабов в лист подчинённых
        self.dict.append(developer)
    def show_salary(self): #Полиморфизм переопределение абстрактного метода
        print(self._salary,"salary class Manger")

    def __str__(self): # Маг метод распечатки объекта
        return f"Posititon: manager, Salary: {str(self._salary)}, Name: {self.name}, Quantity developers: {str(len(self.dict))}, List_developers: {self.dict}"

class Developer(Employer): #Дочерний класс наследуется от базового
    def __init__(self,name,salary,id_ticket):
        super().__init__(name,salary)#Обращаемся к родителю
        self.__id_ticket = id_ticket #Задаем атрибут ID
    @property
    def id_ticket(self):
        return self.__id_ticket
    @id_ticket.setter
    def id_ticket(self,id):
        self.__id_ticket = id

    def show_salary(self):#Полиморфизм переопределение абстрактного метода
        print(self._salary,"salary class Developer")

    def __str__(self):
        return f"Posititon: Developer, Salary: {str(self._salary)}, Name: {self.name}, Id: {self.__id_ticket}"
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        self._salary = salary
class Premial: # новый класс, в котором мы рассчитаем премию
    def __init__(self):
        self.dict_premial = [] #Задаем список зарплат
    def sum_premial_salary(self,*argument): # здесь мы высчитываем премию в 40% от зарплаты
        for i in argument:
            count = i*0.4+i
            self.dict_premial.append(count)
        print(sum(self.dict_premial))


#Задаем экземпляр абстракции
employers = Employer("R",0)
#Задаем экземпляр менеджера
employer1 = Manager("Coco",1000)
print(employer1)
#Проверка полиморфизма
employer1.show_salary()
#Задаем экземпляр разрабов 2 шт
employer2 = Developer("Sasha",500,3452)
employer3 = Developer("Vanya",760,3453)
#Добавляем в список подчинённых
employer1.add_list_developers(str(employer2))
employer1.add_list_developers(str(employer3))
print(employer1)
#Проверка полиморфизма
employer2.show_salary()
print(employer2)
#задаем экземпляр премии
premia = Premial()
#Выполняем метод по вычислении общей премии
premia.sum_premial_salary(employer1.salary, employer2.salary, employer3.salary)



import random
class Student:
    def __init__(self,name):
        self.name = name
        self.dict_course = {}
        self.score = []
        self.id_number = random.choice(range(1000,9999))
    def add_course(self,course):
        list_course = ["Русский язык", "Математика", "Программирование", "Астрономия", "Политология", "Риторика"]
        for item in list_course:
            if item == course:
                self.dict_course[f'{course}'] = ''
                print(f"Курс: {self.dict_course} добавлен к {self.name}")

    def remove_course(self,course):
        for item in self.dict_course:
            if item == course:
                self.dict_course.pop(course)
                print(f"Курс: {course} удалён у {self.name}")
            break

    def add_score(self,point_score,course):
        self.score.append(point_score)
        self.dict_course[f'{course}'] = point_score
        print(f"К {self.name} в предмете: {course}, проставлена оценка {point_score}")

    def show_info(self):
        print(f"Name: {self.name},Courses and score: {self.dict_course}, id:{self.id_number}")

    def average_score(self):
        for i in self.score:
            if type(i) == int:
                average = sum(self.score)/len(self.score)
                print(average)
            else:
                print("Ошибка")


    def __str__(self):
        return f'{self.name},{self.id_number}'

#def createStudent():
 #   students = []
    #while True:
      #  stop = input('Хотите добавить студента? \nвведите д или н\n')
      #  if stop.lower() == 'д':
     #       break
    #name_student = input('Введите имя Студента: ')
    #id_student = input('Введите номер студенческого билета: ')
   # student = Student(name_student, id_student)
    #student.add_course(input("Введите курс: Русский язык\nМатематика\nПрограммирование\nАстрономия\nПолитология\nРиторика\n"))
  #  students.append(student)
 #   return students


#createStudent()
#
# stud = Student("Kevin")
# stud.add_course("Русский язык")
# #stud.remove_course("Русский язык")
# stud.add_score(5,"Русский язык")
# stud.add_score(5,"Русский язык")
# #stud.add_score(3,"Программирование")
# #stud.show_info()
# stud.average_score()

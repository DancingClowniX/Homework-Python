from student import Student
from course import Course
from teacher import Teacher

class School:
    def __init__(self):
        self.list_students = []
        self.list_teachers = []
        self.list_courses = ["Русский язык", "Математика", "Программирование", "Астрономия", "Политология", "Риторика"]
        self.dict_students_id = []

    def add_students(self, student):
        if self.list_students.count(student):
            print("он уже есть")
        else:
            self.list_students.append(student)
    def add_teachers(self, teacher):
        if self.list_teachers.count(teacher):
            print("он уже принят")
        else:
            self.list_teachers.append(teacher)

    def __repr__(self):
        return f"{self.list_teachers}"


    # ------------------------------- Создание Школы ----------------------------#
school = School()
count = 1
def line():
    print("------------------------------------------------------------------------")
while True:
    command_school = input("""
1. Интерфейс Директора
2. Интерфейс Преподавателя
3. Интерфейс Студента
4. Выйти из программы
""")
    if command_school == "1":
        line()
        while True:
            admin = input("""
1. Авторизация Директора
2. Вернуться назад 
""")
            if admin == "1":
                password = input(" Введите пароль: ")
                if password == "makarova":
                    while True:
                        command_director = input("""
1. Показать доступные курсы
2. Принять преподавателя
3. Уволить преподавателя
4. Зачислить студента
5. Отчислить студента
6. Показать список студентов
7. Показать список перподавателей
8. Поиск студентов по номеру билета
9. Вернуться назад
""")
#----------------------------------------------------Блок №1 Интерфейс Директора---------------------------------------#
                        if command_director == "1":
                            line()
                            print(school.list_courses)
                        elif command_director == "2":
                            line()
                            director_name_teacher = input("Введите имя и фамилию преподавателя: ")
                            if len(director_name_teacher) != 0:
                                if type(director_name_teacher) == str:
                                    teacher = Teacher(director_name_teacher)
                                    school.list_teachers.append(teacher)
                                    print(f'{teacher.name_teacher} принят на работу')
                                    continue
                                elif director_name_teacher.isdigit() or director_name_teacher.isspace() or director_name_teacher.isalnum():
                                    print("Введите правильно")
                            else:
                                print("Ошибка")
                        elif command_director == "3":
                            line()
                            remove_teacher = input("Введите имя и фамилию увольняемого преподавателя: ")
                            for i in school.list_teachers:
                                if remove_teacher == i.name_teacher:
                                    school.list_teachers.remove(i)
                                    print(f"{i} уволен с работы")
                                    del i
                            continue
                        elif command_director == "4":
                            line()
                            director_name_student = input("Введите имя и фамилию студента: ")
                            if len(director_name_student) != 0:
                                if type(director_name_student) == str:
                                    student = Student(director_name_student)
                                    student_id = student.id_number
                                    print(f"Студент {student.name},с номером {student_id} зачислен в школу")
                                    school.list_students.append(student)
                                    school.dict_students_id.append(int(student_id))
                                    continue
                                elif director_name_student.isdigit() or director_name_student.isspace() or director_name_student.isalnum():
                                    print("Введите правильно")
                            else:
                                print("Ошибка")
                        elif command_director == "5":
                            line()
                            remove_student = input("Введите имя и фамилию студента: ")
                            for i in school.list_students:
                                if remove_student == i.name:
                                    school.list_students.remove(i)
                                    print(f"{i} отчислен")
                                    del i
                            continue
                        elif command_director == "6":
                            line()
                            for i in school.list_students:
                                print(f"{i}")
                            continue
                        elif command_director == "7":
                            line()
                            for i in school.list_teachers:
                                print(f"{i}")
                            continue
                        elif command_director == "8":
                            line()
                            search_id = int(input("Введите номер студенческого билета: "))
                            for i in school.list_students:
                                if search_id == i.id_number:
                                    print(i.name)
                        elif command_director == "9":
                            line()
                            break
                        else:
                            line()
                            print("Ошибка")
                            break
            elif admin == "2":
                break
            else:
                print("Ошибка")
#----------------------------------------------------Блок №2 Интерфейс Препода---------------------------------------#
    elif command_school == "2":
        line()
        while True:
            admin1 = input("""
1. Авторизация Преподавателя
2. Вернуться назад
""")
            if admin1 == "1":
                line()
                password1 = input("Введите пароль: ")
                if password1 == "makarova":
                    valid_teacher = input("введите имя и фамилию: ")
                    for i in school.list_teachers:
                        if valid_teacher == i.name_teacher:
                            print(i.name_teacher)
                            if len(valid_teacher) != 0:
                                while True:
                                    command_teacher = input("""
1. Показать доступные курсы и взять курс
2. Отказаться от курса
3. Выставить оценку студенту
4. Показать курсы которые вы ведёте
5. Вернуться назад
""")
                                    if command_teacher == "1":
                                        list_course = input(f"""
1.{school.list_courses[0]}
2.{school.list_courses[1]}
3.{school.list_courses[2]}
4.{school.list_courses[3]}
5.{school.list_courses[4]}
6.{school.list_courses[5]}
7.Вернуться назад
""")
                                        if list_course == "1":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[0])
                                                    course = Course(school.list_courses[0],i.name_teacher)
                                                    continue
                                        elif list_course == "2":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[1])
                                                    course = Course(school.list_courses[1], i.name_teacher)
                                                    continue
                                        elif list_course == "3":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[2])
                                                    course = Course(school.list_courses[2], i.name_teacher)
                                                    continue
                                        elif list_course == "4":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[3])
                                                    course = Course(school.list_courses[3], i.name_teacher)
                                                    continue
                                        elif list_course == "5":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[4])
                                                    course = Course(school.list_courses[4], i.name_teacher)
                                                    continue
                                        elif list_course == "6":
                                            for i in school.list_teachers:
                                                if valid_teacher == i.name_teacher:
                                                    i.add_course(school.list_courses[5])
                                                    course = Course(school.list_courses[5], i.name_teacher)
                                                    continue
                                        elif list_course == "7":
                                            break
                                        else:
                                            print("Ошибка")
                                    elif command_teacher == "2":
                                        print(school.list_courses)
                                        remove_list_course = input(f"Введите курс от которого хотите отказаться: ")
                                        for valid_teacher in school.list_teachers:
                                            if remove_list_course in valid_teacher.title_teacher:
                                                valid_teacher.title_teacher.remove(remove_list_course)
                                                print(valid_teacher.title_teacher)
                                    elif command_teacher == "3":
                                        command_score = input(f"""
1.Выставить оценку по предмету {school.list_courses[0]}
2.Выставить оценку по предмету {school.list_courses[1]}
3.Выставить оценку по предмету {school.list_courses[2]}
4.Выставить оценку по предмету {school.list_courses[3]}
5.Выставить оценку по предмету {school.list_courses[4]}
6.Выставить оценку по предмету {school.list_courses[5]}
7.Вернуться назад
""")
                                        if command_score == "1":
                                            student_name_score = str(input("Введите имя студента : "))
                                            for i in school.list_students:
                                                if student_name_score == i.name:
                                                    for teach in school.list_teachers:
                                                        if teach.name_teacher == valid_teacher:
                                                            score = int(input("Введите оценку: "))
                                                            teach.students_list.append(i.name)
                                                            teach.add_score_for_students(i.name,score)
                                                            i.add_score(score,school.list_courses[0])
                                                            print(f"{i.dict_course}")
                                                            print(f"{teach.score_title}")
                                                        else:
                                                            print("Ошибка")
                                            if command_score == "2":
                                                student_name_score = str(input("Введите имя студента : "))
                                                for i in school.list_students:
                                                    if student_name_score == i.name:
                                                        for teach in school.list_teachers:
                                                            if teach.name_teacher == valid_teacher:
                                                                score = int(input("Введите оценку: "))
                                                                teach.students_list.append(i.name)
                                                                teach.add_score_for_students(i.name, score)
                                                                i.add_score(score, school.list_courses[1])
                                                                print(f"{i.dict_course}")
                                                                print(f"{teach.score_title}")
                                                            else:
                                                                print("Ошибка")
                                            if command_score == "3":
                                                student_name_score = str(input("Введите имя студента : "))
                                                for i in school.list_students:
                                                    if student_name_score == i.name:
                                                        for teach in school.list_teachers:
                                                            if teach.name_teacher == valid_teacher:
                                                                score = int(input("Введите оценку: "))
                                                                teach.students_list.append(i.name)
                                                                teach.add_score_for_students(i.name, score)
                                                                i.add_score(score, school.list_courses[2])
                                                                print(f"{i.dict_course}")
                                                                print(f"{teach.score_title}")
                                                            else:
                                                                print("Ошибка")
                                            if command_score == "4":
                                                student_name_score = str(input("Введите имя студента : "))
                                                for i in school.list_students:
                                                    if student_name_score == i.name:
                                                        for teach in school.list_teachers:
                                                            if teach.name_teacher == valid_teacher:
                                                                score = int(input("Введите оценку: "))
                                                                teach.students_list.append(i.name)
                                                                teach.add_score_for_students(i.name, score)
                                                                i.add_score(score, school.list_courses[3])
                                                                print(f"{i.dict_course}")
                                                                print(f"{teach.score_title}")
                                                            else:
                                                                print("Ошибка")
                                            if command_score == "5":
                                                student_name_score = str(input("Введите имя студента : "))
                                                for i in school.list_students:
                                                    if student_name_score == i.name:
                                                        for teach in school.list_teachers:
                                                            if teach.name_teacher == valid_teacher:
                                                                score = int(input("Введите оценку: "))
                                                                teach.students_list.append(i.name)
                                                                teach.add_score_for_students(i.name, score)
                                                                i.add_score(score, school.list_courses[4])
                                                                print(f"{i.dict_course}")
                                                                print(f"{teach.score_title}")
                                                            else:
                                                                print("Ошибка")
                                            if command_score == "6":
                                                student_name_score = str(input("Введите имя студента : "))
                                                for i in school.list_students:
                                                    if student_name_score == i.name:
                                                        for teach in school.list_teachers:
                                                            if teach.name_teacher == valid_teacher:
                                                                score = int(input("Введите оценку: "))
                                                                teach.students_list.append(i.name)
                                                                teach.add_score_for_students(i.name, score)
                                                                i.add_score(score, school.list_courses[5])
                                                                print(f"{i.dict_course}")
                                                                print(f"{teach.score_title}")
                                                            else:
                                                                print("Ошибка")
                                            if command_score == "7":
                                                break
                                            else:
                                                print("Такого студента на вашем курсе нет")
                                    elif command_teacher == "4":
                                        for i in school.list_teachers:
                                            if valid_teacher == i.name_teacher:
                                                print(i.title_teacher)
                                                break
                                            else:
                                                print("У вас нет предмета который вы ведёте")
                                        continue
                                    elif command_teacher == "5":
                                        break
                            elif valid_teacher.isdigit() or valid_teacher.isspace() or valid_teacher.isalnum():
                                print("Введите правильно")
                                break
                            else:
                                print("ошибка")
                                break
                        else:
                            print("Вас ещё не наняли")
            elif admin1 == "2":
                break
            else:
                print("Ошибка")
#----------------------------------------------------Блок №3 Интерфейс Cтудента---------------------------------------#
    elif command_school == "3":
        name_student = input("Введите ваше имя: ")
        #print(type(school.list_students[0]))
        for i in school.list_students:
            if name_student == i.name:
                if i in school.list_students:
                    while True:
                        command_student = input("""
1. Показать ваш номер студенческого билета
2. Показать доступные курсы и взять курс
3. Отказаться от курса
4. Рассчитать средний балл
5. Показать курсы которые вы взяли
6. Вернуться назад
""")
                        if command_student == "1":
                            for i in school.list_students:
                                if name_student == i.name:
                                    print(i.id_number)
                        elif command_student == "2":
                            while True:
                                list_student_course = input(f"""
1.{school.list_courses[0]}
2.{school.list_courses[1]}
3.{school.list_courses[2]}
4.{school.list_courses[3]}
5.{school.list_courses[4]}
6.{school.list_courses[5]}
7.Вернуться назад
""")
                                if list_student_course == "1":
                                    for i in school.list_students:
                                        if name_student == i.name:
                                            i.dict_course[f"{school.list_courses[0]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "2":
                                    for i in school.list_students:
                                        if name_student == i:
                                            i.dict_course[f"{school.list_courses[1]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "3":
                                    for i in school.list_students:
                                        if name_student == i:
                                            i.dict_course[f"{school.list_courses[2]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "4":
                                    for i in school.list_students:
                                        if name_student == i:
                                            i.dict_course[f"{school.list_courses[3]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "5":
                                    for i in school.list_students:
                                        if name_student == i:
                                            i.dict_course[f"{school.list_courses[4]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "6":
                                    for i in school.list_students:
                                        if name_student == i:
                                            i.dict_course[f"{school.list_courses[5]}"] = ""
                                            print(i.dict_course)
                                if list_student_course == "7":
                                    break
                                else:
                                    break
                        elif command_student == "3":
                            course_student_remove = input("Введите курс от которого вы хотите отказаться: ")
                            for i in school.list_students:
                                if name_student == i.name:
                                    if course_student_remove in i.dict_course:
                                        for course_student_remove in i.dict_course:
                                            i.dict_course.pop(f"{course_student_remove}")
                                            print("Предмет удалён из вашего списка")
                                            break
                        elif command_student == "4":
                            for i in school.list_students:
                                if name_student == i.name:
                                    print(i.average_score())
                        elif command_student == "5":
                            for i in school.list_students:
                                if name_student == i.name:
                                    print(f"{i.dict_course}")
                        elif command_student == "6":
                            break

        else:
            print("Вас ещё не зачислили")
    elif command_school == "4":
        break
    else:
        print("ошибка")
class Teacher:
    def __init__(self,name_teacher):
        self.name_teacher = name_teacher
        self.title_teacher = []
        self.students_list = []
        self.score_title = {}

    def add_course(self, add_title):
        if self.title_teacher.count(add_title):
            print(f"Преподаватель, {self.name_teacher} уже взял этот курс")
        else:
            self.title_teacher.append(add_title)
            print(f"Вы {self.name_teacher} взяли вести курс {self.title_teacher}")

    def remove_course(self, remove_title):
        if self.title_teacher.count(remove_title):
            self.title_teacher.remove(remove_title)
            print(f"Преподаватель {self.name_teacher} больше не ведёт курс {remove_title}")
        else:
            print(f"Такого курса у преподавателя {self.name_teacher} нет")
    def add_score_for_students(self,name_students,score):
        if self.students_list.count(name_students):
            self.score_title[f"{name_students}"] = score
    def __str__(self):
        return f'{self.name_teacher}'


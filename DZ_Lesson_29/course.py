#from student import Student
#from student import createStudent
# передается список [students]?
class Course:
    def __init__(self,title,teacher):
        self.title = title
        self.teacher = teacher
        self.list_student = []
        self.score_course_student = {}

    def add_student(self, name):
        if self.list_student.count(name):
            print(f"Студент, {name} уже присутствует в списке")
        else:
            self.list_student.append(name)
            print(f"Студент {name}, добавлен в список")

    def remove_student(self,name):
        for i in self.list_student:
            if i == name:
                self.list_student.remove(name)

    def add_score(self, point_score, name_student):
        if self.list_student.count(name_student):
            self.score_course_student[f"{name_student}"] = point_score
    def show_students(self):
        print(self.list_student)

#course = Course ("Русский язык","Иван")
#course.add_student("Kevin")
#print(course.list_student)
#course.add_score(5,"Kevin")
#print(course.score_course_student)
#course.show_students()
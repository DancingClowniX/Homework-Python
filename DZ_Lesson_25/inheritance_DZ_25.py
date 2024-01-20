class Task:
    def __init__(self):
         self.__title = 'Код ревью'
         self.__status = 'не назначена'

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status
    def display_info(self):
        print(f'Название задачи: {self.__title}, Статус: {self.__status}.')

class Asingnee(Task):
    def __init__(self, name):
        super().__init__()
        self.__name = name
    def asingnee_task(self, status):
        self.status = status
    def display_info(self):
        super().display_info()
        print(f'Name: {self.__name}')

task1 = Task()
task1.display_info()

employer = Asingnee('kevin')
employer.asingnee_task('назначена') #asingnee.status = 'взял'
employer.display_info()

#
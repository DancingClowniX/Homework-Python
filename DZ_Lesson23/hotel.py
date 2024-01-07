# по условию каждый месяц кратный 2 недоступен для брони
import re
class Hotel:
    def __init__(self,guest,date_start,date_end,type_room):
        self.guest = guest
        self.date_start = date_start
        self.date_end = date_end
        self.type_room = type_room
    def show_reservation(self):
        print(f"{self.guest},{self.date_start},{self.date_end},{self.type_room} номер забронирован")
    def __del__(self):
        print(f"{self.guest},{self.date_start},{self.date_end},{self.type_room} номер аннулирован")
        del self
while True:
    command = input('''
    1. Забронировать номер
    2. Выход
    3. отменить бронь
    4. показать бронь
     ''')
    if command == "1":
        command_reservations = input('''
        1. Дата заезда
        2. Выход
        ''')
        if command_reservations == "1":
            date_start = input("введите дату заезда чч.мм.гг : ")
            dict = (re.findall(r'\d\d',date_start))
            if int(dict[1]) % 2 == 0:
                print("Месяц недоступен для брони")
                break
            else:
                date_end = input("введите дату выезда: ")
                dict1 = (re.findall(r'\d\d', date_end))
                if int(dict1[1]) % 2 == 0:
                    print("Месяц недоступен для брони")
                    break
                else:
                    guest1 = input("введите имя: ")
                    type_room = input('''выберите тип номера
                    1. люкс
                    2. эконом ''')
                    if type_room == "1":
                        type_room = "люкс"
                        guest_people = Hotel (guest1,date_start,date_end,type_room)
                        print("забронирован")
                        #guest_people.show_reservation()
                        continue
                    elif type_room == "2":
                        type_room = "'эконом"
                        guest_people = Hotel(guest1, date_start, date_end, type_room)
                        print("забронирован")
                        #guest_people.show_reservation()
                        continue
                    else:
                        print("данные введены некорректно")
    elif command == "2":
        break
    elif command == "3":
        del guest_people
        continue
    elif command == "4":
        guest_people.show_reservation()
        continue
    else:
        print("Комманда введена некорректно")
        break

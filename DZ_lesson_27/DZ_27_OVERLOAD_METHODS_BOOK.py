class Book:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year
    def __eq__(self, other_book):
        if self.year > other_book.year:
            print(f"{self.name}: выпущена позже чем {other_book.name}")
        elif self.year < other_book.year:
            print(f"{other_book.name}: выпущена позже чем {self.name} ")
        elif self.year == other_book.year:
            print('книги выпущены в один год')

book1 = Book("Над пропастью во ржи",1951)
book2 = Book("Приключения Тома Сойера", 1876)
print(book1.__eq__(book2))
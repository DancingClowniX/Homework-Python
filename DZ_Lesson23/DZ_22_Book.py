class Book:
    def __init__(self,autor,name,genre):
        self.autor = autor
        self.name = name
        self.genre = genre
    def show_book(self):
        print(f'{self.autor},{self.name},{self.genre}')

autor1 = input("введите автора ")
name1 = input("введите название книги ")
genre1 = input("введите жанр книги ")

my_book = Book(autor1,name1,genre1)
my_book.show_book()
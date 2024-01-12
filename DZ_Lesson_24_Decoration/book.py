dict_genre = ["проза","фантастика","драма"]
class Book:
    def __init__(self, autor, title, genre):
        self.__autor = autor
        self.__genre = self.validate(genre)
        self.__title = title

    @staticmethod
    def validate(genre):
        if genre in dict_genre:
            if len(genre)>0:
                print("valid")
                return genre
            else:
                print("invalid")

        else:
            print("invalid")


    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self,autor):
        self.__autor = autor
    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self,genre):
        self.__genre = genre
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,title):
        self.__title = title
    def show(self):
        print(f'{self.__autor},{self.__title},{self.__genre}')

book = Book('Nick Jhonson','People of classic','фантастика')
print(book.show())

book.title = 'History of magic'
book.genre = "проза"
book.autor = 'Arman Zhurtanov'
print(book.show())

# TODO: написать класс Book
# TODO: написать класс Library

class Book:
    def __init__(self, id_, name, pages):
        """
        Инициализация атрибутов книги.
        :param id_: int - идентификатор книги
        :param name: str - название книги
        :param pages: int - количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление объекта для пользователя.
        Формат: Книга "название_книги".
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, по которой можно инициализировать идентичный объект.
        Формат: Book(id_=1, name='название', pages=100).
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books=None):
        """
        Инициализация атрибутов библиотеки.
        :param books: list - список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор книги для добавления в библиотеку.
        :return: int - следующий id книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по её id.
        :param book_id: int - идентификатор книги.
        :return: int - индекс книги в списке.
        :raises ValueError: если книги с данным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# База данных книг
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == "__main__":
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library = Library(list_books)

    for book in library.books:
        print(book)  # Проверяем метод __str__

    print(library.books)  # Проверяем метод __repr__

    # Проверяем метод get_next_book_id
    print("Следующий ID книги:", library.get_next_book_id())

    # Проверяем метод get_index_by_book_id
    try:
        print("Индекс книги с ID 1:", library.get_index_by_book_id(1))
    except ValueError as e:
        print(e)

    try:
        print("Индекс книги с ID 3:", library.get_index_by_book_id(3))
    except ValueError as e:
        print(e)

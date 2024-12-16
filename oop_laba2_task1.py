
# TODO: написать класс Book

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
    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__

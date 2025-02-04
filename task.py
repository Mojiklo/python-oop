# TODO: описать базовый класс
class Animal:
    """
    Базовый класс для всех животных.

    Атрибуты:
        name (str): Имя животного.
        species (str): Вид животного.
        age (int): Возраст животного.
    """
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self) -> str:
        """Метод для издания звука. Возвращает общий звук."""
        return "Какой-то звук"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.species.capitalize()} по имени {self.name}, возраст: {self.age} год(а/лет)"

    def __repr__(self) -> str:
        """Возвращает строку для создания объекта."""
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r}, age={self.age!r})"


class Dog(Animal):
    """
    Класс для собак. Наследуется от Animal.

    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (str): Порода собаки.
    """
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, "собака", age)  # Используем конструктор базового класса Animal
        self.breed = breed

    def make_sound(self) -> str:
        """Переопределённый метод для издания звука. Собака лает."""
        return "Гав-гав"

    def fetch(self, item: str) -> str:
        """Метод для команды 'апорт'. Собака приносит предмет."""
        return f"{self.name} принес(ла) {item}!"

    def __str__(self) -> str:
        """Расширяем метод __str__, добавляя информацию о породе."""
        return f"{super().__str__()}, порода: {self.breed}"


class Bird(Animal):
    """
    Класс для птиц. Наследуется от Animal.

    Атрибуты:
        name (str): Имя птицы.
        age (int): Возраст птицы.
        can_fly (bool): Может ли птица летать.
    """
    def __init__(self, name: str, age: int, can_fly: bool = True):
        super().__init__(name, "птица", age)
        self.can_fly = can_fly

    def make_sound(self) -> str:
        """Переопределённый метод. Птица издает чирикающий звук."""
        return "Чирик-чирик"

    def fly(self) -> str:
        """Метод для полёта. Проверяет, может ли птица летать."""
        if self.can_fly:
            return f"{self.name} летит!"
        return f"{self.name} не может летать."

    def __str__(self) -> str:
        """Расширяем метод __str__, добавляя информацию о способности летать."""
        flight_ability = "может летать" if self.can_fly else "не может летать"
        return f"{super().__str__()}, {flight_ability}"


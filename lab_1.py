import doctest

class AbstractEntity:
    def __init__(self, identifier: int, name: str):
        """
        Создание и подготовка к работе абстрактного объекта.
        >>> entity = AbstractEntity(1, "Object1")  # инициализация экземпляра класса
        """
        if not isinstance(identifier, int):
            raise TypeError("Идентификатор должен быть типа int")
        if identifier <= 0:
            raise ValueError("Идентификатор должен быть положительным числом")
        self.identifier = identifier

        if not isinstance(name, str):
            raise TypeError("Имя объекта должно быть типа str")
        if not name:
            raise ValueError("Имя объекта не может быть пустым")
        self.name = name

    def get_description(self) -> str:
        """
        Получение описания объекта.
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.get_description()
        'This is an abstract entity with ID 1 and name Object1.'
        """
        return f"This is an abstract entity with ID {self.identifier} and name {self.name}."

    def update_name(self, new_name: str) -> None:
        """
        Обновление имени объекта.
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.update_name("NewObject")
        >>> entity.name
        'NewObject'
        """
        if not new_name:
            raise ValueError("Новое имя не может быть пустым")
        self.name = new_name

    def generate_report(self) -> str:
        """
        Генерация отчета о состоянии объекта.
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.generate_report()
        'Отчет: Объект с ID 1 и именем Object1.'
        """
        return f"Отчет: Объект с ID {self.identifier} и именем {self.name}."


class PhysicalObject(AbstractEntity):
    def __init__(self, identifier: int, name: str, weight: float):
        """
        Создание и подготовка к работе физического объекта.
        >>> physical_object = PhysicalObject(2, "Box", 10.5)
        """
        super().__init__(identifier, name)

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес объекта должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес объекта должен быть положительным числом")
        self.weight = weight

    def move_object(self, destination: str) -> str:
        """
        Перемещение физического объекта.
        >>> physical_object = PhysicalObject(2, "Box", 10.5)
        >>> physical_object.move_object("Storage Room")
        'Объект Box перемещен в Storage Room.'
        """
        if not destination:
            raise ValueError("Место назначения не может быть пустым")
        return f"Объект {self.name} перемещен в {destination}."

    def measure_weight(self) -> float:
        """
        Измерение веса физического объекта.
        >>> physical_object = PhysicalObject(2, "Box", 10.5)
        >>> physical_object.measure_weight()
        10.5
        """
        return self.weight


class DigitalEntity(AbstractEntity):
    def __init__(self, identifier: int, name: str, version: str):
        """
        Создание и подготовка к работе цифрового объекта.
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")
        """
        super().__init__(identifier, name)

        if not isinstance(version, str):
            raise TypeError("Версия цифрового объекта должна быть типа str")
        self.version = version

    def update_version(self, new_version: str) -> None:
        """
        Обновление версии цифрового объекта.
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")
        >>> digital_entity.update_version("v2.0")
        >>> digital_entity.version
        'v2.0'
        """
        if not new_version:
            raise ValueError("Новая версия не может быть пустой")
        self.version = new_version

    def run_application(self) -> str:
        """
        Запуск цифрового приложения.
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")
        >>> digital_entity.run_application()
        'Запуск приложения Software версии v1.0...'
        """
        return f"Запуск приложения {self.name} версии {self.version}..."


if __name__ == "__main__":
    doctest.testmod()

import doctest


class AbstractEntity:
    def __init__(self, identifier: int, name: str):
        """
        Создание и подготовка к работе абстрактного объекта.
        
        :param identifier: Уникальный идентификатор объекта
        :param name: Имя объекта
        
        Примеры:
        >>> entity = AbstractEntity(1, "Object1")  # инициализация экземпляра класса
        """
        if not isinstance(identifier, int):
            raise TypeError("Идентификатор должен быть типа int")
        if identifier <= 0:
            raise ValueError("Идентификатор должен быть положительным числом")
        self.identifier = identifier

        if not isinstance(name, str):
            raise TypeError("Имя объекта должно быть типа str")
        self.name = name

    def get_description(self) -> str:
        """
        Получение описания объекта.
        
        :return: Описание объекта
        
        Примеры:
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.get_description()
        'This is an abstract entity with ID 1 and name Object1.'
        """
        ...

    def update_name(self, new_name: str) -> None:
        """
        Обновление имени объекта.
        
        :param new_name: Новое имя объекта
        :raise ValueError: Если новое имя объекта пустое, вызываем ошибку
        
        Примеры:
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.update_name("NewObject")
        """
        ...

    def generate_report(self) -> None:
        """
        Генерация отчета о состоянии объекта.
        
        Примеры:
        >>> entity = AbstractEntity(1, "Object1")
        >>> entity.generate_report()
        """
        ...


class PhysicalObject(AbstractEntity):
    def __init__(self, identifier: int, name: str, weight: float):
        """
        Создание и подготовка к работе физического объекта.
        
        :param identifier: Уникальный идентификатор объекта
        :param name: Имя объекта
        :param weight: Вес объекта
        
        Примеры:
        >>> physical_object = PhysicalObject(2, "Box", 10.5)  # инициализация экземпляра класса
        """
        super().__init__(identifier, name)

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес объекта должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес объекта должен быть положительным числом")
        self.weight = weight

    def move_object(self, destination: str) -> None:
        """
        Перемещение физического объекта.
        
        :param destination: Место, куда перемещается объект
        :raise ValueError: Если место назначения пустое, вызываем ошибку
        
        Примеры:
        >>> physical_object = PhysicalObject(2, "Box", 10.5)
        >>> physical_object.move_object("Storage Room")
        """
        ...

    def measure_weight(self) -> float:
        """
        Измерение веса физического объекта.
        
        :return: Вес объекта
        
        Примеры:
        >>> physical_object = PhysicalObject(2, "Box", 10.5)
        >>> physical_object.measure_weight()
        10.5
        """
        ...


class DigitalEntity(AbstractEntity):
    def __init__(self, identifier: int, name: str, version: str):
        """
        Создание и подготовка к работе цифрового объекта.
        
        :param identifier: Уникальный идентификатор объекта
        :param name: Имя объекта
        :param version: Версия цифрового объекта
        
        Примеры:
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")  # инициализация экземпляра класса
        """
        super().__init__(identifier, name)

        if not isinstance(version, str):
            raise TypeError("Версия цифрового объекта должна быть типа str")
        self.version = version

    def update_version(self, new_version: str) -> None:
        """
        Обновление версии цифрового объекта.
        
        :param new_version: Новая версия объекта
        :raise ValueError: Если новая версия объекта пуста, вызываем ошибку
        
        Примеры:
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")
        >>> digital_entity.update_version("v2.0")
        """
        ...

    def run_application(self) -> None:
        """
        Запуск цифрового приложения.
        
        Примеры:
        >>> digital_entity = DigitalEntity(3, "Software", "v1.0")
        >>> digital_entity.run_application()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

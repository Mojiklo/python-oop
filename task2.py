from task_1 import AbstractEntity, PhysicalObject, DigitalEntity

# Проверка создания объектов с неверными типами и значениями
def test_invalid_inputs():
    print("Проверка создания AbstractEntity с неверными данными:")
    try:
        AbstractEntity("один", "Entity1")  # Неверный тип ID
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        AbstractEntity(-1, "Entity1")  # Отрицательный ID
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        AbstractEntity(1, "")  # Пустое имя
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПроверка создания PhysicalObject с неверным весом:")
    try:
        PhysicalObject(4, "Box", "тяжёлый")  # Неверный тип веса
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        PhysicalObject(4, "Box", 0)  # Нулевой вес
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПроверка создания DigitalEntity с неверной версией:")
    try:
        DigitalEntity(5, "App", 1.0)  # Неверный тип версии
    except TypeError as e:
        print(f"Ошибка: {e}")

# Основная проверка корректной работы методов
def main():
    print("Проверка класса AbstractEntity:")
    try:
        entity = AbstractEntity(1, "Entity1")
        print(entity.get_description())
        entity.update_name("UpdatedEntity")
        print(entity.get_description())

        print("Проверка некорректного имени:")
        entity.update_name("")  # Должно вызвать исключение
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПроверка класса PhysicalObject:")
    try:
        obj = PhysicalObject(2, "Box", 10.5)
        print(f"Вес объекта: {obj.measure_weight()}")
        print(obj.move_object("Storage Room"))

        print("Проверка некорректного места назначения:")
        print(obj.move_object(""))  # Должно вызвать исключение
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПроверка класса DigitalEntity:")
    try:
        digital = DigitalEntity(3, "App", "v1.0")
        print(f"Текущая версия: {digital.version}")
        print(digital.run_application())

        digital.update_version("v2.0")
        print(f"Обновленная версия: {digital.version}")

        print("Проверка некорректной версии:")
        digital.update_version("")  # Должно вызвать исключение
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    test_invalid_inputs()
    print("\n" + "=" * 50 + "\n")
    main()

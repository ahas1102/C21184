class InvalidAgeError(Exception):
    pass


class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def set_age(self, age):
        """Устанавливаем возраст. Если возраст некорректный, выбрасываем исключение"""
        if age < 0 or age > 200:
            raise InvalidAgeError("Возраст должен быть в пределах от 0 до 120 лет!")
        self.age = age


try:
    person = Person("Володимер")
    person.set_age(150)
except InvalidAgeError as e:
    print("Ошибка:", e)


person.set_age(36)
print(f"Возраст установлен: {person.age}")
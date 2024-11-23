class Character:
    def __init__(self, health, name , attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return f"{self.name} атакує з силою {self.attack_power} урона!"

class Game:
    def __init__(self):
        self.team = []

    def create_character(self):
        name = input("Введіть ім'я персонажа: ")
        health = int(input("Введіть здоров'я: "))
        attack_power = int(input("Введіть силу атаки: "))
        character = Character(name, health, attack_power)
        self.team.append(character)
        print(f"Персонаж {name} створений!")

    def view_team(self):
        if not self.team:
            print("Команда пуста!")
            return
        for character in self.team:
            print(f"{character.name} - Здоров'я: {character.health}, Атака: {character.attack_power}")

    def attack(self):
        name = input("Введіть ім'я персонажа для атаки: ")
        character = self.get_character_by_name(name)
        if character:
            print(character.attack())
        else:
            print(f"Персонажа з ім'ям {name} не знайдено!")

    def get_character_by_name(self, name):
        for character in self.team:
            if character.name == name:
                return character
        return None

    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Створити персонажа")
            print("2. Переглянути команду")
            print("3. Атака")
            print("4. Вихід")
            choice = input("Виберіть дію: ")

            if choice == "1":
                self.create_character()
            elif choice == "2":
                self.view_team()
            elif choice == "3":
                self.attack()
            elif choice == "4":
                print("Вихід з гри...")
                break
            else:
                print("Невірний вибір!")


if __name__ == "__main__":
    game = Game()
    game.menu()

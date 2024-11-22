class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Character's name is {self.name}")


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []  # Інвентар у гравця

    def introduce(self):
        print(f"Player's name is {self.name}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory")

    def show_inventory(self):
        for item in self.inventory:
            print(item)



def health_manager(initial_health):
    health = initial_health

    def manage_health(amount=None):
        nonlocal health
        if amount is not None:
            health += amount
        return health

    return manage_health



def find_item(inventory, item_name):
    for item in inventory:
        if item_name.lower() in item.lower():
            yield item
    yield "Item not found"



def special_ability(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_uses_left'):
            self._uses_left = 3
        if self._uses_left > 0:
            self._uses_left -= 1
            return func(self, *args, **kwargs)
        else:
            print(f"{self.name} has no uses left for the special ability!")

    return wrapper


# 5. Приклад використання
player = Player("John")
player.introduce()


player.add_item("Sword")
player.add_item("Shield")
player.add_item("Potion")


player.show_inventory()



@special_ability
def special_move(self):
    print(f"{self.name} performs a special move!")


special_move(player)
special_move(player)
special_move(player)
special_move(player)

health = health_manager(100)
print("Health:", health())
health(-20)
print("After damage:", health())
health(50)
print("After healing:", health())


for item in find_item(player.inventory, "Shield"):
    print(item)
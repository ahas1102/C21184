class Character:
  def __init__(self, name, health):
      self.name = name
      self.health = health

  def attack(self, target):
      """Метод атаки: зменшує здоров'я цілі на певну кількість, яку визначає підклас."""
      raise NotImplementedError("Метод 'attack' має бути реалізований в підкласах")


class Hero(Character):
  def __init__(self, name, health, weapon):
      super().__init__(name, health)
      self.weapon = weapon

  def attack(self, target):
      """Метод атаки для героя: зменшує здоров'я ворога залежно від зброї."""
      damage = 10
      if self.weapon == 'dagger':
          damage = 15
      elif self.weapon == 'bow':
          damage = 12
      print(f"{self.name} атакує {target.name} за допомогою {self.weapon}!")
      target.health -= damage
      print(f"{target.name} втрачає {damage} здоров'я. Залишилось здоров'я: {target.health}")


class Enemy(Character):
  def __init__(self, name, health, damage):
      super().__init__(name, health)
      self.damage = damage

  def attack(self, target):
      """Метод атаки для ворога: зменшує здоров'я героя залежно від пошкодження."""
      print(f"{self.name} атакує {target.name}!")
      target.health -= self.damage
      print(f"{target.name} втрачає {self.damage} здоров'я. Залишилось здоров'я: {target.health}")


hero = Hero(name="Gojo", health=150, weapon="dagger")
enemy = Enemy(name="amogus", health=60, damage=15)
hero.attack(enemy)


enemy.attack(hero)
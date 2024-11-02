class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        info = (
            f"Назва товару: {self.name}\n"
            f"Ціна: {self.price} грн\n"
            f"Кількість: {self.quantity}\n"
            f"Загальна вартість: {self.calculate_total_price()} грн"
        )
        print(info)
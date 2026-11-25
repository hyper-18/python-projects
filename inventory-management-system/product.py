class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product ID:{self.product_id}")
        print(f"Product Name:{self.name}")
        print(f"Price $:{self.price}")
        print(f"Quantity:{self.quantity}")

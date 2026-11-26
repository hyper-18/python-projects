from product import Product

from database import (
    create_tables,
    insert_product,
    get_all_products,
    update_product,
    delete_product,
    change_stock,
    get_transactions,
    get_low_stock_products,
    get_inventory_value
)


class Inventory:

    def __init__(self):

        self.products = {}

        create_tables()

        self.load_products()

    # LOAD PRODUCTS
    def load_products(self):

        self.products = {}

        records = get_all_products()

        for record in records:

            product = Product(
                record[0],
                record[1],
                record[2],
                record[3]
            )

            self.products[product.product_id] = product

        print("Products loaded successfully!")

    # ADD PRODUCT
    def add_product(self, product):

        if product.product_id in self.products:

            print("Product already exists!")
            return

        if insert_product(product):

            self.products[product.product_id] = product

            print("Product added successfully!")

        else:

            print("Unable to add product. Check its ID.")

    # VIEW PRODUCTS
    def view_products(self):

        if not self.products:

            print("No products found!")
            return

        print("\n========== PRODUCT INVENTORY ==========")

        for product in self.products.values():

            product.display_product()

            print("---------------------------------------")

    # SEARCH PRODUCT
    def search_product(self, product_id):

        if product_id in self.products:

            print("Product Found!")

            self.products[product_id].display_product()

        else:

            print("Product not found!")

    # UPDATE PRODUCT
    def update_product(self, product_id, new_name, new_price):

        if product_id not in self.products:

            print("Product not found!")
            return

        if not new_name or new_price < 0:

            print("Invalid product details!")
            return

        product = self.products[product_id]

        product.name = new_name
        product.price = new_price

        if update_product(product):

            print("Product updated successfully!")

        else:

            print("Database update failed!")

    # DELETE PRODUCT
    def delete_product(self, product_id):

        if product_id not in self.products:

            print("Product not found!")
            return

        if delete_product(product_id):

            del self.products[product_id]

            print("Product deleted successfully!")

        else:

            print("Database deletion failed!")

    # ADD STOCK
    def add_stock(self, product_id, quantity):

        if product_id not in self.products:

            print("Product not found!")
            return

        if quantity <= 0:

            print("Quantity must be greater than zero!")
            return

        success, result = change_stock(
            product_id,
            quantity,
            "STOCK_ADDED"
        )

        if success:

            self.products[product_id].quantity = result

            print("Stock added successfully!")
            print(f"Updated quantity: {result}")

        else:

            print(result)

    # REMOVE STOCK
    def remove_stock(self, product_id, quantity):

        if product_id not in self.products:

            print("Product not found!")
            return

        if quantity <= 0:

            print("Quantity must be greater than zero!")
            return

        success, result = change_stock(
            product_id,
            quantity,
            "STOCK_REMOVED"
        )

        if success:

            self.products[product_id].quantity = result

            print("Stock removed successfully!")
            print(f"Updated quantity: {result}")

        else:

            print(result)

    # TRANSACTION HISTORY
    def transaction_history(self, product_id=None):

        transactions = get_transactions(product_id)

        if not transactions:

            print("No transactions found!")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in transactions:

            print(f"Transaction ID: {transaction[0]}")
            print(f"Product ID: {transaction[1]}")
            print(f"Type: {transaction[2]}")
            print(f"Quantity: {transaction[3]}")
            print(f"Timestamp: {transaction[4]}")

            print("-----------------------------------------")

    # LOW STOCK PRODUCTS
    def low_stock_report(self, threshold=5):

        products = get_low_stock_products(threshold)

        if not products:

            print("No low-stock products found!")
            return

        print("\n========== LOW STOCK PRODUCTS ==========")

        for record in products:

            print(f"Product ID: {record[0]}")
            print(f"Name: {record[1]}")
            print(f"Quantity: {record[3]}")

            print("----------------------------------------")

    # INVENTORY REPORT
    def inventory_report(self):

        total_products = len(self.products)

        total_units = sum(
            product.quantity
            for product in self.products.values()
        )

        total_value = get_inventory_value()

        print("\n========== INVENTORY REPORT ==========")

        print(f"Total Products: {total_products}")
        print(f"Total Stock Units: {total_units}")
        print(f"Total Inventory Value: ₹{total_value:.2f}")

        print("======================================")

from product import Product


class Inventory:

    def __init__(self):
        self.products = {}

    # ADD PRODUCT
    def add_product(self, product):

        if product.product_id in self.products:
            print("Product already exists!")

        else:
            self.products[product.product_id] = product
            print("Product added successfully!")

    # VIEW ALL PRODUCTS
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
    def update_product(self, product_id):

        if product_id not in self.products:
            print("Product not found!")
            return

        product = self.products[product_id]

        new_name = input("Enter new product name: ").strip()

        if not new_name:
            print("Product name cannot be empty!")
            return

        try:
            new_price = float(input("Enter new product price: "))

            if new_price < 0:
                print("Price cannot be negative!")
                return

            product.name = new_name
            product.price = new_price

            print("Product updated successfully!")

        except ValueError:
            print("Please enter a valid price!")

    # DELETE PRODUCT
    def delete_product(self, product_id):

        if product_id not in self.products:
            print("Product not found!")
            return

        del self.products[product_id]

        print("Product deleted successfully!")

    # ADD STOCK
    def add_stock(self, product_id, quantity):

        if product_id not in self.products:
            print("Product not found!")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        product = self.products[product_id]

        product.quantity += quantity

        print("Stock added successfully!")
        print(f"Updated quantity: {product.quantity}")

    # REMOVE STOCK
    def remove_stock(self, product_id, quantity):

        if product_id not in self.products:
            print("Product not found!")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        product = self.products[product_id]

        if quantity > product.quantity:
            print("Insufficient stock!")
            return

        product.quantity -= quantity

        print("Stock removed successfully!")
        print(f"Updated quantity: {product.quantity}")


# CREATE INVENTORY OBJECT

inventory = Inventory()


# MAIN FUNCTION

def main():

    while True:

        print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")

        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Add Stock")
        print("7. Remove Stock")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ADD PRODUCT
        if choice == "1":

            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()

            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))

                if not product_id or not name:
                    print("Product ID and name cannot be empty!")
                    continue

                if price < 0 or quantity < 0:
                    print("Price and quantity cannot be negative!")
                    continue

                product = Product(product_id, name, price, quantity)

                inventory.add_product(product)

            except ValueError:
                print("Please enter valid product details!")

        # VIEW PRODUCTS
        elif choice == "2":

            inventory.view_products()

        # SEARCH PRODUCT
        elif choice == "3":

            product_id = input("Enter product ID: ").strip()

            inventory.search_product(product_id)

        # UPDATE PRODUCT
        elif choice == "4":

            product_id = input("Enter product ID: ").strip()

            inventory.update_product(product_id)

        # DELETE PRODUCT
        elif choice == "5":

            product_id = input("Enter product ID: ").strip()

            inventory.delete_product(product_id)

        # ADD STOCK
        elif choice == "6":

            product_id = input("Enter product ID: ").strip()

            try:
                quantity = int(input("Enter quantity to add: "))

                inventory.add_stock(product_id, quantity)

            except ValueError:
                print("Please enter a valid quantity!")

        # REMOVE STOCK
        elif choice == "7":

            product_id = input("Enter product ID: ").strip()

            try:
                quantity = int(input("Enter quantity to remove: "))

                inventory.remove_stock(product_id, quantity)

            except ValueError:
                print("Please enter a valid quantity!")

        # EXIT
        elif choice == "8":

            print("Thank you for using Inventory Management System!")
            break

        else:

            print("Invalid choice! Please try again.")


# PROGRAM ENTRY POINT

if __name__ == "__main__":
    main()

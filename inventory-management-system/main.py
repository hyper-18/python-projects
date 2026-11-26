from product import Product
from inventory import Inventory


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
        print("8. Transaction History")
        print("9. Inventory Report")
        print("10. Low Stock Products")
        print("11. Exit")

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

                product = Product(
                    product_id,
                    name,
                    price,
                    quantity
                )

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

            if product_id not in inventory.products:

                print("Product not found!")
                continue

            new_name = input("Enter new product name: ").strip()

            try:

                new_price = float(input("Enter new price: "))

                inventory.update_product(
                    product_id,
                    new_name,
                    new_price
                )

            except ValueError:

                print("Please enter a valid price!")

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

        # TRANSACTION HISTORY
        elif choice == "8":

            product_id = input(
                "Enter product ID (press Enter for all): "
            ).strip()

            inventory.transaction_history(
                product_id if product_id else None
            )

        # INVENTORY REPORT
        elif choice == "9":

            inventory.inventory_report()

        # LOW STOCK PRODUCTS
        elif choice == "10":

            try:

                threshold = int(
                    input("Enter low-stock threshold (default 5): ") or 5
                )

                if threshold < 0:

                    print("Threshold cannot be negative!")
                    continue

                inventory.low_stock_report(threshold)

            except ValueError:

                print("Please enter a valid threshold!")

        # EXIT
        elif choice == "11":

            print("Thank you for using Inventory Management System!")
            break

        else:

            print("Invalid choice! Please try again.")


# PROGRAM ENTRY POINT
if __name__ == "__main__":

    main()

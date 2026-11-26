import sqlite3
from datetime import datetime

DATABASE_NAME = "inventory.db"


# CREATE DATABASE TABLES
def create_tables():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# INSERT PRODUCT
def insert_product(product):

    connection = sqlite3.connect(DATABASE_NAME)

    try:

        connection.execute("""
            INSERT INTO products
            (product_id, name, price, quantity)
            VALUES (?, ?, ?, ?)
        """, (
            product.product_id,
            product.name,
            product.price,
            product.quantity
        ))

        if product.quantity > 0:

            connection.execute("""
                INSERT INTO transactions
                (product_id, transaction_type, quantity, timestamp)
                VALUES (?, ?, ?, ?)
            """, (
                product.product_id,
                "INITIAL_STOCK",
                product.quantity,
                datetime.now().astimezone().isoformat(timespec="seconds")
            ))

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        connection.rollback()
        return False

    finally:

        connection.close()


# GET ALL PRODUCTS
def get_all_products():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    return products


# UPDATE PRODUCT
def update_product(product):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.execute("""
        UPDATE products
        SET name = ?, price = ?, quantity = ?
        WHERE product_id = ?
    """, (
        product.name,
        product.price,
        product.quantity,
        product.product_id
    ))

    updated = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return updated


# DELETE PRODUCT
def delete_product(product_id):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.execute(
        "DELETE FROM products WHERE product_id = ?",
        (product_id,)
    )

    deleted = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return deleted


# CHANGE STOCK
def change_stock(product_id, quantity, transaction_type):

    connection = sqlite3.connect(DATABASE_NAME)

    try:

        cursor = connection.cursor()

        cursor.execute(
            "SELECT quantity FROM products WHERE product_id = ?",
            (product_id,)
        )

        result = cursor.fetchone()

        if result is None:
            return False, "Product not found!"

        current_quantity = result[0]

        if transaction_type == "STOCK_ADDED":

            new_quantity = current_quantity + quantity

        elif transaction_type == "STOCK_REMOVED":

            if quantity > current_quantity:
                return False, "Insufficient stock!"

            new_quantity = current_quantity - quantity

        else:

            return False, "Invalid transaction type!"

        cursor.execute("""
            UPDATE products
            SET quantity = ?
            WHERE product_id = ?
        """, (new_quantity, product_id))

        cursor.execute("""
            INSERT INTO transactions
            (product_id, transaction_type, quantity, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            product_id,
            transaction_type,
            quantity,
            datetime.now().astimezone().isoformat(timespec="seconds")
        ))

        connection.commit()

        return True, new_quantity

    except sqlite3.Error:

        connection.rollback()
        return False, "Database error occurred!"

    finally:

        connection.close()


# GET TRANSACTION HISTORY
def get_transactions(product_id=None):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    if product_id:

        cursor.execute("""
            SELECT * FROM transactions
            WHERE product_id = ?
            ORDER BY transaction_id DESC
        """, (product_id,))

    else:

        cursor.execute("""
            SELECT * FROM transactions
            ORDER BY transaction_id DESC
        """)

    transactions = cursor.fetchall()

    connection.close()

    return transactions


# GET LOW STOCK PRODUCTS
def get_low_stock_products(threshold):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE quantity <= ?
        ORDER BY quantity ASC
    """, (threshold,))

    products = cursor.fetchall()

    connection.close()

    return products


# CALCULATE INVENTORY VALUE
def get_inventory_value():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(price * quantity)
        FROM products
    """)

    result = cursor.fetchone()[0]

    connection.close()

    return result if result is not None else 0

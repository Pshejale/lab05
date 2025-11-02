"""
Inventory System Module
-----------------------
Provides basic inventory management operations such as
adding, removing, saving, and loading items using JSON storage.
Includes input validation and safe file handling.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item: str = "default", qty: int = 0, logs=None):
    """Add an item and quantity to the stock data."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for add_item: %s, %s", item, qty)
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item: str, qty: int):
    """Remove a specific quantity of an item from stock."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
                logging.info("%s removed from inventory", item)
        else:
            logging.warning("Attempted to remove non-existent item: %s", item)
    except KeyError as e:
        logging.error("Error removing item: %s", e)


def get_qty(item: str):
    """Return the current quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info("Inventory data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.warning("Inventory file not found. Starting with empty data.")
        return {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        return {}


def save_data(file: str = "inventory.json"):
    """Save the current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory data saved successfully.")


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5):
    """Return a list of items with stock below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    logging.info("Inventory operations completed successfully.")


if __name__ == "__main__":
    main()

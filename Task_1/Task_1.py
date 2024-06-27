class Menu:
    def __init__(self):
        self.items = {
            'coffee': 30.0,
            'tea': 10.0,
            'sandwich': 50.0,
            'burger': 75.0,
            'fries': 90.0,
            'cake': 250.0
        }

    def get_price(self, item):
        return self.items.get(item.lower(), 0)

    def display_menu(self):
        print("\nMenu:")
        for item, price in self.items.items():
            print(f"{item.capitalize()}: ${price}")


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        item = item.lower().strip()
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        item = item.lower().strip()
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                del self.items[item]

    def get_items(self):
        return self.items

    def calculate_total(self, menu):
        total = 0
        for item, quantity in self.items.items():
            total += menu.get_price(item) * quantity
        return total

    def display_order(self, menu):
        print("\nCurrent Order:")
        for item, quantity in self.items.items():
            print(f"{item.capitalize()}: {quantity} x ${menu.get_price(item)} = ${menu.get_price(item) * quantity}")
        print(f"Total: ${self.calculate_total(menu)}")


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.order = Order()
        self.is_active = True

    def add_to_order(self, item, quantity):
        self.order.add_item(item, quantity)

    def close_order(self):
        self.is_active = False

    def open_order(self):
        self.order = Order()
        self.is_active = True

    def display_order(self, menu):
        self.order.display_order(menu)


class Cafe:
    def __init__(self, num_tables):
        self.menu = Menu()
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def place_order(self, table_number, items):
        table = self.tables[table_number - 1]
        if not table.is_active:
            table.open_order()
        for item, quantity in items.items():
            table.add_to_order(item, quantity)
            print(f"Added {quantity} x {item.capitalize()} to Table {table_number}")

    def close_order(self, table_number):
        table = self.tables[table_number - 1]
        table.close_order()
        print(f"Table {table_number} order closed.")

    def display_bill(self, table_number):
        table = self.tables[table_number - 1]
        if not table.is_active:
            print(f"\nBill for Table {table_number}:")
            table.display_order(self.menu)
        else:
            print(f"Table {table_number} order is still open.")


def main():
    cafe = Cafe(6)
    while True:
        cafe.menu.display_menu()
        print("\nCommands: order, close, bill, exit")
        command = input("Enter command: ").strip().lower()

        if command == 'order':
            table_number = int(input("Enter table number (1-6): "))
            items_input = input("Enter items and quantities : ")
            items = {}
            for part in items_input.split(','):
                item, quantity = part.strip().rsplit(' ', 1)
                items[item] = int(quantity)
            cafe.place_order(table_number, items)

        elif command == 'close':
            table_number = int(input("Enter table number (1-6): "))
            cafe.close_order(table_number)

        elif command == 'bill':
            table_number = int(input("Enter table number (1-6): "))
            cafe.display_bill(table_number)

        elif command == 'exit':
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
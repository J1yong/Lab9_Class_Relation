from physical_product import physical_product
from digital_product import digital_product
from file import save_json, load_json
from supplier import Supplier
from inventory import Inventory
from product import Product
from order import order



def display_all(inventory):
    if len(inventory.get_all_products()) == 0:
        print("No Product in Inventory yet.")
    else:
        for item in inventory.get_all_products():
            item.display_information()

def create_supplier():
            while True:
                try:
            
                    supplier_id = int(input("Supplier ID: "))
                    name = input("Name: ")
                    contact_email  = str(input("Contact Email: "))

                    account = Supplier(supplier_id, name, contact_email)
                    print("Supplier Account created Successfully!")

                    return account
                
                except ValueError:
                    print("invalid input!")
                    continue


def add_digital_product(account, inventory: Inventory):

    while True:
        try:
            id = inventory.load_latest_id()
            name = str(input("Product Name: "))
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            digital_size = int(input("Digital Size: "))

            newproduct = digital_product(id, name, stock, price, account, digital_size)

            inventory.add_product(newproduct)
            break

        except ValueError:
            print("Invalid input!")



def add_physical_product(account, inventory: Inventory):
    while True:
        try:
            id = inventory.load_latest_id()
            name = str(input("Product Name: "))
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            weight = int(input("Weight: "))

            newproduct = physical_product(id, name, stock, price, account, weight)
            
            inventory.add_product(newproduct)

            break

        except ValueError:
            print("Invalid input!")


def add_product(inventory: Inventory):

    account = create_supplier()

    while True:
        try:
            print("1. Physical Product")
            print("2. Digital Product")
            choice = int(input("choice: "))

            if choice == 1:
                print("------------------------------------------------")
                add_physical_product(account, inventory)
                break
            elif choice ==2:
                print("------------------------------------------------")
                add_digital_product(account, inventory)
                break
            else:
                print("invalid input!")
                continue
        
        except ValueError:
            print("invalid input!")
            continue




def update_stock(inventory):
    if len(inventory.get_all_products()) == 0:
        print("No Product in Inventory yet.")
    
    else:
        while True:
            try:
                inputid = str(input("Product ID:  "))
                inventory.search_product(inputid)
                
                quantity = int(input("Stock:  "))
                inventory.update_stock(inputid, quantity)
                break
            
            except ValueError:
                print("invalid input!")
                continue
                            
        
def search_product(inventory):
    if len(inventory.get_all_products()) == 0:
        print("No Product in Inventory yet.")
    else:
        while True:
            try:
                inputid = str(input("Product ID: "))
                inventory.search_product(inputid)
                break

            except ValueError:
                print("invalid input")
                continue


def display_ship_cost(inventory):
    physical_box = []

    for item in inventory.get_all_products():
        if isinstance(item, physical_product):
            physical_box.append(item)

    if len(physical_box) == 0:
        print("No Existing Physical Products")
        

    else:
        total = 0.0
        for item in physical_box:
            item.display_information()
            subtotal = item.calculate_shipping_cost()
            total += float(subtotal)
            
    print(f"total: ${total:2f}")


def create_order():
    while True:
        try:
            order_id = int(input("Order ID:  "))
            orderlist = order(order_id)
            return orderlist
        
        
        except ValueError:
            print("invalid input!")
            continue

def add_order(inventory, orderlist):
    if orderlist is None:
        print("No order assigned")
        return

    while True:
        try:
            product_id = input("Product ID: ")
            product_found = False

            for item in inventory.get_all_products():
                if item.get_product_id() == product_id:
                    product_found = True

                    quantity = int(input("Quantity: "))

                    if quantity <= 0:
                        print("Quantity must be greater than 0!")
                        break

                    if quantity > item.get_stock():
                        print("Not enough stock!")
                        break

                    orderlist.add_order_line(item, quantity)
                    print("Product added to order successfully!")
                    break

            if not product_found:
                print("Product ID not found!")
                continue

            break

        except ValueError:
            print("Invalid input!")


def remove_order(orderlist):
    if orderlist is None:
        print("No order assgined")

    else:
        while True:
            try: 
                print("Type the number of sqeunce of the product you want to remove.")
                index = int(input("Index: "))
                orderlist.remove_order_line(index)
                print("product removed successfully!")
                break

            except ValueError:
                print("invalid input")
                continue

def view_order(orderlist):

    if orderlist is None:
        print("no order assgined")
    else:
            
        print("----------------Order List------------------")
        print(f"Order ID: {orderlist.get_order_id()}")
        print("\n")

        orderlistss = orderlist.get_order_lines()
        for item in orderlistss:
            product = item[0]
            quantity = item[1]
            subtotal = item[2]
            print(f"Name: {product.get_name()} ")
            print(f"Quantity: {quantity}")
            print(f"Subtotal: ${subtotal} \n")


def order_calculate_total(orderlist):
    if orderlist is None:
        print("no order assgined")
    else:
            
        print("----------------Order List------------------")
        print(f"Order ID: {orderlist.get_order_id()}")
        print("\n")

        orderlistss = orderlist.get_order_lines()
        for item in orderlistss:
            product = item[0]
            quantity = item[1]
            subtotal = item[2]
            print(f"Name: {product.get_name()} ")
            print(f"Quantity: {quantity}")
            print(f"Subtotal: ${subtotal} \n")
    

        print("--------------------------------------------")
        print(f"Grandtotal: ${orderlist.calculate_total()}")

    

def inventory_main_print():
    print("----------------Inventory Menu------------------")
    print("1. Display all products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Show Total of all Shipping Cost")
    print("6. Save Inventory")
    print("7. Create an Order")
    print("8. Quit")


def order_main_print():
    print("-----------------Order Menu-----------------------")
    print("1. Create Order")
    print("2. Add Product to Order")
    print("3. View Order")
    print("4. Remove Order Line")
    print("5. Calculate Total")
    print("6. back")


def order_menu(inventory):

        while True:
            try:
                print("-----------------------------------------------------")
                choice = int(input("Enter option:  "))

            except ValueError:
                print("invalid input! try again")
                continue

            if choice == 1:
                orderlist = create_order()


            elif choice == 2:
                add_order(inventory, orderlist)

            elif choice == 3:
                view_order(orderlist)

            elif choice == 4:
                remove_order(orderlist)

            elif choice == 5:
                order_calculate_total(orderlist)

            elif choice == 6:
                inventory_main_print()
                return False


def main():

    inventory = Inventory()


    print("======================================")
    print("Welcome to INVENTORY MANAGEMENT SYSTEM")
    print("======================================")


    print("Loading inventory from Json file...")
    load_json(inventory)
    print("Json file loaded successfully!")


    inventory_main_print()

    while True:

        try:
            print("-----------------------------------------------------")
            choice = int(input("Enter option:  "))

        except ValueError:
            print("invalid input! try again")
            continue

        if choice == 1:
            display_all(inventory)

        elif choice == 2:
            add_product(inventory)

        elif choice == 3:
            update_stock(inventory)

        elif choice == 4:
            search_product(inventory)

        elif choice == 5:
            display_ship_cost(inventory)

        elif choice == 6:
            save_json(inventory)
            print("inventory saved!")

        elif choice ==7:
            order_main_print()
            order_menu(inventory)

        elif choice == 8:
            print("you have quited the program!")
            return False



main()
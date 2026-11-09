from physical_product import physical_product
from digital_product import digital_product
from supplier import Supplier
from inventory import Inventory
from product import Product
from order import order
from canbeshipped import CanBeShipped

def test_association():
    # Create a Supplier independently
    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")

    # Create two Products using the same Supplier
    product1 = physical_product(
        "P001", "Laptop", 10, 1000.0, supplier, 2.0
    )

    product2 = digital_product(
        "P002", "Ebook", 20, 50.0, supplier, 100
    )

    # Display Supplier information through each Product
    print("Physical Product Supplier:")
    product1.get_supplier().display_information()

    print("\nDigital Product Supplier:")
    product2.get_supplier().display_information()

    # Confirm both Products reference the same Supplier
    print("\nSame Supplier:",
          product1.get_supplier() is product2.get_supplier())

    # Delete the original Supplier variable
    del supplier

    # Check whether both Products can still access Supplier information
    print("\nAfter deleting Supplier variable:")

    product1.get_supplier().display_information()
    product2.get_supplier().display_information()

# -----------------------------------------------------------------------------------------------------------


def test_aggregation():
    print("===== AGGREGATION TEST =====")

    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")

    # Create Product before Inventory
    product1 = physical_product(
        "P001", "Laptop", 10, 1000.0, supplier, 2.0
    )

    inventory_a = Inventory()
    inventory_b = Inventory()

    # Add Product to Inventory A
    inventory_a.add_product(product1)

    print("Product in Inventory A:",
          product1 in inventory_a.get_all_products())

    # Remove Product from Inventory A
    inventory_a.remove_product("P001")

    print("Inventory A is empty:",
          len(inventory_a.get_all_products()) == 0)

    # Product still exists
    print("Product still works:")
    product1.display_information()

    # Add same Product to Inventory B
    inventory_b.add_product(product1)

    print("Same Product in Inventory B:",
          product1 in inventory_b.get_all_products())

    # Remove Product from Inventory B
    inventory_b.remove_product("P001")

    print("Inventory B is empty:",
          len(inventory_b.get_all_products()) == 0)

    print("Product still exists:", product1.get_name())

test_aggregation()


# -----------------------------------------------------------------------------------------------------------
def test_composition():
    print("===== COMPOSITION TEST =====")

    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")

    product1 = physical_product(
        "P001", "Laptop", 10, 1000.0, supplier, 2.0
    )

    product2 = digital_product(
        "P002", "Ebook", 20, 50.0, supplier, 100
    )

    # Create Order 1
    order1 = order("O001")

    # Add two products
    order1.add_order_line(product1, 2)
    order1.add_order_line(product2, 3)

    # Display order lines
    print("\nOrder 1:")
    for product, quantity, subtotal in order1.get_order_lines():
        print("Product:", product.get_name())
        print("Quantity:", quantity)
        print("Subtotal:", subtotal)

    print("Order 1 Total:", order1.calculate_total())

    # Create Order 2 using the same Product
    order2 = order("O002")
    order2.add_order_line(product1, 1)

    print("\nOrder 2:")
    for product, quantity, subtotal in order2.get_order_lines():
        print("Product:", product.get_name())
        print("Quantity:", quantity)
        print("Subtotal:", subtotal)

    print("Order 2 Total:", order2.calculate_total())

    # Check whether both orders share the same Product
    print("\nSame Product:",
          order1.get_order_lines()[0][0] is order2.get_order_lines()[0][0])

    # Check number of OrderLines
    print("Order 1 OrderLines:", len(order1.get_order_lines()))
    print("Order 2 OrderLines:", len(order2.get_order_lines()))

    # Remove an OrderLine from Order 1
    order1.remove_order_line(0)

    print("\nAfter removing OrderLine:")
    print("Order 1 OrderLines:", len(order1.get_order_lines()))
    print("Order 2 OrderLines:", len(order2.get_order_lines()))

    # Product still exists
    print("Product still exists:", product1.get_name())



supplier30 = Supplier("S001", "ABC Supplier", "abc@gmail.com")
product30 = physical_product(
    "P001", "Laptop", 10, 1000.0, supplier30, 2.0
    )



def show_product_details (product: Product) -> None:
    print("=====Inheritance Test=====")

    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")
    product1 = physical_product(
        "P001", "Laptop", 10, 1000.0, supplier, 2.0
    )

    product2 = digital_product(
        "P002", "Ebook", 20, 50.0, supplier, 100
    )

    print(product1.get_fulfilment_info())
    print(product2.get_fulfilment_info())


test_composition()
show_product_details(product30)

# -----------------------------------------------------------------------------------------------------------

def test_lsp():
    print("===== LSP TEST =====")

    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")

    product1 = physical_product(
        "P001", "Laptop", 10, 1000.0, supplier, 2.0
    )

    product2 = digital_product(
        "P002", "Ebook", 20, 50.0, supplier, 100
    )

    # Test both subclasses with the same function
    print("\nPhysical Product:")
    show_product_details(product1)

    print("\nDigital Product:")
    show_product_details(product2)

    # Test both subclasses with Inventory
    inventory = Inventory()

    inventory.add_product(product1)
    inventory.add_product(product2)

    print("\nProducts in Inventory:")
    for product in inventory.get_all_products():
        print(product.get_name())

    # Update stock using Inventory
    inventory.update_stock("P001", 5)
    inventory.update_stock("P002", 8)

    print("\nAfter updating stock:")
    for product in inventory.get_all_products():
        print(product.get_name(), "Stock:", product.get_stock())

test_lsp()
# -----------------------------------------------------------------------------------------------------------

def test_polymorphism():
    print("===== POLYMORPHISM TEST =====")

    supplier = Supplier("S001", "ABC Supplier", "abc@gmail.com")

        # Create physical and digital products
    product1 = physical_product(
            "P001", "Laptop", 10, 1000.0, supplier, 2.0
        )

    product2 = digital_product(
            "P002", "Ebook", 20, 50.0, supplier, 100
        )

        # Add both products to the same Inventory
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)

        # Call the same methods through the Product collection
    for product in inventory.get_all_products():
        product.display_information()
        print(product.get_fulfilment_info())
        print("-----------------------------")

test_polymorphism()
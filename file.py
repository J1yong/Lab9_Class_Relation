import json
from physical_product import physical_product
from digital_product import digital_product
from supplier import Supplier


FILE = "inventory.json"

def load_json(inventory):

    try:

        with open(FILE, "r") as file:
            data = json.load(file)

            for item in data:
                if item["type"] == "physical":
                    product_id = str(item["[Product] id"])
                    name = str(item["[Product] name"])
                    stock = int(item["[Product] stock"])
                    price = float(item["[Product] price"])
                    supplier_id = int(item["[Supplier] id"])
                    supplier_name = str(item["[Supplier] name"])
                    supplier_email = str(item["[Supplier] email"])
                    weight = int(item["[Product] weight"])

                    supply = Supplier(supplier_id,supplier_name, supplier_email)
                    physical = physical_product(product_id, name, stock, price,supply, weight)
                    inventory.add_product(physical)

                elif item["type"] == "digital":
                    product_id = str(item["[Product] id"])
                    name = str(item["[Product] name"])
                    stock = int(item["[Product] stock"])
                    price = float(item["[Product] price"])
                    supplier_id = int(item["[Supplier] id"])
                    supplier_name = str(item["[Supplier] name"])
                    supplier_email = str(item["[Supplier] email"])
                    digital_size = int(item["[Product] digital_size"])

                    supply = Supplier(supplier_id,supplier_name, supplier_email)
                    digital = digital_product(product_id, name, stock, price, supply, digital_size)
                    inventory.add_product(digital)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing file found")


def save_json(inventory):
    
    dictdata = []
    
    for product in inventory.get_all_products():
        dictdata.append(product.to_dictionary())

    with open(FILE, "w") as file:
        json.dump(dictdata, file, indent=4)


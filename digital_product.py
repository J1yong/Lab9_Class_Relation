from product import Product
from supplier import Supplier

class digital_product(Product):
    def __init__ (self, product_id: str, name: str, stock: int, price: float, supplier: Supplier, digital_size: int):
        super().__init__(product_id, name, stock, price, supplier)
        self.__digital_size = digital_size

    def display_information(self):
        super().display_information()
        print(f"Digital Size: {self.__digital_size}MB\n")

    def to_dictionary(self):
        data = super().to_dictionary()
        data["[Product] digital_size"] = self.__digital_size
        data["type"] = "digital"
        return data

    def get_fulfilment_info(self) -> str:
        return "The product is delivered digitally."

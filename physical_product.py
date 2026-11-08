from product import Product
from canbeshipped import CanBeShipped
from supplier import Supplier

class physical_product(Product, CanBeShipped):
    def __init__ (self, product_id: str, name: str, stock: int, price: float, supplier: Supplier, weight: float):
        super().__init__(product_id, name, stock, price, supplier)
        self.__weight = weight


    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg ")
        print(f"Shipping Cost: ${self.calculate_shipping_cost()} ($3.00 per kg)\n")


    def to_dictionary(self):
        data = super().to_dictionary()
        data["[Product] weight"] = self.__weight
        data["type"] = "physical"
        return data 


    def get_fulfilment_info(self) -> str:
        return "The product requires physical shipping."


    def calculate_shipping_cost(self) -> float:
        shipping_cost = self.__weight * 3.0
        return shipping_cost
        






from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, stock: int, price: float, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__stock = stock
        self.__price = price
        self.__supplier : Supplier = supplier


    def get_supplier(self) -> Supplier:
        return self.__supplier


    def updating_stock(self, quantity: int) -> int:
        if quantity >= 0:
            self.__stock = quantity
            return quantity


    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Stock: {self.__stock}")
        print(f"Price: ${self.__price}")


    def to_dictionary(self):
        data =  {
            "[Product] id": self.__product_id,
            "[Product] name": self.__name,
            "[Product] stock": self.__stock,
            "[Product] price": self.__price,
            "[Supplier] id": self.__supplier.get_supplier_id(),
            "[Supplier] name": self.__supplier.get_name(),
            "[Supplier] email": self.__supplier.get_contact_email()
        }
        return data


    def get_product_id(self) -> int:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name  

    def get_stock(self) -> int:
        return self.__stock 

    def get_price(self) -> float:
        return self.__price

    @abstractmethod

    def get_fulfilment_info(self):
        pass




    









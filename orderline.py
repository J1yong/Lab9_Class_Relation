from product import Product


class orderline:
    def __init__(self, product: Product, quantity:int):
        self.__product = product
        self.__quantity = quantity

    def get_product(self) -> Product:
        return self.__product 
    
    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        subtotal = self.__product.get_price() * self.__quantity
        return subtotal

    
from product import Product


# {"1000": physicalproduct(), "1001":digitalproduct(), "1002":physicalproduct()}


class Inventory:
    def __init__(self):
        self.__products: dict[str, Product] = {}

    def load_latest_id(self) -> str:
        if len(self.__products) == 0:
            return "P001"

        else:
            latest_id = max(int(key[1:]) for key in self.__products)
            latest_id += 1
            return f"P{latest_id:03d}"


    def add_product(self, product: Product) -> None:
        self.__products[product.get_product_id()] = product

    def remove_product(self, product_id:str ):
        if product_id in self.__products:
            del self.__products[product_id]

    def search_product(self, product_id:str):
        if product_id in self.__products:
            print("Product Found\n")
            (self.__products[product_id]).display_information()

        else:
            raise ValueError("Product ID not found!")

    def update_stock(self, product_id:str, quantity:int):
        if product_id in self.__products:
            (self.__products[product_id]).updating_stock(quantity)

    def get_all_products(self):
        return tuple(self.__products.values())

        

    

    
                

        

        


                    
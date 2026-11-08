from orderline import orderline
from product import Product

class order:
    def __init__(self, order_id:str):
        self.__order_id = order_id
        self.__order_lines = []


    def get_order_id(self) -> str:
        return self.__order_id 

    def add_order_line(self, product: Product, quantity: int) -> None:
        line = orderline(product,quantity)
        self.__order_lines.append(line)

    def remove_order_line (self, index: int) -> None:
        if 0 <= index < len(self.__order_lines):
            self.__order_lines.pop(index)
        else:
            print("invalid index")

    def get_order_lines(self):
        data = ()
        for item in self.__order_lines:
            orderlist = (item.get_product(), item.get_quantity(), item.calculate_subtotal())
            data += (orderlist,)
        return data
    
    def calculate_total(self) -> float:
        total = 0.0
        for item in self.__order_lines:
            total += float(item.calculate_subtotal())
        
        return total

    






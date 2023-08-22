import sys
from typing import List

class SandwichError(Exception):
    pass


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Products:
    def __init__(self, product_list: List[str]) -> None:
        self.product_list = product_list

    @property
    def product_list(self):
        return self.__product_list

    @product_list.setter
    def product_list(self, value):
        if "sandwich" not in value:
            raise SandwichError("You forgot the sandwich!!!")
        self.__product_list = value

    @classmethod
    def custom(cls):
        my_products = ["banana", "sandwich", "chocolate"]
        return cls(my_products)

    def __str__(self) -> str:
        return "This is very cool and works as expected"



products = Products.custom()

try:
    sorted_product = next(filter(lambda x: x == "sandwich", products.product_list))
    print(Colors.BLUE + f"I found a {sorted_product} from the list of products: {', '.join(products.product_list)}" + Colors.RESET)
except StopIteration:
    print(Colors.RED + "I can not find it" + Colors.RESET)
else:
    print(Colors.GREEN + "I will try next time" + Colors.RESET)
finally:
    print(Colors.HEADER + Colors.BOLD + "I will do it anyway" + Colors.RESET)

print(products, file=sys.stderr)

print(Colors.UNDERLINE + Colors.RED + ", ".join(next(iter(products.__dict__.values()))) + Colors.RESET)






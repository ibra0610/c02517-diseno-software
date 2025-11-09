from ..item_menu import ItemMenu

class Tea(ItemMenu):
    
    def __init__(self, type: str = "negro"):
        self.type = type

    def get_description(self) -> str:
        return f"Té {self.type}"

    def get_price(self) -> float:
        return 2.00
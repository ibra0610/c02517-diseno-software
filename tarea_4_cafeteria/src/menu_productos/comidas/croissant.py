from ..item_menu import ItemMenu

class Croissant(ItemMenu):
    def get_description(self) -> str:
        return "Croissant"

    def get_price(self) -> float:
        return 3.00
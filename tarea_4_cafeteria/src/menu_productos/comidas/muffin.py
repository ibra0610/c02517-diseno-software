from ..item_menu import ItemMenu

class Muffin(ItemMenu):
    def get_description(self) -> str:
        return "Muffin"

    def get_price(self) -> float:
        return 2.75
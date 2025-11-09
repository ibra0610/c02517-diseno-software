from ..item_menu import ItemMenu

class Coffee(ItemMenu):
    def get_description(self) -> str:
        return "Café"

    def get_price(self) -> float:
        return 2.50
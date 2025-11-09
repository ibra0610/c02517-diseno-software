from ..item_menu import ItemMenu

class Toast(ItemMenu):
    def get_description(self) -> str:
        return "Tostada"

    def get_price(self) -> float:
        return 1.50
    

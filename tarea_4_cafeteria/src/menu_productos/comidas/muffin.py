from ..item_menu import ItemMenu

class Muffin(ItemMenu):
    def get_descripcion(self) -> str:
        return "Muffin"

    def get_precio(self) -> float:
        return 2.75
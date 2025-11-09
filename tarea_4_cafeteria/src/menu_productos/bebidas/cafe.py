from ..item_menu import ItemMenu

class Cafe(ItemMenu):
    def get_descripcion(self) -> str:
        return "Café"

    def get_precio(self) -> float:
        return 2.50
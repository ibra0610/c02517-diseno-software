from ..item_menu import ItemMenu

class Tostada(ItemMenu):
    def get_descripcion(self) -> str:
        return "Tostada"

    def get_precio(self) -> float:
        return 1.50
    

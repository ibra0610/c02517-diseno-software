from ..item_menu import ItemMenu

class Te(ItemMenu):
    
    def __init__(self, tipo: str = "negro"):
        self.tipo = tipo

    def get_descripcion(self) -> str:
        return f"Té {self.tipo}"

    def get_precio(self) -> float:
        return 2.00
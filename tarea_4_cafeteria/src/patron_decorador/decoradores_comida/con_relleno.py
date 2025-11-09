from ..decorators import ItemDecorator
from ...menu_productos.item_menu import ItemMenu

class ConRelleno(ItemDecorator):

    def __init__(self, item: ItemMenu, tipo_relleno: str = "chocolate"):
        super().__init__(item)
        self._tipo_relleno = tipo_relleno
    
    def get_descripcion(self) -> str:
        return f"{self._item.get_descripcion()} con relleno de {self._tipo_relleno}"

    def get_precio(self) -> float:
        return self._item.get_precio() + 1.00
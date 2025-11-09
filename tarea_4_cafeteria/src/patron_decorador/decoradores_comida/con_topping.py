from ..decorators import ItemDecorator
from ...menu_productos.item_menu import ItemMenu

class ConTopping(ItemDecorator):
    def __init__(self, item: ItemMenu, topping: str = "fresa"):
        super().__init__(item)
        self.topping = topping

    def get_descripcion(self) -> str:
        return f"{self._item.get_descripcion()} con topping de {self.topping}"

    def get_precio(self) -> float:
        return self._item.get_precio() + 0.80
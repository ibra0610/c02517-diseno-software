from ..menu_productos.item_menu import ItemMenu
from .command import Command

class PrepararBebida(Command):

    def __init__(self, item: ItemMenu):
        self.item = item

    def ejecutar(self):
        print(f"[Barista]: Preparo bebida: {self.item.get_descripcion()}")

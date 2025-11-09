from ..menu_productos.item_menu import ItemMenu
from command import Command

class PrepararComida(Command):

    def __init__(self, item: ItemMenu):
        self.item = item

    def ejecutar(self):
        print(f"[Pastelero]: Preparo alimento: {self.item.get_descripcion()}")

        
"""
decorators.py
Decorador base para los items del menú de la cafetería.
"""

from abc import ABC, abstractmethod
from ..menu_productos.item_menu import ItemMenu

class ItemDecorator(ItemMenu):
    """
    Clase abstracta que representa un decorador para los items del menú.
    """

    def __init__(self, item: ItemMenu):
        self._item = item

    @abstractmethod
    def get_descripcion(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> float:
        pass


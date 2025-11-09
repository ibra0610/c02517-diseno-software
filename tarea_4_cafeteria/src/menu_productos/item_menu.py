"""
item_menu.py
Clase base para los items del menú de la cafetería.
"""

from abc import ABC, abstractmethod

class ItemMenu(ABC):
    """
    Clase abstracta que representa un item del menú.
    """

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass
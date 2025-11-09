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
        """
        Método abstracto para obtener la descripción del item del menú.
        """
        pass

    @abstractmethod
    def get_price(self) -> float:
        """
        Método abstracto para obtener el precio del item del menú.
        """
        pass
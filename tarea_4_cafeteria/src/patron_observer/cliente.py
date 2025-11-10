from .observer import Observer
from typing import List
from ..menu_productos.item_menu import ItemMenu

class Cliente(Observer):
    """
    Cliente que sera notificado
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pedidos: List[ItemMenu] = []

    def agregar_item(self, item: ItemMenu):
        """Agrega un item al pedido del cliente"""
        self.pedidos.append(item)
        print(f"Ordena un {item.get_descripcion().lower()}")

    def actualizar(self, mensaje: str):
        """Recibe notificaciones"""
        print(f"[Notificación para {self.nombre}]: {mensaje}")

    def get_total_pedido(self) -> float:
        """Calcula el total del pedido"""
        return sum(item.get_precio() for item in self.pedidos)
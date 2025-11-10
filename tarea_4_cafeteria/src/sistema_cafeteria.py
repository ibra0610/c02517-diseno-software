"""
sistema_cafeteria.py
Sistema principal que gestiona los pedidos y notificaciones
"""

from typing import List
from .patron_observer.subject import Subject
from .patron_observer.observer import Observer
from .patron_command.pedido import Pedido

class SistemaCafeteria(Subject):
    """Sistema principal que gestiona los pedidos y notificaciones"""

    def __init__(self):
        self._observadores: List[Observer] = []
        self.pedidos: List[Pedido] = []

    def agregar_observer(self, observer: Observer):
        """Agrega un observador (cliente) al sistema"""
        self._observadores.append(observer)

    def eliminar_observer(self, observer: Observer):
        """Remueve un observador del sistema"""
        self._observadores.remove(observer)

    def notificar_observers(self, mensaje: str):
        """Notifica a todos los observadores"""
        for observer in self._observadores:
            observer.actualizar(mensaje)
    
    def registrar_pedido(self, pedido: Pedido):
        """Registra un nuevo pedido en el sistema"""
        self.pedidos.append(pedido)

    def procesar_pedidos(self):
        """Procesa todos los pedidos registrados"""
        for pedido in self.pedidos:
            pedido.procesar()
    
    def notificar_pedidos_listos(self):
        """Notifica a todos los clientes que sus pedidos están listos"""
        print("\n[Sistema]: Se notifican los clientes cuando sus pedidos estan listos.")
        for pedido in self.pedidos:
            total = pedido.cliente.get_total_pedido()
            mensaje = f"Tu pedido está listo. Total: ${total:.2f}"
            pedido.cliente.actualizar(mensaje)
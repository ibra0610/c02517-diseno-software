from ..patron_observer.cliente import Cliente
from typing import List
from command import Command

class Pedido:
    """
    Clase que representa un pedido realizado por un cliente
    """

    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.comandos: List[Command] = []

    def agregar_comando(self, comando: Command):
        """Agrega un comando al pedido"""
        self.comandos.append(comando)

    def procesar(self):
        """ Ejecuta todos los comandos del pedido """
        for comando in self.comandos:
            comando.ejecutar()

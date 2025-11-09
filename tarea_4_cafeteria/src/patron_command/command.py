"""
command.py
Implementación del patrón Command para encapsular órdenes
"""
from abc import ABC, abstractmethod


class Command(ABC):
    """ Interfaz para los comandos """

    @abstractmethod
    def ejecutar(self):
        pass
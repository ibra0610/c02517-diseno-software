"""
observer.py
Implementación del patrón Observer para notificaciones
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Interfaz para los observers
    """

    @abstractmethod
    def actualizar(self, mensaje: str):
        pass
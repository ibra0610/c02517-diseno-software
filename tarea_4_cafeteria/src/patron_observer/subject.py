from abc import ABC, abstractmethod
from observer import Observer


class Subject(ABC):
    """
    Interfaz para los subjects
    """

    @abstractmethod
    def agregar_observer(self, observer: Observer):
        pass

    @abstractmethod
    def eliminar_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notificar_observers(self, mensaje: str):
        pass
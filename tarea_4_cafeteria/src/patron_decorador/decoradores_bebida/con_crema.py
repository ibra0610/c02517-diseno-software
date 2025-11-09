from ..decorators import ItemDecorator

class ConCrema(ItemDecorator):
    def get_descripcion(self) -> str:
        return f"{self._item.get_descripcion()} con crema"

    def get_precio(self) -> float:
        return self._item.get_precio() + 0.70
    
    
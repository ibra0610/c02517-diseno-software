"""
main.py
Simula el flujo completo de pedidos
"""

from .menu_productos.bebidas.cafe import Cafe
from .menu_productos.bebidas.te import Te
from .patron_decorador.decoradores_bebida.con_canela import ConCanela
from .patron_decorador.decoradores_bebida.con_crema import ConCrema
from .patron_decorador.decoradores_bebida.con_leche import ConLeche
from .menu_productos.comidas.croissant import Croissant
from .menu_productos.comidas.muffin import Muffin
from .menu_productos.comidas.tostada import Tostada
from .patron_decorador.decoradores_comida.con_relleno import ConRelleno
from .patron_decorador.decoradores_comida.con_topping import ConTopping
from .patron_observer.cliente import Cliente
from .patron_command.pedido import Pedido
from .patron_command.preparar_bebida import PrepararBebida
from .patron_command.preparar_comida import PrepararComida
from .sistema_cafeteria import SistemaCafeteria

def main():
    """Función principal que simula el sistema de cafetería"""

    print("=== Simulacion de Cafeteria ===\n")

    sistema = SistemaCafeteria()

    # Cliente Ana
    ana = Cliente("Ana")
    sistema.agregar_observer(ana)
    print(f"Cliente: {ana.nombre}")

    # Pedido 1, cafe con leche y canela
    cafe1 = Cafe()
    cafe1 = ConLeche(cafe1)
    cafe1 = ConCanela(cafe1)
    ana.agregar_item(cafe1)

    # Pedido 2, croissant con relleno de chocolate
    croissant1 = Croissant()
    croissant1 = ConRelleno(croissant1, "chocolate")
    ana.agregar_item(croissant1)

    # Pedido de Ana con comandos
    pedido_ana = Pedido(ana)
    pedido_ana.agregar_comando(PrepararBebida(cafe1))
    pedido_ana.agregar_comando(PrepararComida(croissant1))
    sistema.registrar_pedido(pedido_ana)

    print("\n---\n")

    # Cliente Carlos
    carlos = Cliente("Carlos")
    sistema.agregar_observer(carlos)
    print(f"Cliente: {carlos.nombre}")

    # Pedido 1, té verde
    te1 = Te("verde")
    carlos.agregar_item(te1)

    # Pedido 2, cafe con crema
    cafe2 = Cafe()
    cafe2 = ConCrema(cafe2)
    carlos.agregar_item(cafe2)

    # Pedido de Carlos con comandos
    pedido_carlos = Pedido(carlos)
    pedido_carlos.agregar_comando(PrepararBebida(te1))
    pedido_carlos.agregar_comando(PrepararBebida(cafe2))
    sistema.registrar_pedido(pedido_carlos)

    print("\n---\n")

    # Procesar todos los pedidos

    sistema.procesar_pedidos()

    # Notificar clientes
    sistema.notificar_pedidos_listos()

if __name__ == "__main__":
    main()


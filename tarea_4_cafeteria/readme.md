# Cafetería con patrones de diseño - Javier Cruz C02517

## Descripción del proyecto

Este proyecto se trata de desarrollar un sistema de pedidos para una cafetería que permite a los clientes ordenar bebidas y comidas personalizadas.

### Instrucciones de ejecución

Para correr el proyecto, se debe ejecutar el comando `python -m src.main` en la ruta `c02517-diseno-software\tarea_4_cafeteria`. La salida esperada es la siguiente:

```
=== Simulacion de Cafeteria ===

Cliente: Ana
Ordena un café con leche con canela
Ordena un croissant con relleno de chocolate

---

Cliente: Carlos
Ordena un té verde
Ordena un café con crema

---

[Barista]: Preparo bebida: Café con leche con canela
[Pastelero]: Preparo alimento: Croissant con relleno de chocolate
[Barista]: Preparo bebida: Té verde
[Barista]: Preparo bebida: Café con crema

[Sistema]: Se notifican los clientes cuando sus pedidos estan listos.
[Notificación para Ana]: Tu pedido está listo. Total: $7.30
[Notificación para Carlos]: Tu pedido está listo. Total: $5.20
```
#### Estructura del proyecto

El proyecto se encuentra organizado en diferentes carpetas, separando los patrones de diseño, así como los elementos de la cafetería.

    src/
    ├── main.py
    ├── sistema_cafeteria.py
    ├── menu_productos/
    │   ├── item_menu.py
    │   ├── bebidas/
    │   │   ├── cafe.py
    │   │   └── te.py
    │   └── comidas/
    │       ├── croissant.py
    │       ├── muffin.py
    │       └── tostada.py
    ├── patron_command/
    │   ├── command.py
    │   ├── pedido.py
    │   ├── preparar_bebida.py
    │   └── preparar_comida.py
    ├── patron_decorator/
    │   ├── decorators.py
    │   ├── decoradores_bebida/
    │   │   ├── con_canela.py
    │   │   ├── con_crema.py
    │   │   └── con_leche.py
    │   └── decoradores_comida/
    │       ├── con_relleno.py
    │       └── con_topping.py
    └── patron_observer/
        ├── client.py
        ├── observer.py
        └── subject.py

## Patrones de diseño elegidos

### Patrón Decorator

Decorador es un patrón de diseño estructural que permite agregar nuevas funciones a objetos al agregar los mismos a *wrappers* especiales qeu contienen dichas funciones. 

Se decidió utilizar este patrón de diseño ya que permite agregar funciones y personalización a las bebidas y alimentos de manera flexible sin afectar las clases base.

#### Implementación

- `ItemMenu` Corresponde al componente base abstracto para los elementos de la cafetería.

- Elementos como `Cafe`, `Tostada`, etc corresponden a los componentes concretos del patrón.

- `ItemDecorator` sería el decorador base para los elementos.

- Clases como `ConLeche`, `ConCrema`, etc corresponden a los decoradores concretos. 

Ejemplo de uso en en el proyecto (clase main):

```python
cafe1 = Cafe()
cafe1 = ConLeche(cafe1)
cafe1 = ConCanela(cafe1)
```

Se crea un café base, posteriormente "se le agrega" leche y canela.


### Patrón Observer

Observer es un patrón de comportamiento que permite definir un mecanismo de *suscripción* para notificar a múltiples objetos sobre eventos que le ocurren al elemento que están observando. 

Se decició utilizar observer para notificar a los clientes cuando sus pedidos están listos.

#### Implementación

- `Subject` Corresponde a la interfaz del elemento observado.
- `Observer` Sería la interfaz del observador
- El `SistemaCafeteria` es la sección que gestiona las notificaciones
- El `Cliente` corresponde al observador concreto que recibe notificaciones

Ejemplo de uso en en el proyecto (clase main):

```python
    sistema = SistemaCafeteria()

    # Cliente Ana
    ana = Cliente("Ana")
    sistema.agregar_observer(ana)
```

### Patrón Command

Command es un patrón de comportamiento que transforma un *request* en un objeto que contiene la información de dicho request. Esto permite enviar requests como argumentos. 

Se decidió utilizar ya que este patrón encapsula las solicitudes de preparación como objetos, permitiendo parametrizar, encolar y ejecutar operaciones de manera desacoplada.

#### Implementación

- `Command` Es la interfaz del comando.
- `PrepararBebida` Corresponde al comando para preparar bebidas (ejecutado por el Barista)
- `PrepararAlimento` Sería el comando para preparar alimentos (ejecutado por el Pastelero)
- `Pedido` Invoker que almacena y ejecuta comandos

Ejemplo de uso en en el proyecto (clase main):

```python
    pedido_carlos = Pedido(carlos)
    pedido_carlos.agregar_comando(PrepararBebida(te1))
    pedido_carlos.agregar_comando(PrepararBebida(cafe2))
```

## Referencias

Patrones de diseño: [Refactoring Guru](https://refactoring.guru/design-patterns/catalog)


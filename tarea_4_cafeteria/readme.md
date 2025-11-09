# Cafetería con patrones de diseño - Javier Cruz C02517

## Descripción del proyecto

Este proyecto se trata de desarrollar un sistema de pedidos para una cafetería que permite a los clientes ordenar bebidas y comidas personalizadas.

## Patrones de diseño elegidos

### Patrón Decorator

Decorador es un patrón de diseño estructural que permite agregar nuevas funciones a objetos al agregar los mismos a *wrappers* especiales qeu contienen dichas funciones. 

Se decidió utilizar este patrón de diseño ya que permite agregar funciones y personalización a las bebidas y alimentos de manera flexible sin afectar las clases base. 

### Patrón Observer

Observer es un patrón de comportamiento que permite definir un mecanismo de *suscripción* para notificar a múltiples objetos sobre eventos que le ocurren al elemento que están observando. 

Se decició utilizar observer para notificar a los clientes cuando sus pedidos están listos.

### Patrón Command

Command es un patrón de comportamiento que transforma un *request* en un objeto que contiene la información de dicho request. Esto permite enviar requests como argumentos. 

Se decidió utilizar ya que este patrón encapsula las solicitudes de preparación como objetos, permitiendo parametrizar, encolar y ejecutar operaciones de manera desacoplada.

## Referencias

Patrones de diseño: [Refactoring Guru](https://refactoring.guru/design-patterns/catalog)


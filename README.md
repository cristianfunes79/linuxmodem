# [Modem IoT 4G de uso general] FIXME: Definir nombre
## Que es un [modem para IoT]? FIXME: Cambiar por el nuevo nombre

Es un modem pensado para aplicaciones tipicas de Internet of Things, donde se requiere enviar y recibir datos hacia y desde internet.
En particular utilizamos la red celular 4G para acceder a internet.
Cuenta con diversas interfaces de cominicacion:
+ USART
+ SPI
+ I2C

Permite utilizarse como AP: FIXME: Agregar figuras

EQUIPO_CLIENTE ---> INTERFAZ(UART,SPI,I2C) ---> MODEM ---> INTERNET

O como monitor: FIXME: Agregar figuras

SENSORES_CLIENTE ---> INTERFAZ_SENSORES ---> MODEM ---> INTERNET


Los usos como monitor abarcan distintas configuraciones:

+Datalogger
+Alarma
+Tracking GPS

## Finalidad del Proyecto
Facilitar la conexion de dispositivos a internet contando con una interfaz facil de utilizar y resolviendo tareas de backgroud comunes a la mayoria de los proyectos de aplicacion. 

## APIS 
Se dispone de APIs en:
+ C
+ C++
+ Python
+ Java :FIXME definir
+ C# :FIXME definir

## Distribucion
Clonar el repositorio desde: https://github.com/cristianfunes79/linuxmodem.git
Hacer un checkout al branch 'release'

## Contribuir
Para contribuir con el desarrollo del proyecto leer el archivo CONTRIBUTING.md

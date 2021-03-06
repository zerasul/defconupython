# defconupython
Defcon Wifi Signal With MicroPython



Señal de defcon con wifi integrado utilizando el ESP8266. Este proyecto utiliza la placa [Wemos D1 Mini](https://wiki.wemos.cc/products:d1:d1_mini).
Este código corresponde a la mejora de una señal defcon para la Oficina Técnica de Platino. Seguidamente se muestran la imagenes de pines de la Wemos D1 mini.

![Pinout](http://escapequotes.net/wp-content/uploads/2016/02/esp8266-wemos-d1-mini-pinout.png)

## Ejemplo de uso

Para poder cambiar el estado del defcon, nos conectaremos a la wifi que corresponde a este proyecto y nos conectaremos a la web correspondiente.
Que se encontará en la dirección http://192.168.4.1

![web](web.png)

Para cambiar de estado se selecciona el estado del formulario y se pulsa en enviar.

## Configuración

A partir de la versión _0.2_, existe un fichero llamado ```config.py``` donde existe una serie de variables de configuración que serán utilizados por el dispositivo.

Seguidamente se muestran las variables y para que se utiliza.

| Variable | descripcion |
| --- | ----------- |
| WIFI_MODE | Establece el modo de la wifi; puede ser "WIFIMODE_AP"(Modo punto de acceso) o "WIFIMODE_AS" (modo estación de acceso). |
| WIFI_ESSID | ESSID de la wifi de la que vamos a crear (modo AP) o conectar (modo AS). |
| WIFI_PASS | Clave de la wifi de la que vamos a crear (modo AP) o conectar (modo AS). |
| DEFCON_VERSION | Versión actual del software del dispositivo. |

## Lista de Pines

| pin | descripcion |
| --- | ----------- |
| D0 | Defcon 1 |
| D5 | Defcon 2 |
| D6 | Defcon 3 |
| D7 | Defcon 4 |
| D8 | Defcon 5 |
| V5 | Alimentación poner a 5 Voltios |
| GND | Tierra |
 

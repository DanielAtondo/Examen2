# Examen #2 Conexión TCP
_Se realizo un Servidor que maneja el protocolo TCP y permite la conexión de un cliente emisor y uno receptor._
![tcpserver](https://github.com/DanielAtondo/Examen2/blob/main/Imagenes/Conexi%C3%B3nTCP.png "Diagrama del modelo TCP Cliente-Servidor")
### Configuración de los microcontroladores
* Emisor: 
  * Descargar el Archivo "CodigoEmisor.ino".
  * Abrir el archivo en el IDE de Arduino.
  * En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.
  * Darle al boton de "Subir/Upload".
* Receptor
  * Descargar el Archivo "CodigoReceptor.ino".
  * Abrir el archivo en el IDE de Arduino.
  * En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.
  * Darle al boton de "Subir/Upload".
### Configuración del Servidor
En caso de tener un modem de INFINITUM ingresar a http://192.168.1.254/login.html y buscar el apartado "DMZ" (Demilitarized Zone ó Zona desmilitarizada) y activamos la función DMZ.<br>
Buscar el apartado "Mapeo de Puertos/Port Mapping" y una vez ahí en la sección "Reenvió de Puertos" definimos un puerto nuevo y especificamos que se trata de un Protocolo TCP.<br>
<strong>Nota:</strong> Es importante guardar los datos de la Dirección IP Pública.

### Fd


# Automatizacion Mundial XI - 8
Este programa hecho en python automatiza la subida
de registros de jugadores y equipos en la base de datos
de ejemplo en concreto las tablas de jugadores y la de
equipos basada en el mundial del 2018 <br/>

numero total de equipos que se registran: 32 <br/>
numero total de jugadores que se registran: 352
## Instrucciones:
* Primero necesitas descargar unas dependencias de python
con el siguiente comando:
`pip install pymysql`
y
`pip install requests`

* Luego edita el codigo para que tenga las mismas
credenciales que tu necesitas, por ejemplo el nombre
de la base de datos y las sentencias SQl, por ejemplo este pedazo
de codigo debes reemplazar el nombre de la base de la datos
por la tuya y tu user y password del MYSQL:
```
self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='mundial_seccion8'
        )
``` 
o por ejemplo esta sentencia debes cambiar en esta sentencia
el nombre tu tabla y el nombre los campos:

``` 
sql = "INSERT INTO equipos (idEquipo, nombreEquipo, grupo) 
VALUES ('{}', '{}', '{}');".format(id_equipo, nombre_equipo, grupo)
```
* Ejecuta el xampp y enciende el proceso de MySql 

* Luego debes ejecutar el archivo de python llamado main.py
(es el unico archivo que hay xd)

* Al final verifica los registros que se crearon en tu base de datos
con el siguiente comando en MySql Workbench o PhpMyAdmin

`SELECT * FROM AquiVaElNombreDeTuTablaDeJugadoresOEquipo;`

Cualquier duda, problema o error pueden escribirme para guiarlos
con esto
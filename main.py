import pymysql
import requests

#urls de API'S que traen la informacion
URL_JUGADORES = 'https://world-cup-json-2018.herokuapp.com/matches'
URL_EQUIPOS = 'https://world-cup-json-2018.herokuapp.com/teams'

#Clase de la base de datos para manipularla
class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='mundial_seccion8'
        )

        self.cursor = self.connection.cursor()
        print('Conexion establecida correctamente')
    def select_sede(self):
        sql = 'SELECT * FROM sedes;'
        try:
            self.cursor.execute(sql)
            sedes = self.cursor.fetchall()
            print(sedes)
        except Exception as err:
            raise
    def select_equipo(self, nombre_equipo):
        sql = "SELECT * FROM equipos WHERE nombreEquipo = '{}';".format(nombre_equipo)
        try:
            self.cursor.execute(sql)
            equipo = self.cursor.fetchone()
            return equipo
        except Exception as err:
            raise

    def insertar_equipos(self, id_equipo, nombre_equipo, grupo):
        sql = "INSERT INTO equipos (idEquipo, nombreEquipo, grupo) VALUES ('{}', '{}', '{}');".format(id_equipo, nombre_equipo, grupo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            raise

    def insert_jugadores(self, id_jugador, nombre_jugador, posicion, id_equipo):
        sql = "INSERT INTO jugadores (idJugadore, nombreJugador, idEquipo, posicion) VALUES ('{}', '{}', '{}', '{}')".format(id_jugador, nombre_jugador, id_equipo, posicion)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            raise

database = Database()

def obtener_equipos(url, database):
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        for i in range(len(response_json)):
            id_equipo = response_json[i]['id']
            nombre_equipo = response_json[i]['country']
            grupo = response_json[i]['group_letter']
            database.insertar_equipos(id_equipo, nombre_equipo, grupo)

def obtener_jugadores(url, database):
    countrys = []
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        for i in range(len(response_json)):
            datos = response_json[i]
            datos_concretos = datos['home_team_statistics']
            extra_id = 0
            if datos_concretos['country'] not in countrys:
                current_equipo = database.select_equipo(datos_concretos['country'])
                countrys.append(datos_concretos['country'])
                for x in range(len(datos_concretos['starting_eleven'])):
                    currentJugador = datos_concretos['starting_eleven'][x]
                    id_jugador = int(str(current_equipo[0]) + str(currentJugador['shirt_number']) + str(extra_id))
                    database.insert_jugadores(id_jugador, str(currentJugador['name']), str(currentJugador['position']), int(current_equipo[0]))
                    extra_id += 1
            else:
                continue

    else:
        print('Error con el API')

obtener_equipos(URL_EQUIPOS, database)
obtener_jugadores(URL_JUGADORES, database)

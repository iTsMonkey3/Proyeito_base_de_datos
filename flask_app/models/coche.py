from flask_app.models import user, compra
from flask_app.config.postgresqlconnection import connectToPostgreSQL
from flask import flash
import re
from flask_app import app


class Coche:
    db_name = 'legendaryMotosport'
    def __init__(self, data):
        self.id_coche = data['id_coche']
        self.matricula = data['matricula']
        self.modelo = data['modelo']
        self.marca = data['marca']
        self.color = data['color']
        self.kilometraje = data['kilometraje']
        self.precio = data['precio']
        self.age = data['age']
        self.velocidadmax = data['velocidadmax']
        self.acelera_0_100 = data['acelera_0_100']
        self.consu_urb = data['consu_urb']
        self.consu_ext = data['consu_ext']
        self.consu_mix = data['consu_mix']
        self.co2_emis = data['co2_emis']
        self.carroceria = data['carroceria']
        self.num_puertas = data['num_puertas']
        self.num_plazas = data['num_plazas']
        self.depositol = data['depositol']
        self.combustible = data['combustible']
        self.num_cilindros = data['num_cilindros']
        self.disposicion_cil = data['disposicion_cil']
        self.transmision = data['transmision']
        self.num_velocidades = data['num_velocidades']
        self.traccion = data['traccion']
        self.vendedor = None
    
    @classmethod
    def add_coche(cls, data):
        query = """
        INSERT INTO coches 
        (matricula, modelo, marca, color, kilometraje, precio, age, velocidadmax, acelera_0_100, consu_urb, consu_ext, consu_mix, co2_emis, carroceria, num_puertas, 
        num_plazas, depositol, combustible, num_cilindros, disposicion_cil, transmision, num_velocidades, traccion, vendedor) 
        VALUES
        (%(matricula)s,%(modelo)s,%(marca)s,%(color)s,%(kilometraje)s,%(precio)s,%(age)s,%(velocidadmax)s,%(acelera_0_100)s,%(consu_urb)s,%(consu_ext)s,%(consu_mix)s,
        %(co2_emis)s,%(carroceria)s,%(num_puertas)s,%(num_plazas)s,%(depositol)s,%(combustible)s,%(num_cilindros)s,%(disposicion_cil)s,
        %(transmision)s,%(num_velocidades)s,%(traccion)s,%(vendedor)s);"""
        return connectToPostgreSQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def mostrar_coches(cls):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query)

        if len(resultados) == 0:
            return []
        else:
            todos_coches = []

            for coche_act in resultados:
                coche_obj = Coche(coche_act)
                usuario_dic={
                    "id_usuario": coche_act["id_usuario"],
                    "email": coche_act["email"],
                    "password": coche_act["password"],
                    "nombre": coche_act["nombre"],
                    "apellidopat": coche_act["apellidopat"],
                    "apellidomat": coche_act["apellidomat"],
                    "colonia": coche_act["colonia"],
                    "calle": coche_act["calle"],
                    "numerointerior": coche_act["numerointerior"],
                    "cp": coche_act["cp"],
                    "telefono": coche_act["telefono"]
                }

                usuario_obj = user.User(usuario_dic)
                coche_obj.vendedor = usuario_obj
                todos_coches.append(coche_obj)

            return todos_coches
        
    @classmethod
    def mostrar_coches_caros_a_baratos(cls):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario ORDER BY coches.precio DESC;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query)

        if len(resultados) == 0:
            return []
        else:
            todos_coches_caro_a_barato = []

            for coche_act in resultados:
                coche_obj = Coche(coche_act)
                usuario_dic={
                    "id_usuario": coche_act["id_usuario"],
                    "email": coche_act["email"],
                    "password": coche_act["password"],
                    "nombre": coche_act["nombre"],
                    "apellidopat": coche_act["apellidopat"],
                    "apellidomat": coche_act["apellidomat"],
                    "colonia": coche_act["colonia"],
                    "calle": coche_act["calle"],
                    "numerointerior": coche_act["numerointerior"],
                    "cp": coche_act["cp"],
                    "telefono": coche_act["telefono"]
                }

                usuario_obj = user.User(usuario_dic)
                coche_obj.vendedor = usuario_obj
                todos_coches_caro_a_barato.append(coche_obj)

            return todos_coches_caro_a_barato
        
    @classmethod
    def mostrar_coches_baratos_a_caros(cls):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario ORDER BY coches.precio ASC;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query)

        if len(resultados) == 0:
            return []
        else:
            todos_coches_barato_a_caro = []

            for coche_act in resultados:
                coche_obj = Coche(coche_act)
                usuario_dic={
                    "id_usuario": coche_act["id_usuario"],
                    "email": coche_act["email"],
                    "password": coche_act["password"],
                    "nombre": coche_act["nombre"],
                    "apellidopat": coche_act["apellidopat"],
                    "apellidomat": coche_act["apellidomat"],
                    "colonia": coche_act["colonia"],
                    "calle": coche_act["calle"],
                    "numerointerior": coche_act["numerointerior"],
                    "cp": coche_act["cp"],
                    "telefono": coche_act["telefono"]
                }

                usuario_obj = user.User(usuario_dic)
                coche_obj.vendedor = usuario_obj
                todos_coches_barato_a_caro.append(coche_obj)

            return todos_coches_barato_a_caro
    
    @classmethod
    def mostrar_coches_marcas(cls):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario ORDER BY coches.marca ASC;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query)

        if len(resultados) == 0:
            return []
        else:
            todos_coches_marca = []

            for coche_act in resultados:
                coche_obj = Coche(coche_act)
                usuario_dic={
                    "id_usuario": coche_act["id_usuario"],
                    "email": coche_act["email"],
                    "password": coche_act["password"],
                    "nombre": coche_act["nombre"],
                    "apellidopat": coche_act["apellidopat"],
                    "apellidomat": coche_act["apellidomat"],
                    "colonia": coche_act["colonia"],
                    "calle": coche_act["calle"],
                    "numerointerior": coche_act["numerointerior"],
                    "cp": coche_act["cp"],
                    "telefono": coche_act["telefono"]
                }

                usuario_obj = user.User(usuario_dic)
                coche_obj.vendedor = usuario_obj
                todos_coches_marca.append(coche_obj)

            return todos_coches_marca
        
    @classmethod
    def mostrar_coches_anio(cls):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario ORDER BY coches.age DESC;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query)

        if len(resultados) == 0:
            return []
        else:
            todos_coches_anio = []

            for coche_act in resultados:
                coche_obj = Coche(coche_act)
                usuario_dic={
                    "id_usuario": coche_act["id_usuario"],
                    "email": coche_act["email"],
                    "password": coche_act["password"],
                    "nombre": coche_act["nombre"],
                    "apellidopat": coche_act["apellidopat"],
                    "apellidomat": coche_act["apellidomat"],
                    "colonia": coche_act["colonia"],
                    "calle": coche_act["calle"],
                    "numerointerior": coche_act["numerointerior"],
                    "cp": coche_act["cp"],
                    "telefono": coche_act["telefono"]
                }

                usuario_obj = user.User(usuario_dic)
                coche_obj.vendedor = usuario_obj
                todos_coches_anio.append(coche_obj)

            return todos_coches_anio
        
    @classmethod
    def tomar_coche(cls, data):
        query = """
        SELECT * FROM coches JOIN usuarios ON coches.vendedor = id_usuario WHERE coches.id_coche = %(id_coche)s;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query, data)

        if len(resultados) == 0:
            return None
        else:
            coche_obj = Coche(resultados[0])
            usuario_dic={
                    "id_usuario": resultados[0]["id_usuario"],
                    "email": resultados[0]["email"],
                    "password": resultados[0]["password"],
                    "nombre": resultados[0]["nombre"],
                    "apellidopat": resultados[0]["apellidopat"],
                    "apellidomat": resultados[0]["apellidomat"],
                    "colonia": resultados[0]["colonia"],
                    "calle": resultados[0]["calle"],
                    "numerointerior": resultados[0]["numerointerior"],
                    "cp": resultados[0]["cp"],
                    "telefono": resultados[0]["telefono"]
                }
            
            usuario_obj = user.User(usuario_dic)
            coche_obj.vendedor = usuario_obj

        return coche_obj
    
    @classmethod
    def modificar_coche(cls, data):
        query = """
        UPDATE coches SET matricula=%(matricula)s, modelo=%(modelo)s, marca=%(marca)s, color=%(color)s, kilometraje=%(kilometraje)s, precio=%(precio)s, 
        age=%(age)s, velocidadmax=%(velocidadmax)s, acelera_0_100=%(acelera_0_100)s, consu_urb=%(consu_urb)s, consu_ext=%(consu_ext)s, consu_mix=%(consu_mix)s, 
        co2_emis=%(co2_emis)s, carroceria=%(carroceria)s, num_puertas=%(num_puertas)s, num_plazas=%(num_plazas)s, depositol=%(depositol)s, combustible=%(combustible)s, 
        num_cilindros=%(num_cilindros)s, disposicion_cil=%(disposicion_cil)s, transmision=%(transmision)s, num_velocidades=%(num_velocidades)s, traccion=%(traccion)s WHERE id_coche = %(id_coche)s;
        """
        return connectToPostgreSQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def eliminar_coche(cls,data):
        query = """
        DELETE FROM coches WHERE id_coche = %(id_coche)s;
        """
        return connectToPostgreSQL(cls.db_name).query_db(query, data)
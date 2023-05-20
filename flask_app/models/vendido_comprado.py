from flask_app.models import user, coche
from flask_app.config.postgresqlconnection import connectToPostgreSQL
from flask import flash
import re
from flask_app import app

class Vendido_Comprado:
    db_name = 'legendaryMotosport'
    def __init__(self, data):
        self.matricula = data['matricula']
        self.modelo = data['modelo']
        self.marca = data['marca']
        self.precio = data['precio']
        self.nombre = data['nombre']
        self.apellidopat = data['apellidopat']
        self.telefono = data['telefono']
        self.fecha = data['fecha']

    @classmethod
    def mostrar_orden_vendido(cls, data):
        #Este es el id de la sesion que esta iniciada
        query = """

        SELECT ficha_comven.matricula AS matricula, 
        ficha_comven.modelo, 
        ficha_comven.marca,
        ficha_comven.precio,
        usuarios.nombre,
        usuarios.apellidopat,
        usuarios.telefono,
        ficha_comven.fecha
        FROM ficha_comven 
        JOIN usuarios ON ficha_comven.comprador_id = usuarios.id_usuario 
        WHERE vendedor_id = %(id)s;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query,data)

        if len(resultados)==0:
            return []
        else:
            orden_obj = []

            for orden_act in resultados:
                orden_obj.append(Vendido_Comprado(orden_act))
            
            return orden_obj
        
    @classmethod
    def mostrar_orden_comprado(cls, data):
        #Este es el id de la sesion que esta iniciada
        query = """

        SELECT ficha_comven.matricula AS matricula, 
        ficha_comven.modelo, 
        ficha_comven.marca,
        ficha_comven.precio,
        usuarios.nombre,
        usuarios.apellidopat,
        usuarios.telefono,
        ficha_comven.fecha
        FROM ficha_comven 
        JOIN usuarios ON ficha_comven.vendedor_id = usuarios.id_usuario 
        WHERE comprador_id = %(id)s;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query,data)

        if len(resultados)==0:
            return []
        else:
            orden_obj = []

            for orden_act in resultados:
                orden_obj.append(Vendido_Comprado(orden_act))
            
            return orden_obj
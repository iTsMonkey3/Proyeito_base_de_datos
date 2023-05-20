from flask_app.models import user, coche
from flask_app.config.postgresqlconnection import connectToPostgreSQL
from flask import flash
import re
from flask_app import app

class Compra:
    db_name = 'legendaryMotosport'
    def __init__(self, data):
        self.num_orden = data['num_orden']
        self.matricula = data['matricula']
        self.modelo = data['modelo']
        self.marca = data['marca']
        self.precio = data['precio']
        self.comprador_id = data['comprador_id']
        self.vendedor_id = data['vendedor_id']
        self.fecha = data['fecha']

    @classmethod
    def crear_orden(cls,data):
        query = """
        WITH deleted_coches AS (
        DELETE FROM coches WHERE id_coche = %(id_coche)s RETURNING *
        )
        INSERT INTO ficha_comven (matricula, modelo, marca, precio, comprador_id, vendedor_id) VALUES ( %(matricula)s, %(modelo)s, %(marca)s, %(precio)s, %(comprador_id)s, %(vendedor_id)s);
        """
        return connectToPostgreSQL(cls.db_name).query_db(query, data)
    
   

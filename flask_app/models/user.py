from flask_app.models import coche
from flask_app.config.postgresqlconnection import connectToPostgreSQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = 'legendaryMotosport'
    def __init__(self, data):
        self.id_usuario = data['id_usuario']
        self.email = data['email']
        self.password = data['password']
        self.nombre = data['nombre']
        self.apellidopat = data['apellidopat']
        self.apellidomat = data['apellidomat']
        self.colonia = data['colonia']
        self.calle = data['calle']
        self.numerointerior = data['numerointerior']
        self.cp = data['cp']
        self.telefono = data['telefono']
        self.publicados = []

    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO usuarios (email, password, nombre, apellidopat, apellidomat, colonia, calle, numerointerior, cp, telefono)
        VALUES (%(email)s,%(password)s,%(nombre)s,%(apellidopat)s,%(apellidomat)s,%(colonia)s,%(calle)s,%(numerointerior)s,%(cp)s,%(telefono)s)
        ;"""
        return connectToPostgreSQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = """
        SELECT * FROM usuarios
        WHERE email = %(email)s
        ;"""
        results = connectToPostgreSQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            print('-----> Results', results[0])
            return cls(results[0])
        
    @classmethod
    def get_user_by_id(cls, data):
        query = """
        SELECT * FROM usuarios
        WHERE id_usuario = %(id)s
        ;"""
        results = connectToPostgreSQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            print('-----> Results', results[0])
            return cls(results[0])
        
    @staticmethod
    def validate_signup(form_data):
        is_valid = True
        if len(form_data['nombre']) < 3:
            flash('nombre must be 3 character or more', 'register')
            is_valid = False
        if form_data['nombre'].isalpha() == False and form_data['nombre'] != '':
            flash('nombre field only accepts letters', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash('Invalid email address', 'register')
            is_valid = False
        data = {
            'email': form_data['email']
        }
        is_user_found = User.get_user_by_email(data)
        if is_user_found != None:
            flash('Email is already taken', 'register')
            is_valid = False
        if len(form_data['password']) < 8:
            flash('Password must be 8 characters or more', 'register')
            is_valid = False
        if not form_data['password'] == form_data['confirm_password']:
            flash("Passwords don't match", 'register')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(form_data):
        if not EMAIL_REGEX.match(form_data['email']):
            flash('Invalid log in credentials', 'login')
            return False
        data = {
            'email': form_data['email']
        }
        is_user_found = User.get_user_by_email(data)
        if is_user_found == None:
            flash('Invalid log in credentials', 'login')
            return False
        if not bcrypt.check_password_hash(is_user_found.password, form_data['password']):
            flash('Invalid log in credentials', 'login')
            return False
        return is_user_found
    
    @classmethod
    def usuarios_coches(cls, data):
        query = """
        SELECT * FROM usuarios JOIN coches ON id_usuario = coches.vendedor WHERE id_usuario = %(id)s;
        """
        resultados = connectToPostgreSQL(cls.db_name).query_db(query,data)

        if len(resultados)==0:
            return None
        else:
            usuario_obj = User(resultados[0])

            for coches_total in resultados:
                coches_dic = {
                    "id_coche": coches_total["id_coche"],
                    "matricula": coches_total["matricula"],
                    "modelo": coches_total["modelo"],
                    "marca": coches_total["marca"],
                    "color": coches_total["color"],
                    "kilometraje": coches_total["kilometraje"],
                    "precio": coches_total["precio"],
                    "age": coches_total["age"],
                    "velocidadmax": coches_total["velocidadmax"],
                    "acelera_0_100": coches_total["acelera_0_100"],
                    "consu_urb": coches_total["consu_urb"],
                    "consu_ext": coches_total["consu_ext"],
                    "consu_mix": coches_total["consu_mix"],
                    "co2_emis": coches_total["co2_emis"],
                    "carroceria": coches_total["carroceria"],
                    "num_puertas": coches_total["num_puertas"],
                    "num_plazas": coches_total["num_plazas"],
                    "depositol": coches_total["depositol"],
                    "combustible": coches_total["combustible"],
                    "num_cilindros": coches_total["num_cilindros"],
                    "disposicion_cil": coches_total["disposicion_cil"],
                    "transmision": coches_total["transmision"],
                    "num_velocidades": coches_total["num_velocidades"],
                    "traccion": coches_total["traccion"]
                }

                coche_obj = coche.Coche(coches_dic)
                usuario_obj.publicados.append(coche_obj)

            return usuario_obj
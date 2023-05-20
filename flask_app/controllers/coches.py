from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, coche, compra

@app.route('/success')
def success():
    data = {
        'id': session['user_id']
    }
    return render_template('success.html', logged_user=user.User.get_user_by_id(data), 
                           todos_los_coches=coche.Coche.mostrar_coches(), 
                           todos_coches_caro_a_barato=coche.Coche.mostrar_coches_caros_a_baratos(), 
                           todos_coches_barato_a_caro=coche.Coche.mostrar_coches_baratos_a_caros(), 
                           todos_coches_marca=coche.Coche.mostrar_coches_marcas(), 
                           todos_coches_anio=coche.Coche.mostrar_coches_anio(),
                           rutas_fotos=['../static/imagenes/1','../static/imagenes/2','../static/imagenes/3','../static/imagenes/4','../static/imagenes/5'])

@app.route('/registro_coche')
def registro_coche():
    return render_template('registro_coche2.html')

@app.route('/ingresar_coche_db', methods=["POST"])
def ingresar_coche_db():
    data = {
        "matricula": request.form['matricula'],
        "modelo": request.form["modelo"],
        "marca": request.form["marca"],
        "color": request.form["color"],
        "kilometraje": request.form["kilometraje"],
        "precio": request.form["precio"],
        "age": request.form["age"],
        "velocidadmax": request.form["velocidadmax"],
        "acelera_0_100": request.form["acelera_0_100"],
        "consu_urb": request.form["consu_urb"],
        "consu_ext": request.form["consu_ext"],
        "consu_mix": request.form["consu_mix"],
        "co2_emis": request.form["co2_emis"],
        "carroceria": request.form["carroceria"],
        "num_puertas": request.form["num_puertas"],
        "num_plazas": request.form["num_plazas"],
        "depositol": request.form["depositol"],
        "combustible": request.form["combustible"],
        "num_cilindros": request.form["num_cilindros"],
        "disposicion_cil": request.form["disposicion_cil"],
        "transmision": request.form["transmision"],
        "num_velocidades": request.form["num_velocidades"],
        "traccion": request.form["traccion"],
        "vendedor": session["user_id"]
    }

    coche.Coche.add_coche(data)
    return redirect("/success")

@app.route('/detalle/<int:id_coche>')
def detalle_coche(id_coche):
    data_coche = {
        "id_coche": id_coche
    }
    return render_template('detalle_coche.html',coche_obj=coche.Coche.tomar_coche(data_coche))

@app.route('/mis_coches')
def mis_coches():
    data = {
        'id': session['user_id']
    }
    return render_template('mis_coches.html',usuario_obj=user.User.usuarios_coches(data))

@app.route('/modificar_coche/<int:id_coche>')
def modificar_coche(id_coche):
    data_coche = {
        "id_coche": id_coche
    }
    return render_template('modificar_coches.html',coche_obj=coche.Coche.tomar_coche(data_coche))

@app.route('/modificar_coche_db/<int:id_coche>', methods=["POST"])
def modificar_coche_db(id_coche):
    data = {
            "matricula": request.form['matricula'],
            "modelo": request.form["modelo"],
            "marca": request.form["marca"],
            "color": request.form["color"],
            "kilometraje": request.form["kilometraje"],
            "precio": request.form["precio"],
            "age": request.form["age"],
            "velocidadmax": request.form["velocidadmax"],
            "acelera_0_100": request.form["acelera_0_100"],
            "consu_urb": request.form["consu_urb"],
            "consu_ext": request.form["consu_ext"],
            "consu_mix": request.form["consu_mix"],
            "co2_emis": request.form["co2_emis"],
            "carroceria": request.form["carroceria"],
            "num_puertas": request.form["num_puertas"],
            "num_plazas": request.form["num_plazas"],
            "depositol": request.form["depositol"],
            "combustible": request.form["combustible"],
            "num_cilindros": request.form["num_cilindros"],
            "disposicion_cil": request.form["disposicion_cil"],
            "transmision": request.form["transmision"],
            "num_velocidades": request.form["num_velocidades"],
            "traccion": request.form["traccion"],
            "id_coche": id_coche
        }
    coche.Coche.modificar_coche(data)
    return redirect('/success')

@app.route('/eliminar_coche_db/<int:id_coche>')
def eliminar_coche_db(id_coche):
    data = {
        "id_coche": id_coche
    }
    coche.Coche.eliminar_coche(data)
    return redirect('/success')
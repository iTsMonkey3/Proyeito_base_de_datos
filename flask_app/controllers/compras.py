from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, coche, compra

@app.route('/compra/<int:id_coche>')
def compra_coche(id_coche):
    data = {
        'id': session['user_id']
    }
    data_coche = {
        "id_coche": id_coche
    }
    return render_template('compra_coche.html', logged_user=user.User.get_user_by_id(data), coche_obj=coche.Coche.tomar_coche(data_coche))

@app.route('/registrar_compra_db', methods=["POST"])
def registrar_compra_db():
    data = {
        "id_coche": request.form['id_coche'],
        "matricula": request.form['matricula'],
        "modelo": request.form['modelo'],
        "marca": request.form['marca'],
        "precio": request.form['precio'],
        "comprador_id": request.form['comprador_id'],
        "vendedor_id": request.form['vendedor_id']
    }

    compra.Compra.crear_orden(data)
    return redirect("/success")
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, coche, compra, vendido_comprado

@app.route('/mis_ventas')
def mis_ventas():
    data = {
        'id': session['user_id']
    }
    return render_template('mis_ventas.html',orden_obj=vendido_comprado.Vendido_Comprado.mostrar_orden_vendido(data))

@app.route('/mis_compras')
def mis_compras():
    data = {
        'id': session['user_id']
    }
    return render_template('mis_compras.html',orden_obj=vendido_comprado.Vendido_Comprado.mostrar_orden_comprado(data))
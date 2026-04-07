from flask import render_template, request
from main import app
import database
import models


@app.route('/')
def index():
    dogs_data = database.get_available_dogs()
    available_dogs = [models.Dog(row[0], row[1], row[2], row[3]) for row in dogs_data]

    return render_template('catalogo.html', dogs=available_dogs)


@app.route('/adoptar/<int:dog_id>')
def form_adopcion(dog_id):
    dog = database.get_dog_by_id(dog_id)

    if not dog:
        return "Perrito no encontrado", 404

    dog_obj = models.Dog(dog[0], dog[1], dog[2], dog[3])
    return render_template('confirmacion.html', dog=dog_obj)


@app.route('/confirmar_adopcion', methods=['POST'])
def procesar_adopcion():

    dog_id = request.form['dog_id']
    name = request.form['name']
    lastname = request.form['lastname']
    address = request.form['address']
    id_card = request.form['id_card']

    success = database.register_adoption_transactional(
        dog_id, name, lastname, address, id_card
    )

    if success:
        dog = database.get_dog_by_id(dog_id)
        return f"<h1>¡Felicidades! Has adoptado a {dog[1]} exitosamente.</h1><a href='/'>Volver al catálogo</a>"
    else:
        return "Error al procesar la adopción. Por favor, inténtalo de nuevo."
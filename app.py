#Se importa la clase Flask de la biblioteca Flask.
from flask import Flask, jsonify

#Se crea una instancia de la aplicación Flask llamada app.
app = Flask(__name__)

# Lista de nombres de personas
personas = ['Yair', 'Mari', 'Liam', 'Ana']

#Se define una función de vista obtener_personas() que responde a las solicitudes GET en el endpoint '/personas'. Esta función retorna la lista de nombres de personas en formato JSON utilizando la función jsonify() de Flask.
@app.route('/personas', methods=['GET'])
def obtener_personas():
    return jsonify(personas)
#si el script es ejecutado directamente (__name__ == '__main__'), la aplicación Flask se ejecuta en modo de depuración (debug=True).
if __name__ == '__main__':
    app.run(debug=True)

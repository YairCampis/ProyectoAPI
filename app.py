<<<<<<< HEAD
from flask import Flask, jsonify #Se importa la clase Flask de la biblioteca Flask.

app = Flask(__name__) #Se crea una instancia de la aplicación Flask llamada app.
=======
#Se importa la clase Flask de la biblioteca Flask.
from flask import Flask, jsonify

#Se crea una instancia de la aplicación Flask llamada app.
app = Flask(__name__)
>>>>>>> 448656ea8e7fd00e937a349505e7c3e184aa8278

# Lista de nombres de personas
personas = ['Yair', 'Mari', 'Liam', 'Ana']

<<<<<<< HEAD
@app.route('/personas', methods=['GET']) #Se define una función de vista obtener_personas() que responde a las solicitudes GET en el endpoint '/personas'. Esta función retorna la lista de nombres de personas en formato JSON utilizando la función jsonify() de Flask.
def obtener_personas():
    return jsonify(personas)

if __name__ == '__main__': #si el script es ejecutado directamente (__name__ == '__main__'), la aplicación Flask se ejecuta en modo de depuración (debug=True).
=======
#Se define una función de vista obtener_personas() que responde a las solicitudes GET en el endpoint '/personas'. Esta función retorna la lista de nombres de personas en formato JSON utilizando la función jsonify() de Flask.
@app.route('/personas', methods=['GET'])
def obtener_personas():
    return jsonify(personas)
#si el script es ejecutado directamente (__name__ == '__main__'), la aplicación Flask se ejecuta en modo de depuración (debug=True).
if __name__ == '__main__':
>>>>>>> 448656ea8e7fd00e937a349505e7c3e184aa8278
    app.run(debug=True)

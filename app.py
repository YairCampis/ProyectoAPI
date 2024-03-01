from flask import Flask, jsonify

app = Flask(__name__)

# Lista de nombres de personas
personas = ['Yair', 'Mari', 'Liam', 'Ana']

@app.route('/personas', methods=['GET'])
def obtener_personas():
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)

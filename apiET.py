from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/et-phone-home', methods=['POST'])
def et_phone_home():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Mensaje no encontrado en la solicitud."}), 400

    message = data['message']
    if message == "E.T. está en casa!":
        return jsonify({"response": "Mensaje recibido. ¡Feliz Navidad desde el planeta de E.T.!"})
    else:
        return jsonify({"response": "Mensaje incorrecto. Intenta de nuevo."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

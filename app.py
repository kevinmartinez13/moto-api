from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route('/api/registros')
def get_registros():
      return jsonify({
		"status": "online",
		"servidor":("ubuntu de KEVIN YOEL MARTINEZ CLAVIJO"),
		"hora_servidor": str(datetime.datetime.now()),
		"inventario ":  ["Yamaha_MT-07","Honda_CB500","susuki","susuki","yANHANA_MT-07"]
	})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)

@app.route('/api/repuestos', methods=['GET'])
def get_repuestos():
@app.route('/api/peritajes', methods=['POST'])
def registrar_peritaje():
    from flask import request
    datos = request.get_json()

    # FORZAR FORMATEO A MAYÚSCULAS ESTRICTAS (Solución del Bug)
    placa_recibida = datos.get('placa', '')
    placa_procesada = placa_recibida.upper()

    return jsonify({
        "status": "Peritaje registrado con exito",
        "placa_guardada": placa_procesada
    })

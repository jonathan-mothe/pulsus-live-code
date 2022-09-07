from flask import Flask, jsonify, Response, request # Importa e cria o app (até linha 4)

from models import *
import json


#app = Flask(__name__)


@app.route('/devices')
def get_devices():
    device = Device.query.all()
    device_json = [item.to_json() for item in device]

    return gera_response(200, 'devices', device_json)


@app.route('/devices/add', methods=['POST'])
def add_devices():
    body = request.get_json()

    try:
        device = Device(id=body['id'], location_lat=body['location_lat'], location_long=body['location_long'])
        db.session.add(device)
        db.session.commit()
        return gera_response(201, 'device', device.to_json(), 'Dispositivo adicionado')
    except Exception as e:
        print('Erro', e)
        return gera_response(400, 'device', {}, "Erro ao cadastrar")



def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body['mensagem'] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)

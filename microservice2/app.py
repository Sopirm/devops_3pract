from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        response = requests.get('http://microservice1:5001/')
        microservice1_message = response.json()['message']
    except requests.exceptions.ConnectionError:
        microservice1_message = 'Не удалось связаться с первым микросервисом.'
    return jsonify(message=f'Привет от второго микросервиса! Первый микросервис сказал: {microservice1_message}', json_as_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

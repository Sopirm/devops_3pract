import requests

def test_microservice(port, name):
    try:
        response = requests.get(f'http://localhost:{port}')
        print(f'{name} ({port}): {response.json()}')
    except requests.exceptions.ConnectionError:
        print(f'Не удалось подключиться к {name} на порту {port}.')

if __name__ == '__main__':
    test_microservice(5001, 'Микросервис 1')
    test_microservice(5002, 'Микросервис 2')

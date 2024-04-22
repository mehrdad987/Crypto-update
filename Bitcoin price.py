import requests
from flask import Flask

app = Flask(__name__)

def get_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data['bpi']['USD']['rate']

@app.route('/')
def index():
    bitcoin_price = get_bitcoin_price()
    return f'The current Bitcoin price is: {bitcoin_price} USD'

if __name__ == '__main__':
    app.run()

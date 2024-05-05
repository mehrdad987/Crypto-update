import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data['bpi']['USD']['rate']

@app.route('/')
def index():
    bitcoin_price = get_bitcoin_price()
    return render_template('bitcoin_price.html', bitcoin_price=bitcoin_price)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
from xml.etree import ElementTree

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    moeda = None
    
    currency = get_currency()
    
    if request.method == 'POST':
        valor = request.form['valor']
        para = request.form['para']
        de = request.form['de']
        convert = convert_coin(de, para, valor)
        
        moeda = convert[0]['bid']
            
    return render_template('index.html', error= error, moeda= moeda, currency= currency)

def convert_coin(de, para, valor):
    url = "https://economia.awesomeapi.com.br/BRL-USD/1"

    response = requests.request("GET", url)

    return response.json()

def get_currency():
    url = "https://economia.awesomeapi.com.br/xml/available/uniq"
    

    response = requests.request("GET", url)

    result = ElementTree.fromstring(response.text)
    return result
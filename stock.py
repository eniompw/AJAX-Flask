import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('stock.html')

@app.route('/ajax')
def ajax():
    # https://www.pythonanywhere.com/whitelist
    req = requests.get('https://finance.yahoo.com/quote/HSBA.L',timeout=10)
    pos = req.text.find("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    extract = req.text[pos+61:pos+67]
    return extract

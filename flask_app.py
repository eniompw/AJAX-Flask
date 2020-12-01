from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ajax.html')

@app.route('/helloname')
def hn():
    name = request.args.get('q', '')
    return 'hello ' + name

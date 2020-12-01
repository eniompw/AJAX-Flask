from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '/ajax'

@app.route('/ajax')
def ajax():
    return render_template('ajax.html')

@app.route('/bookingid')
def bid():
    name = request.args.get('q', '')
    return 'hello ' + name

from flask import Flask, request, render_template
from scvToAdjList import convert 

app = Flask(__name__)

@app.route('/')
def index():
    colors = ['red','green','blue','orange']
    carModels = ['Audi','Mercedes','BMW']
    return render_template('index.html', colors=colors, cars=carModels)

@app.route('/api', methods=['POST'])
def api():
    color = request.form['color']
    car = request.form['car']
    return f'A {color} {car}, coming right up...'

@app.route('/car-shop')
def cars():
    colors = ['red','green','blue','orange']
    carModels = ['Audi','Mercedes','BMW']
    return render_template('car-shop.html', colors=colors, cars=carModels)

@app.route('/car-factory', methods=['POST'])
def carShop():
    color = request.form['color']
    car = request.form['car']
    return f'A {color} {car}, coming right up...'

@app.route('/adj')
def adj():
    result = convert()
    return result




if __name__ == '__main__':
    app.run(host='localhost', port=9874)
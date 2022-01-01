from io import BytesIO
from flask import Flask, request, render_template, send_file
from scvToAdjList import convert 
from mapper import getSchoolPath, getMap, getSchoolPlaces, getBlankMap, getTownPath, getTownPlaces

app = Flask(__name__)

@app.route('/')
def index():
    places = getTownPlaces()
    return render_template('index.html', places=places)

@app.route('/town-mapper', methods=['POST'])
def townMapper():
    start = request.form['start']
    end = request.form['end']
    path = getTownPath(start,end)
    return str(path)

@app.route('/school')
def school():
    places = getSchoolPlaces()
    return render_template('school.html', places=places)

# https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
@app.route('/blank-map')
def blankMap():
    filename = getBlankMap()
    return send_file(filename, mimetype='image/gif')

@app.route('/school-mapper', methods=['POST'])
def schoolMapper():
    start = request.form['start']
    end = request.form['end']
    path = getSchoolPath(start,end)
    filename = getMap(path)
    return send_file(filename, mimetype='image/gif')

@app.route('/sample-path')
def samplePath():
    places = getSchoolPlaces()
    path = [(places[0],places[2]),(places[2],places[1])]
    filename = getMap(path)
    return send_file(filename, mimetype='image/gif')

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
    result = convert('school-graph.csv')
    return result

if __name__ == '__main__':
    app.run(host='localhost', port=9874)
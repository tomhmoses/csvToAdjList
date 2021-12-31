from flask import Flask, request, render_template, send_file
from scvToAdjList import convert 
from mapper import getPath, getMap, getPlaces, getBlankMap

app = Flask(__name__)

@app.route('/')
def index():
    places = getPlaces()
    return render_template('index.html', places=places)

# https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
@app.route('/blank-map')
def blankMap():
    filename = getBlankMap()
    return send_file(filename, mimetype='image/gif')

@app.route('/mapper', methods=['POST'])
def mapper():
    start = request.form['start']
    end = request.form['end']
    path = getPath(start,end)
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
    result = convert()
    return result

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    # img_io.seek(0,0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='localhost', port=9874)
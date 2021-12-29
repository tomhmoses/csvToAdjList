from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    colors = ['red','green','blue','orange']
    return render_template('index.html', colors=colors)

@app.route('/api', methods=['POST'])
def api():
    color = request.form['color']
    car = request.form['car']
    return f'A {color} {car}, coming right up...'



if __name__ == '__main__':
    app.run(host='localhost', port=9874)
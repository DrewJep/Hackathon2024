from flask import *

app = Flask(__name__)

app.config.from_object('config')

@app.route('/login', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/detail', methods=['GET', 'POST'])
def detail():
<<<<<<< HEAD
    return render_template("detial.html")
=======
    pass

@app.route('/prepare', methods=['GET', 'POST'])
def prepare():
    return render_template('detail.html')
>>>>>>> b5c36a1104f63ff88dbc550819c696039f4a6802

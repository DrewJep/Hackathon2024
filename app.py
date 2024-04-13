from flask import *


app = Flask(__name__)

app.config.from_object('config')

@app.route('/login', methods=['GET', 'POST'])
def index():
    pass

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    pass

@app.route('/prepare', methods=['GET', 'POST'])
def prepare():
    return render_template('detail.html')

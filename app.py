from flask import Flask
from routes.dashboard import dashboard
app = Flask(__name__)
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIN_DATA_FILE = os.path.join(BASE_DIR, 'data', 'garbage_data_check2.csv')


app.register_blueprint(dashboard, url_prefix='/dashboard')



@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
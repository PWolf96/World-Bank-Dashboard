from worldbankapp import app
import json, plotly
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

   
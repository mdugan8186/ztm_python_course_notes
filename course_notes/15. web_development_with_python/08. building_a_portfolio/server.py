# ==== building a portfolio ====

from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about.htm')
def about():
    return render_template('about.html')


# to run the server
# flask --app server run --debug

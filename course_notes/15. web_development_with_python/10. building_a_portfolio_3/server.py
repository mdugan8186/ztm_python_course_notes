# ==== building a portfolio 3 ====

from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


# use this instead of copy and pasting code for different pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# to run the server
# flask --app server run --debug

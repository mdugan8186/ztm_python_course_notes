# ==== URL parameters ====

from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)  # __main__

# to have render_templates work properly you must create a folder and have the file you're going to run in it


# we can now dynamically add a name to the homepage and a post id
@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)

# to load the homepage now we would need to have it look like this
# http://127.0.0.1:5000/Dugan/1


@app.route("/about.html")
def about():
    return render_template('./about.html')


@app.route("/blog")
def blog():
    return "<p>These are my thoughts on blogs</p>"


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog</p>"


# using flask for a favicon


# == to run the app, run this in the command line ==
# flask --app server run

# to activate debug mode run this
# flask --app server run --debug


# == or have this withing the file ==

# if __name__ == "__main__":
#     app.run()


# file path for interpreter
# /Users/michaeldugan/coding_projects/ztm_python_course_notes/course_notes/15. web_development_with_python/04. flask_static_files/.venv/bin/python

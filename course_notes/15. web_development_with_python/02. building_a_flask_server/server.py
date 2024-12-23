# ==== building a flask server ====

from flask import Flask

app = Flask(__name__)
print(__name__)  # __main__


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# == to run the app, run this in the command line ==
# flask --app server run

# to activate debug mode run this
# flask --app server run --debug


# == or have this withing the file ==

# if __name__ == "__main__":
#     app.run()


# filepath for the interpreter
# /Users/michaeldugan/coding_projects/ztm_python_course_notes/course_notes/15. web_development_with_python/02. building_a_flask_server/.venv/bin/python

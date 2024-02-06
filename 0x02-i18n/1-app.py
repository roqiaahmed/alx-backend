from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    LANGUAGES = ["en", "fr"]


babel = Babel(app, default_locale="en", default_timezone="UTC")


@app.route("/")
def index():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)

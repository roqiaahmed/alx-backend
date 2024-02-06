#!/usr/bin/env python3
"""
2. Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class config:
    """
    config
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get_locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """index"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)

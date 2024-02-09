#!/usr/bin/env python3
"""
5. Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """
    Before request function
    """
    try:
        g.user = get_user()
        print(f"===========>{g.user}")
    except:
        None


def get_user():
    """
    Get user function
    """
    login_id = request.args.get("login_as")
    if login_id:
        return users[int(login_id)]
    return None


@babel.localeselector
def get_locale():
    """
    Get locale function
    """
    lang_code = request.args.get("locale")
    return lang_code


@app.route("/")
def index():
    """Index function"""
    return render_template(
        "5-index.html",
        home_title=_("home_title"),
        home_header=_("home_header"),
    )


if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/env python3
"""
5. Mock logging in
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

from datetime import datetime
import pytz

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
    except:
        g.user = None


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
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    elif g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]

    elif request.accept_languages.best_match(app.config["LANGUAGES"]):
        return request.accept_languages.best_match(app.config["LANGUAGES"])

    return request.default_locale


@babel.timezoneselector
def get_timezone():
    """
    Get timezone function
    """
    try:
        url_timezone = request.args.get("timezone")
        user_timezone = g.user["timezone"]
        if url_timezone:
            return pytz.timezone(url_timezone).zone
        if user_timezone:
            return pytz.timezone(user_timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


@app.route("/")
def index():
    """Index function"""
    return render_template(
        "7-index.html",
        home_title=_("home_title"),
        home_header=_("home_header"),
    )


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    if not g.get("lang_code", None):
        g.lang_code = request.accept_languages.best_match(app.config["LANGUAGES"])
    return g.lang_code


@app.route("/")
def index():
    return render_template(
        "4-index.html", home_title=_("home_title"), home_header=_("home_header")
    )


if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, render_template

def create_home_blueprint():
    home_bp = Blueprint("home", __name__)

    @home_bp.route("/")
    def homepage():
        return render_template("index.html")

    return home_bp


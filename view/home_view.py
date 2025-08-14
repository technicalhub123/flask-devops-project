from flask import Blueprint, render_template

def create_home_blueprint():
    home_bp = Blueprint("home", __name__)

    @home_bp.route("/")
    def homepage():
        return render_template("index.html")

    # Frontend page for signup form
    @home_bp.route("/signup-page")
    def signup_page():
        return render_template("signup.html")

    # Frontend page for users listing
    @home_bp.route("/users-page")
    def users_page():
        return render_template("users.html")

    return home_bp

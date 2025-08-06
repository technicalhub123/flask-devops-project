from flask import render_template
from .auth_view import create_auth_blueprint
from .home_view import create_home_blueprint  # 👈 added import

def create_endpoints(app, services):
    @app.route("/")
    def homepage():
        return render_template("index.html")  # 👈 Home page rendering

    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    # Register auth blueprint
    app.register_blueprint(create_auth_blueprint(services))

    # Register home page blueprint
    app.register_blueprint(create_home_blueprint())  # 👈 added home page


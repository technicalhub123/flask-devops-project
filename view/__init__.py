from flask import render_template
from .auth_view import create_auth_blueprint
from .home_view import create_home_blueprint

def create_endpoints(app, auth_service):  # Updated signature
    @app.route("/")
    def homepage():
        return render_template("index.html")

    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    # Register auth blueprint with direct auth_service
    app.register_blueprint(create_auth_blueprint(auth_service))

    # Register home page blueprint
    app.register_blueprint(create_home_blueprint())

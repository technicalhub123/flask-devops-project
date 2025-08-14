from flask import Blueprint, request, jsonify

def create_auth_blueprint(auth_service):  # Updated to take auth_service directly
    auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

    @auth_bp.route("/signup", methods=["POST"])
    def signup():
        new_user = request.json
        try:
            auth_service.create_new_user(new_user)
            return jsonify({"message": "User created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @auth_bp.route("/users", methods=["GET"])
    def list_users():
        """
        Returns JSON list of users for frontend consumption.
        """
        try:
            users = auth_service.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return auth_bp

import bcrypt
from sqlalchemy.exc import SQLAlchemyError

class AuthService:
    def __init__(self, auth_dao, config):
        self.auth_dao = auth_dao
        self.config = config

    def create_new_user(self, new_user):
        try:
            new_user["hashed_password"] = bcrypt.hashpw(
                new_user["password"].encode("UTF-8"), bcrypt.gensalt()
            ).decode('utf-8')  # Decode for MySQL storage
            
            # Remove password key to prevent accidental exposure
            del new_user["password"]
            
            return self.auth_dao.insert_user(new_user)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(f"Database error: {error}") from e

    def get_all_users(self):
        try:
            return self.auth_dao.get_all_users()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise Exception(f"Database error: {error}") from e

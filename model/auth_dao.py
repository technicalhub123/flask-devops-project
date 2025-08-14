from sqlalchemy import text

class AuthDao:
    def __init__(self, database):
        self.db = database

    def insert_user(self, new_user):
        return self.db.execute(
            text(
                """
                INSERT INTO users (email, username, hashed_password)  # Changed to lowercase
                VALUES (:email, :username, :hashed_password)
                """
            ),
            new_user,
        )

    def get_all_users(self):
        result = self.db.execute(text("""
            SELECT id, email, username, created_at 
            FROM users  # Changed to lowercase
            ORDER BY id DESC
        """))
        return [dict(row) for row in result.mappings().all()]

from sqlalchemy import text

def check_db_health(db):
    try:
        db.execute(text("SELECT 1"))
        return True, "Database connection healthy"
    except Exception as e:
        return False, str(e)

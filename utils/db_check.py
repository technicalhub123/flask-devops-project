from sqlalchemy import text

def verify_table_exists(db):
    try:
        result = db.execute(text("SHOW TABLES LIKE 'users'"))
        return result.rowcount > 0
    except Exception as e:
        print(f"Table verification failed: {str(e)}")
        return False

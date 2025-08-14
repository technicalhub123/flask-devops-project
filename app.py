from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import time
import logging
from model.auth_dao import AuthDao
from service.auth_service import AuthService
from view import create_endpoints
from utils.db_check import verify_table_exists  # Import verification function

class Services:
    pass

def check_db_health(db):
    """Utility function to check database health"""
    try:
        with db.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True, "Database connection healthy"
    except Exception as e:
        return False, str(e)

def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__)
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.logger.info("Starting application initialization...")

    if test_config is None:
        app.config.from_envvar("APP_CONFIG_FILE")
    else:
        app.config.update(test_config)

    # Database connection with retries
    db_connected = False
    retries = 5
    database = None
    
    while not db_connected and retries > 0:
        try:
            # Create engine with connection pooling
            database = create_engine(
                app.config["DB_URL"],
                pool_pre_ping=True,
                pool_recycle=300,
                pool_size=5,
                max_overflow=10
            )
            
            # Test connection
            with database.connect() as connection:
                connection.execute(text("SELECT 1"))
            
            db_connected = True
            app.logger.info("✅ Database connection successful")
        except Exception as e:
            app.logger.error(f"Database connection failed: {str(e)}")
            app.logger.info(f"Retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)
            retries -= 1

    if not db_connected:
        raise RuntimeError("Failed to connect to database after multiple attempts")
    
    # Verify users table exists
    if not verify_table_exists(database):
        app.logger.error("❌ Users table verification failed")
        raise RuntimeError("Users table does not exist after initialization")
    else:
        app.logger.info("✅ Users table verified")

    # Persistence Layer
    auth_dao = AuthDao(database)

    # Business Layer
    services = Services
    services.auth_service = AuthService(auth_dao, app.config)

    # Presentation Layer
    create_endpoints(app, services.auth_service)

    # Health check endpoint
    @app.route("/health")
    def health_check():
        db_healthy, db_message = check_db_health(database)
        status = 200 if db_healthy else 500
        return jsonify({
            "status": "up" if db_healthy else "down",
            "database": db_message,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }), status

    app.logger.info("Application initialized successfully")
    return app

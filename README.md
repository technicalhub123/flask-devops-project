# 🚀 **Flask Layered App with Docker** 🐳 

This project is based on the [flask-layered-template](https://github.com/sangmin7648/flask-layered-template) by sangmin7648, with significant improvements:

### Original Template Features:
- Basic 3-tier Flask architecture (Model-Service-View)
- MySQL/MariaDB integration
- Configuration management (dev/prod/test)
- Simple signup API example



<pre> ```bash . ├── app.py ├── config/ │ ├── development.py │ ├── __init__.py │ ├── production.py │ └── test.py ├── docker-compose.yml ├── Dockerfile ├── Multistage-Dockerfile ├── model/ │ ├── auth_dao.py │ └── __init__.py ├── requirements.txt ├── service/ │ ├── auth_service.py │ └── __init__.py ├── static/ │ ├── css/ │ │ └── style.css │ └── js/ │ └── script.js ├── templates/ │ └── index.html └── view/ ├── auth_view.py ├── home_view.py └── __init__.py ``` </pre>


## Architecture Overview
1. **Model Layer**: Data access objects (DAO) with singleton pattern
2. **Service Layer**: Business logic implementation
3. **View Layer**: REST API endpoints and response handling

## Docker Setup

### Prerequisites
- Docker Engine 20.10+
- Docker Compose 2.20+

### 1. Using Docker Compose (Recommended)
```bash
# Build and start all services
docker compose up -d --build

# View logs
docker compose logs -f flask-app

# Tear down
docker compose down -v


2. Manual Docker Deployment

# Create network and volume
docker network create flask-network
docker volume create flask-volume

# Start MySQL container
docker run -d --name mysql-container \
  --network flask-network \
  --volume flask-volume:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=1111 \
  -e MYSQL_DATABASE=ggulgguk \
  -p 3306:3306 \
  mysql:8.0

# Build Flask image (choose one)
# Standard build:
docker build -t flask-app .

# Multi-stage build:
docker build -t flask-app -f Multistage-Dockerfile .

# Run Flask container
docker run -d --name flask-app \
  --network flask-network \
  -p 5000:5000 \
  --env-file .env \
  flask-app


Development Setup (Non-Docker)
bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file with:
FLASK_APP=app.py
FLASK_ENV=development
APP_CONFIG_FILE=config/development.py

flask run


Accessing the Application
Flask App: http://localhost:5000

MySQL Admin: docker exec -it mysql-container mysql -u root -p

### Your Major Enhancements:
1. **Dockerization**:
   - Added 3 Docker configurations (standard, multi-stage, compose)
   - Production-ready container optimizations
   - Proper database containerization with volumes

2. **Frontend Expansion**:
├── static/
│ ├── css/style.css
│ └── js/script.js
└── templates/index.html

- Added complete frontend assets
- HTML templates with static resource support
- Ready for modern frontend frameworks

3. **Production Improvements**:
- Health checks for MySQL
- Distroless container support
- Environment variable management
- Network isolation best practices

4. **Structural Additions**:
- New home view endpoint (`home_view.py`)
- Complete development toolchain
- Detailed documentation

### Migration Guide (Original → Your Version):
To upgrade from the original template:
1. Copy your business logic to corresponding layers
2. Update database configuration in `config/development.py`
3. Place static files in `/static` and templates in `/templates`
4. Use `docker-compose.yml` for dependency management

### License Note:
This project maintains the original MIT license from the base repository while including your containerization and frontend additions.




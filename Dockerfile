# Base image with compatible Python version
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system packages required for mysqlclient and cffi
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# Copy project code
COPY . .

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Default command to run
CMD ["flask", "run", "--host=0.0.0.0"]


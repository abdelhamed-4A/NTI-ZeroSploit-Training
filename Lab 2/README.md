# Dockerized Flask-PostgreSQL Web Application

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-brightgreen.svg)](https://www.postgresql.org/)

A containerized web application demonstrating Docker and Docker Compose integration with Flask and PostgreSQL, featuring persistent database storage.

## Features

- 🐍 Python Flask web server
- 🐘 PostgreSQL database
- 🐳 Docker containerization
- 💾 Persistent data storage with Docker volumes
- 🔗 Automatic service linking via Docker Compose

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Terminal/Command Prompt

## Project Structure
```bash
├── Dockerfile # Web service configuration
├── docker-compose.yml # Orchestration setup
├── app.py # Flask application
└── README.md
```

## Getting Started

1. Clone the repository or create these files manually:
   ```bash
   git clone https://github.com/abdelhamed-4A/NTI-ZeroSploit-Training.git
   cd Lab2
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   ```bash
   http://localhost:5000
   ```
![image](./images/local-host.png)


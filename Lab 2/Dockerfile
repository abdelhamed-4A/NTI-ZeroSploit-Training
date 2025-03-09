# Use official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies and Flask
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --no-cache-dir flask psycopg2-binary

# Create and set working directory
WORKDIR /app

# Copy application code
COPY app.py .

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host", "0.0.0.0"]
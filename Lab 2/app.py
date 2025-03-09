from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # Basic database connection test
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        conn.close()
        return "Hello! Database connection successful!"
    except Exception as e:
        return f"Hello! Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run()
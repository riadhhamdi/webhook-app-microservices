from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Get the backend URL from the environment variable, with a default value
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000/webhooks")

@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL)
        webhooks = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        webhooks = []

    return render_template('index.html', webhooks=webhooks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

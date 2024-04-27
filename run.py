from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
# run.py
from flask import Flask
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == "__main__":
    app.run(debug=True)

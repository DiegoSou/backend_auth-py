from flask import Flask
from flask_cors import CORS
from .route import route_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(route_blueprint)

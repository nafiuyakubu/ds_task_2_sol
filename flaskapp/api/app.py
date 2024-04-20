from flask import Flask, request, jsonify, abort, make_response
from flask_cors import CORS
# Import all needed blueprints
from src.gender.get_gender_routes import get_gender_bp
from src.recomendations.month_recomendation_routes import month_recommendation_bp
from src.ask.ask_routes import ask_bp


app = Flask(__name__)
CORS(app)  # This will allow CORS for all routes
# Register blueprints
app.register_blueprint(get_gender_bp)
app.register_blueprint(month_recommendation_bp)
app.register_blueprint(ask_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True) 
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



# # Load our dataset
# sales_data = pd.read_csv('sales_data_sample.csv')





# CORS(app, resources={r"/recommend_fruits": {"origins": "http://localhost:8080"}})
# @app.route('/recommend_fruits', methods=['POST'])
# def recommend_fruits():
#     try:
#         answers = request.json
#         # return jsonify({'posteddata': answers})

#         # Check if the JSON data is None or does not contain required keys
#         answers_keys = ['q1', 'q2', 'q3', 'q4']
#         if answers is None or not all(key in answers for key in answers_keys):
#             return jsonify({'error': 'Invalid JSON data. Ensure all required keys[q1, q2, q3, q4] are present.'}), 400
       
#         recommended_fruits = generate_recommendations(answers)
#         return jsonify({'recommended_fruits': recommended_fruits})
#     except Exception as e:
#         # Handle other types of errors
#         return jsonify({"error": f"An error occurred: {e}"}), 500







"""
used a simple statistical analysis algorithm to generate recommendations 
based on the average sales amount for the specified month.
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4000"), debug=True) 
from flask import Blueprint, request, jsonify, abort, make_response
import gender_guesser.detector as guess_gender #[Provides functionality to infer the gender based on first names.]
import pandas as pd
import numpy as np

get_gender_bp = Blueprint('gender', __name__)


# Load our dataset
sales_data = pd.read_csv('sales_data_sample.csv')

############[Function to infer gender analysis]############
def infer_gender(person_name):
    d = guess_gender.Detector()
    gender = d.get_gender(person_name)
    return gender


@get_gender_bp.route('/get_gender', methods=['POST'])
def get_gender():
    try:
        body = request.json
        # Check if the JSON data is None or does not contain required keys
        req_keys = ['order_id']
        if body is None or not all(key in body for key in req_keys):
            error_message = f"Invalid JSON data. Ensure all required keys [{', '.join(req_keys)}] are present."
            return jsonify({'error': error_message}), 400
    
        order_id = int(body["order_id"])
        # return jsonify({"order_id": order_id})

        # Find the row corresponding to the order ID
        order_row = sales_data[sales_data['ORDERNUMBER'] == order_id]
        if order_row.empty:
            return jsonify({"error": "Order ID not found"}), 404
        
        # Extract the first name of the customer
        first_name = order_row['CONTACTFIRSTNAME'].iloc[0]
        # Infer the gender based on the first name
        gender = infer_gender(first_name)
        
        return jsonify({"gender": gender})
    except Exception as e:
        # Handle other types of errors
        return jsonify({"error": f"An error occurred: {e}"}), 500
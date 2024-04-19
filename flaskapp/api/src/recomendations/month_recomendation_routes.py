from flask import Blueprint, request, jsonify, abort, make_response
import pandas as pd
import numpy as np

month_recommendation_bp = Blueprint('recommendations', __name__)


# Load our dataset
sales_data = pd.read_csv('sales_data_sample.csv')

############[simple statistical analysis algorithm]############
def analyze_sales_data(sales_data_month):
    # sample analysis: calculate average sales amount for the month
    avg_sales_amount = sales_data_month['SALES'].mean()
    # sample analysis: check if the average sales amount is higher than usual
    if avg_sales_amount > sales_data['SALES'].mean():
        recommendation = "The average sales amount for this month is higher than usual. Consider investigating further."
    else:
        recommendation = "The average sales amount for this month is normal."
    return recommendation


@month_recommendation_bp.route('/month_recommendation', methods=['POST'])
def month_recommendation():
    try:
        body = request.json
        # Check if the JSON data is None or does not contain required keys
        req_keys = ['month']
        if body is None or not all(key in body for key in req_keys):
            error_message = f"Invalid JSON data. Ensure all required keys [{', '.join(req_keys)}] are present."
            return jsonify({'error': error_message}), 400
    
        month = body["month"]
        # return jsonify({"month": month})
        
        # Filter the sales data for the specified month
        sales_data_month = sales_data[pd.to_datetime(sales_data['ORDERDATE']).dt.month == month]
        
        # Perform analysis on sales_data_month to identify trends or anomalies
        recommendations = analyze_sales_data(sales_data_month)  # Function to analyze sales data
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        # Handle other types of errors
        return jsonify({"error": f"An error occurred: {e}"}), 500
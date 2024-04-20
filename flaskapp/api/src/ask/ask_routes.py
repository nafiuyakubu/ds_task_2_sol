from flask import Blueprint, request, jsonify, abort, make_response
import os
import pandas as pd
from langchain.llms  import OpenAI
from langchain_experimental.agents import create_csv_agent


os.environ['OPENAI_API_KEY'] = "YOUR_OPENAI_API_KEY" 
agent = create_csv_agent(OpenAI(temperature=0), 'sales_data_sample.csv', verbose=True)


ask_bp = Blueprint('ask', __name__)


def handle_question(questions):
    questions.lower() # Converting questions to lowercase
    output = agent.run(questions) # Running the agent to process the questions
    return output

@ask_bp.route('/ask', methods=['POST'])
def handle_query():
    try:
        body = request.json
        # Check if the JSON data is None or does not contain required keys
        req_keys = ['query']
        if body is None or not all(key in body for key in req_keys):
            error_message = f"Invalid JSON data. Ensure all required keys [{', '.join(req_keys)}] are present."
            return jsonify({'error': error_message}), 400
    
        query = body["query"]
        # return jsonify({"month": query})
        response = handle_question(query)
        return jsonify({"response": response})
    except Exception as e:
        # Handle other types of errors
        return jsonify({"error": f"An error occurred: {e}"}), 500




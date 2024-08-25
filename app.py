from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

# POST method endpoint to process the input
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Get the 'data' list from the JSON request
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        
        # Find the highest lowercase alphabet (if available)
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
        
        # Prepare the response structure
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)  # Return the response as JSON
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})  # Error handling

# GET method endpoint for basic check
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1})

# Route to serve the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

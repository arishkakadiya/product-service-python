from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS



import os

# Load environment variables from a .env file (only for local dev)
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

CORS(app)

# Fetch the port from the environment, or default to 3030
port = int(os.getenv('PORT', 3030))

# Define a route for the "/products" path
@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},  # Product 1
        {"id": 2, "name": "Cat Food", "price": 34.99},  # Product 2
        {"id": 3, "name": "Bird Seeds", "price": 10.99}  # Product 3
    ]
    # Return the products as a JSON response
    return jsonify(products)

# Start the server
if __name__ == '__main__':
    # Run the Flask server on the specified port
    app.run(host='0.0.0.0', port=port)

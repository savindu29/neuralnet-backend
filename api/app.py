from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# In-memory data (as an example)
data = {
    "message": "Hello, World!"
}

# Serve the HTML file as the home page from the 'static' folder
@app.route('/')
def home():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

# Handle GET request
@app.route('/hi', methods=['GET'])
def get_message():
    return jsonify(data)  # Return the current message in the data

# Handle POST request
@app.route('/hi', methods=['POST'])
def post_message():
    new_message = request.json.get('message')
    if new_message:
        data["message"] = new_message  # Update the message in the data
        return jsonify({"message": "Message updated successfully", "data": data}), 201
    else:
        return jsonify({"error": "No message provided"}), 400

# Handle PUT request
@app.route('/hi', methods=['PUT'])
def put_message():
    new_message = request.json.get('message')
    if new_message:
        data["message"] = new_message  # Replace the current message
        return jsonify({"message": "Message replaced successfully", "data": data})
    else:
        return jsonify({"error": "No message provided"}), 400

# Handle DELETE request
@app.route('/hi', methods=['DELETE'])
def delete_message():
    data["message"] = ""  # Reset the message in the data
    return jsonify({"message": "Message deleted successfully", "data": data})

if __name__ == '__main__':
    app.run(debug=True)

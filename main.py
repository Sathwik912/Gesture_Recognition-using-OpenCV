from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# Global variables
rotation_count = 0

# Serve static files from the 'static' directory
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return send_from_directory('static', 'home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Replace this with your actual gesture recognition logic
    data = request.get_json()
    gesture = data.get('gesture', 'Unknown')
    return jsonify({'predicted_character': gesture})

@app.route('/rotation-count', methods=['GET'])
def get_rotation_count():
    global rotation_count
    return jsonify({'count': rotation_count})

if __name__ == '__main__':
    # Ensure the static folder is created
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)

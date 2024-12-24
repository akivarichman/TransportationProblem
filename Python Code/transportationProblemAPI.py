from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, from Python backend!'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    print(data)
    return jsonify({'received': data})

if __name__ == '__main__':
    app.run(debug=True)
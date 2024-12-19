from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Python backend!'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({'received': data})

if __name__ == '__main__':
    app.run(debug=True)
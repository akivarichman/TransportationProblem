from flask import Flask, jsonify, request
from flask_cors import CORS
from copy import deepcopy
from NWCM import NWCM
from LCM import LCM
from VAM import VAM
from steppingStoneMethod import stepping_stone_method

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, from Python backend!'})

@app.route('/api/data', methods=['POST'])
def post_data():
    try:
        data = request.json  # Get JSON data from the request
        nested_data = data['data']
        supply = [int(s) for s in nested_data['supplies']]
        demand = [int(d) for d in nested_data['demands']]
        costs = [[int(c) for c in row] for row in nested_data['costs']]
        method = nested_data['method']
        solution = [[0 for _ in row] for row in nested_data['costs']]
        total = sum(s for s in supply)
        rows = len(supply)
        columns = len(demand)
        number_of_iterations = 0
        print(nested_data)  # Debug: Print the received data
        print(supply)
        print(demand)
        print(costs)
        print(method)
        print(solution)
        print(total)
        print(rows)
        print(columns)
        
        # Validate the data
        if not data:
            return jsonify({
                'error': 'Invalid data received.'
            }), 400  # Send a 400 Bad Request status

        # If all validations pass, process the data
        if(method == 'NWCM'):
            init_solution = NWCM(supply, demand, costs, deepcopy(solution), total)
            opt_solution = stepping_stone_method(costs, deepcopy(init_solution), rows, columns)
        elif(method == 'LCM'):
            init_solution = NWCM(supply, demand, costs, deepcopy(solution), total)
            opt_solution = stepping_stone_method(costs, deepcopy(init_solution), rows, columns)
        elif(method == 'VAM'):
            init_solution = NWCM(supply, demand, costs, deepcopy(solution), total, rows, columns)
            opt_solution = stepping_stone_method(costs, deepcopy(init_solution), rows, columns)

        return jsonify({
            'message': 'Data received successfully!',
            'received': data,
            'initial_solution': init_solution,
            'optimal_solution': opt_solution
        }), 200  # Send a 200 OK status

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            'error': 'An unexpected error occurred.',
            'details': str(e)  # Include error details for debugging (optional)
        }), 500  # Send a 500 Internal Server Error status

if __name__ == '__main__':
    app.run(debug=True)
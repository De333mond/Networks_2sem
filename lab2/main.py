from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app, origins=['*'])

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operand1 = data.get('operand1')
    operand2 = data.get('operand2')
    operation = data.get('operation')

    print(operand1, operand2, operation)

    result = None

    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            return jsonify({'error': 'Division by zero'}), 400
    elif operation == 'power':
        result = operand1 ** operand2
    elif operation == 'root':
        if operand1 >= 0 and operand2 != 0:
            result = operand1 ** (1 / operand2)
        else:
            return jsonify({'error': 'Invalid operands for root operation'}), 400
    elif operation == 'sin':
        result = math.sin(operand1)
    elif operation == 'cos':
        result = math.cos(operand1)
    elif operation == 'tan':
        result = math.tan(operand1)
    elif operation == 'cot':
        if math.tan(operand1) != 0:
            result = 1 / math.tan(operand1)
        else:
            return jsonify({'error': 'Cotangent is undefined for the given operand'}), 400
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

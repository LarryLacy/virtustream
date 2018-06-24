from flask import Flask, jsonify, request

app = Flask(__name__)

INP = []

@app.route('/fib', methods=['POST'])
def get_fib():
    if 'INP' in request.args and request.args['INP'] > '0':
        INP = request.args['INP']
        VAL = 0
        NUM = 0
        PREV1 = 0
        PREV2 = 1
        OUTPUT = []
        for x in range(int(INP)):
            NUM = (PREV1 + PREV2)
            PREV2 = PREV1
            PREV1 = NUM
            OUTPUT.append(NUM)
        return jsonify(OUTPUT)
    else:
        return request.args['INP'] + " is not a positive integer"


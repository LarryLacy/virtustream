# Import required modules
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the INP variable
INP = []

# Set the app.route and method
@app.route('/fib', methods=['POST'])

def get_fib():
# Verify INP is a positive value
# We don't actually check for alpha characters as "Fibonacci" kind of implies we'll be expecting numbers.
    if 'INP' in request.args and request.args['INP'] > '0':
# Define INP as data from request
        INP = request.args['INP']
# Set initial variable values
        VAL = 0
        NUM = 0
        PREV1 = 0
        PREV2 = 1
        OUTPUT = []
# Set the number of itterations
        for x in range(int(INP)):
# Do actual math
            NUM = (PREV1 + PREV2)
# Reset variables for next itteration
            PREV2 = PREV1
            PREV1 = NUM
# Append values for output
            OUTPUT.append(NUM)
# Return output to requestor
        return jsonify(OUTPUT)
    else:
# Notify user of poor choices on discovery of invalid input.
        return request.args['INP'] + " is not a positive integer"


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Temperature API Home"

@app.route('/api/v1/converter', methods=['POST'])
def temperature_converter():
    """
    API to convert temperature from Celcius to Farenheit, and vise versa
    Request format is JSON, and sample data format is 
        - C to F: {"type": "C", "value": 100}
        - F to C: {"type": "F", "value": 80}
    Output is converted value
    """
    # parse json data
    temperature_data = request.get_json()

    # simple validation
    if 'type' in temperature_data.keys() and 'value' in temperature_data.keys():
        # get temperature value, and convert it to float
        try:
            t_value = float(temperature_data['value'])
        except:
            t_value = None
        if t_value != None:
            if temperature_data['type'].upper() == 'C':
                # Convert from Celcius to Fahrenheit
                fahrenheit = 9.0/5.0 * t_value + 32
                return jsonify("{:.2f}".format(fahrenheit))
            elif temperature_data['type'].upper() == 'F':
                # Convert from Fahrenheit to Celcius
                celsius = (t_value - 32) * 5.0/9.0
                return jsonify("{:.2f}".format(celsius))
    return jsonify('Validation Error')

app.run()
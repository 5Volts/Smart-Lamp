from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

smart_lamp_control= {'color':{'red':255,'green':255,'blue':255},
                     'brightness':255}

@app.route('/smart_lamp')
def homepage():
    return render_template('index.html')

@app.route('/smart_lamp_color')
def colorapi():
    print(request.remote_addr)
    red = int(request.args.get('r',0))
    green = int(request.args.get('g',0))
    blue = int(request.args.get('b',0))
    smart_lamp_control['color']['red'] = red
    smart_lamp_control['color']['green'] = green
    smart_lamp_control['color']['blue'] = blue
    print(smart_lamp_control)
    return jsonify({})

@app.route('/smart_lamp_brightness')
def brightnessapi():
    val = int(request.args.get('brightness',0))
    smart_lamp_control['brightness'] = val
    print(smart_lamp_control)
    return jsonify({})

@app.route("/esp_api")
def esp_api():
    return jsonify(smart_lamp_control)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

# Imports
from flask import Flask, render_template
import random


app = Flask(__name__)

# Constants for energy calculation
HOME_COEF = 100
LIGHT_COEF = 0.04
DEVICES_COEF = 5

def result_calculate(size, lights, device):
    """Calculates the total energy consumption."""
    return size * HOME_COEF + lights * LIGHT_COEF + device * DEVICES_COEF

# Page 1: Index
@app.route('/')
def index():
    return render_template('index.html')

# Page 2: Lights
@app.route('/<int:size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Page 3: Electronics
@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights
                           )

# Page 4: Result
@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    return render_template('end.html',
                            result=result_calculate(size, lights, device)
                        )

# Page 5: Fortuna (Russian Roulette)
@app.route('/fortuna')
def fortuna():
    """Simulates one round of Russian Roulette."""
    chambers = [False] * 5 + [True]  # 5 empty, 1 loaded
    random.shuffle(chambers)
    shot = chambers[0]  # True if shot, False if lucky
    return render_template('fortuna.html', shot=shot)


# To run the app
if __name__ == '__main__':
    app.run(debug=True)

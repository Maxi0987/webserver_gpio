from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def control_led():
    led_status = "unbekannt"
    timestamp = ""
    
    if request.method == 'POST':
        led_status = request.form.get('action')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if led_status == "on":
            GPIO.output(12, GPIO.HIGH)
        elif led_status == "off":
            GPIO.output(12, GPIO.LOW)
    
    return render_template('index.html', led_status=led_status, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.teardown_appcontext
def cleanup(exception=None):
    GPIO.cleanup()

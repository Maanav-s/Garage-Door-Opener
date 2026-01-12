#Currently no functionality for door
#command prompt test

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from time import sleep

from flask.helpers import url_for
from gpiozero import DigitalOutputDevice

app = Flask(__name__)
pin = DigitalOutputDevice(9)
status = "Fail"

@app.route('/', methods = ['POST', 'GET'])
def home():
    print("home called")
    global l
    global status

    if request.method == 'POST':
        print(request.form['code'])
        if request.form['code'] == "TOGGLE":
            try:
                
                #pin.blink(on_time = 0.5, n=1)

                status = "success"
                print(status)
            except Exception:
                print(Exception.__name__)
        else:
            status = "denied"
        return redirect(f'/message/{status}')
            
    return render_template('/page.html')

@app.route('/message/<status>', methods = ['GET'])
def message(status):
    return render_template('/message.html', status=status)
    

if __name__=='__main__':
   app.run(host='0.0.0.0', port=5000, debug = True)

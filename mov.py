from flask import Flask, render_template
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
app = Flask(__name__,static_url_path="/home/pi/Desktop/project_1/pictures", static_folder="/home/pi/Desktop/project_1/pictures")
line_counter=0
last_photo=""
@app.route("/")
def index():
    return "Hello"

@app.route("/check-movement")
def checkmovement():
    if os.path.exists("/home/pi/Desktop/project_1/photo_logs.txt "):
        with open("/home/pi/Desktop/project_1/photo_logs.txt ","r") as log:
            for line in log:
                print(line)
                line_counter+=1
                last_photo= line
    else:
        print("NO LOG")



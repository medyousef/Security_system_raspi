import time
import RPi.GPIO as GPIO
from picamera import PiCamera
import os
import sys
import logging
import yagmail
PIR_PIN= 15
LED_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(LED_PIN, GPIO.LOW)
PIR_time_counter =0

if not os.path.exists("/home/pi/Desktop/project_1/pictures"):
    os.mkdir("/home/pi/Desktop/project_1/pictures")
logging.basicConfig(filename="photo_logs.txt", level=logging.INFO)

password = "yousseftest"
with open("/home/pi/Desktop/Security_system_raspi/.email_password", "r") as pswd:
    password=pswd.read()

yag= yagmail.SMTP("youssefraspitest@gmail.com", password)

def send_email_with_photo(attachment):
    yag.send(to='medyousef95@gmail.com',
        subject="Warning",
        contents="movement detected",
        attachments=attachment)
    print("email sent")

last_time_photo_taken=""

camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
def take_photo():
    file_name="/home/pi/Desktop/project_1/pictures/"+"image_"+str(time.time())+".jpg"
    print(file_name +" to be taken")
    camera.capture(file_name)
    print(file_name +" taken")
    send_email_with_photo(file_name)
    logging.info(file_name)
    last_time_photo_taken=file_name

try :
    while True :
        time.sleep(0.5)
        print(GPIO.input(PIR_PIN))
        if GPIO.input(PIR_PIN)==GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
            PIR_time_counter +=1
        elif GPIO.input(PIR_PIN)==GPIO.LOW:
            PIR_time_counter =0
        if PIR_time_counter==3:
            take_photo()
            PIR_time_counter=0
            time.sleep(5)
        

except KeyboardInterrupt:
    GPIO.cleanup

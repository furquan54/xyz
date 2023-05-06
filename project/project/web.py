


from flask import Flask, render_template, request, redirect, url_for, make_response, Response
import motors
import RPi.GPIO as GPIO
import requests
import threading
import cam
import servo
import time
#import cv2
import numpy as np
import math
import commands
import socket

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():
    
   
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    print s.getsockname()[0]
    
    ipap = ip+":5000"
    print ipap
    
    templatedata = {            
        'ip' : ipap
        }
    #return render_template('index.html', content = content)
    return render_template('web.html', **templatedata)

#recieve which pin to change from the button press on web.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
		
	else:
		motors.stop()


	response = make_response(redirect(url_for('index')))
	return(response)


app.run(debug=True, host='0.0.0.0', port=5000) #set up the server in debug mode to the port 5000

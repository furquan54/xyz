#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# motors.py
#######

import RPI.GPIO as GPIO
import time
from time import sleep
import re

from subprocess import call

Motor1A = 05 
Motor1B = 06 

Motor2A = 13 
Motor2B = 19

srelay = 23
urelay = 24

#Function splits a big paragraph into smaller sentences for easy TTS
def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


def sound(spk):
        cmd_beg=" espeak -ven+f4 -s120 -k20 --stdout '"
        cmd_end="' | aplay"
       
        call ([cmd_beg+spk+cmd_end], shell=True)

sentences = splitParagraphIntoSentences("Spy robot by web application")


for s in sentences:
	sound(s.strip())
 

#Set up all as outputs
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

GPIO.setup(srelay,GPIO.OUT)
GPIO.setup(urelay,GPIO.OUT)

def forward():
        
        print("Going Forwards")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
	

def backward():
	print("Going Backwards")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.05)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.05)
	

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

	sleep(0.05)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	


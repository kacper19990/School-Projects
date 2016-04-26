<<<<<<< HEAD
import RPi.GPIO as GPIO
import time

def RL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(58,GPIO.OUT)
	GPIO.output(58,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(58,GPIO.LOW)

def RL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(57,GPIO.OUT)
	GPIO.output(57,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(57,GPIO.LOW)

def OL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(22,GPIO.LOW)

def OL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(23,GPIO.LOW)
	
def GL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(6,GPIO.OUT)
	GPIO.output(6,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(6,GPIO.LOW)
	
def GL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(52,GPIO.OUT)
	GPIO.output(52,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(52,GPIO.LOW)

def start():
	GL1
	RL2
	time.sleep(5)
	OL1
	OL2
	time.sleep(5)
	GL2
	RL1
	time.sleep(5)

while True:
	start
	continue


=======
import RPi.GPIO as GPIO
import time

def RL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(18,GPIO.LOW)

def RL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(17,GPIO.OUT)
	GPIO.output(17,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(17,GPIO.LOW)

def OL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(22,GPIO.LOW)

def OL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(23,GPIO.LOW)
	
def GL1():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(6,GPIO.OUT)
	GPIO.output(6,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(6,GPIO.LOW)
	
def GL2():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(12,GPIO.OUT)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(12,GPIO.LOW)

def start():
	GL1
	RL2
	time.sleep(5)
	OL1
	OL2
	time.sleep(5)
	GL2
	RL1
	time.sleep(5)

while True:
	start
	continue


>>>>>>> origin/master

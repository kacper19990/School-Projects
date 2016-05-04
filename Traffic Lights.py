from multiprocessing import Process 			#Load a library called "multiprocessing" and import the commands from "Process"
import sys						#Import the "sys" commands
import RPi.GPIO as GPIO					#Import the "RPi.GPIO" commands that allow us to utilise the pins on the RaspberryPi
import time						#Import the ability to use .time commands
def Left():						#Create a definition that makes it easy to load up all the commands using one word rather than rewrite the code
	GPIO.setmode(GPIO.BCM)				#Referring to the pins on the Pi
	GPIO.setwarnings(False)				#Turn off the warnings
	GPIO.setup(23,GPIO.OUT)				#Set the 23rd pin as an output (Green)
	GPIO.output(23,GPIO.High)			#Turns on the LED that is connected to the pin
	time.sleep(5)					#LED turns on for 5 seconds
	GPIO.output(23,GPIO.Low)			#Turns off the LED
	GPIO.setup(18,GPIO.OUT)				#Set the 18th pin as an output (Orange)
	GPIO.output(18,GPIO.High)			#Turns on the LED that is connected to the pin
	time.sleep(2)					#LED turns on for 2 seconds
	GPIO.output(18,GPIO.Low)			#Turns off the LED
	GPIO.setup(25,GPIO.OUT)				#Set the 25th pin as an output (Red)
	GPIO.setup(25,GPIO.High				#Turns on the LED that is connected to the pin
	time.sleep(7)					#LED turns on for 5 seconds
	GPIO.setup(25,GPIO.Low)				#Turns off the LED
	pass
def Right():						#Create a definition that makes it easy to load up all the commands using one word rather than rewrite the code
	GPIO.setmode(GPIO.BCM)				#Referring to the pins on the Pi
	GPIO.setwarnings(False)				#Turn off the warnings
	GPIO.setup(12,GPIO.OUT)				#Set the 12th pin as an output (Red)
	GPIO.output(12,GPIO.High)			#Turns on the LED that is connected to the pin
	time.sleep(7)					#LED turns on for 7 seconds
	GPIO.output(12,GPIO.Low)			#Turns off the LED
	GPIO.setup(17,GPIO.OUT)				#Set the 17th pin as an output (Green)
	GPIO.output(17,GPIO.High)			#Turns on the LED that is connected to the pin
	time.sleep(5)					#LED turns on for 5 seconds
	GPIO.output(17,GPIO.Low)			#Turns off the LED
	GPIO.setup(22,GPIO.OUT)				#Set the 22nd pin as an output (Orange)
	GPIO.setup(22,GPIO.High)				#Turns on the LED that is connected to the pin
	time.sleep(2)					#LED turns on for 2 seconds
	GPIO.setup(22,GPIO.Low)				#Turns off the LED
	pass
if __name__ == '__main__':				#Allows us to run two or more commands at the same time
	while True:					#The code is executed while the statement is True
		Process(target=Left).start()		#Loads the "Left" process that we made before and starts it
		Process(target=Right).start()		#Loads the "Right" process that we made before and starts it
		time.sleep(14)				#Waits 14 seconds before proceeding to the next command
		continue				#Goes back to the start of the 'While True' command

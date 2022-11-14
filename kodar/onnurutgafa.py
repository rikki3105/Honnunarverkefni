#!/usr/bin/python -u
import digitalio
import board
import time
from board import *
import glob
import adafruit_dht
import RPi.GPIO as GPIO
import os
import datetime

## A - LIÐUR
## Kveikjum á viftu

# Configuration
FAN_GPIO_PIN = 20
RELAY_FAN_GPIO_PIN = 26 # BCM pin used to turn RELAY for FAN ON/OFF
##PWM_duty_cycle = 10

def dutycyclevifta():

	def setFanSpeed(PWM_duty_cycle):
		fan.start(PWM_duty_cycle)
		return()

	try:
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
  	# Setting up relay for FAN
		GPIO.setup(RELAY_FAN_GPIO_PIN, GPIO.OUT, initial=GPIO.HIGH) # HIGH MEANS RELAY IS OFF

		GPIO.output(RELAY_FAN_GPIO_PIN,GPIO.LOW) # Turn the FAN ON
		print("FAN IS ON")
		time.sleep(5)
	except KeyboardInterrupt:
			GPIO.cleanup() # resets all GPIO ports used by this function


PWM_OFF = 0             # the PWM_duty_cycle 0%
PWM_MAX = 100           # the PWM_duty_cycle 100%



base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/temperature'
#### Setjum Duty Cycle ####

dutycyclegildi = [10,90]


for i in dutycyclegildi:
	setFanSpeed(i)
	time.sleep(30)
	print("Duty cycle: " + i + " 10%")
###### Hitanemi ######
	def read_temp_raw():
		temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		while (teljari < 11):
			print(temp_c)
			if i == 0:
				gildi10 = []
				gildi10.append(temp_c)
			else:
				gildi90 = []
				gildi90.append(temp_c)
			time.sleep(10)
			teljari = teljari + 1

	## finna meðaltal af mælingunum tíu
medaltal10 = sum(gildi10)/10
medaltal90 = sum(gildi90)/10


#### B - LIÐUR #######
oskgildi = (medaltal10 + medaltal90)/2
print("Hitastig mitt á milli gilda: " + oskgildi)

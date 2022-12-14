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
RELAY_HEATER_FAN_GPIO_PIN = 16
##PWM_duty_cycle = 10
PWM_FREQ = 125        # [Hz] 25kHz for PWM control


PWM_OFF = 0             # the PWM_duty_cycle 0%
PWM_MAX = 100           # the PWM_duty_cycle 100%
dutycyclegildi = [10, 90]

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/temperature'

################################################
try:
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

# PWM used to control the fan's speed
	GPIO.setup(RELAY_FAN_GPIO_PIN, GPIO.OUT, initial=GPIO.HIGH)
# tachometer - from a hall sensor located in the fan
	GPIO.setup(RELAY_HEATER_FAN_GPIO_PIN, GPIO.OUT, initial=GPIO.HIGH)

	GPIO.output(RELAY_FAN_GPIO_PIN,GPIO.LOW) # Turn the FAN ON
	print("FAN IS ON")
	time.sleep(5)

	GPIO.output(RELAY_HEATER_FAN_GPIO_PIN, GPIO.LOW)
	print("HEATER ON")
except KeyboardInterrupt:
		GPIO.cleanup() # resets all GPIO ports used by this function


# Set fan speed
def setFanSpeed(PWM_duty_cycle):
	fan.start(PWM_duty_cycle)
	return()

def read_temp_raw():
	f = open(device_file, 'r')
	line = f.read()
	f.close()
	return line

##################################
try:
	GPIO.setwarnings(False)
	GPIO.setup(FAN_GPIO_PIN,GPIO.OUT, initial = GPIO.LOW)
	fan = GPIO.PWM(FAN_GPIO_PIN, PWM_FREQ)
	setFanSpeed(PWM_OFF)

#### Setjum Duty Cycle ####
	gildi10 = []
	teljari = 0
	duty_cycle = 10
	print("Duty cycle: " + str(duty_cycle) + "%")

	while (teljari < 10):
		setFanSpeed(duty_cycle)
		temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		print(temp_c)
		gildi10.append(temp_c)
		time.sleep(2)
		teljari = teljari + 1

		medaltal10 = sum(gildi10)/10
		print("Meðaltal 10: " + str(medaltal10))


#Hitastig m.v. 90% duty gildi

	gildi90 = []
	teljari1 = 0
	duty_cycle = 90
	print("Duty cycle: " + str(duty_cycle) + "%")

	while (teljari1 < 10):
		setFanSpeed(duty_cycle)
		temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		print(temp_c)
		gildi90.append(temp_c)
		time.sleep(2)
		teljari1 = teljari1 + 1

	medaltal90 = sum(gildi90)/10
	print("Meðaltal 90: " + str(medaltal90))

	raunhitastig = (medaltal10 + medaltal90)/2
	print("Miðgildið er " + str(raunhitastig))

	currenttimi = time.time()

	while (timi <= 30)
		timi = time.time() - currenttimi
		k = 3
		e = oskgildi - temp_c
		setFanSpeed(k * e)
		print(e)

		GPIO.cleanup()
		print("FAN IS OFF")

except KeyboardInterrupt:
	setFanSpeed(FAN_OFF)

	## finna meðaltal af mælingunum tíu

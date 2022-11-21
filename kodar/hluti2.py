#!/usr/bin/python -u
# coding=utf-8
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
PWM_FREQ = 1250        # [Hz] 25kHz for PWM control


PWM_OFF = 0             # the PWM_duty_cycle 0%
PWM_MAX = 100           # the PWM_duty_cycle 100%
gildi10 = 27.553
gildi90 = 24.375
oskgildi = 25.964

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
	time.sleep(3)

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


	setFanSpeed(40)
	time.sleep(2)


	temp_string = read_temp_raw()
	temp_c = float(temp_string) / 1000.0
	print("Hiti fyrir " + str(temp_c))

	bil = (oskgildi - gildi90)/30 ##0,052967
	u_0 = 40
	currenttimi = time.time()
	timi = 0
	while (timi <= 30):
		timi = time.time() - currenttimi
		print("timi = " + str(timi))
		e = oskgildi - temp_c
		oskgildi = oskgildi - bil
		if (e < 0):
			k = 6
		elif (e > 0):
			k = 12
		fanspeed = u_0 - k*e
		if (fanspeed < 0):
			fanspeed = 0
		elif (fanspeed > 100):
			fanspeed = 100

		temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		print(temp_c)

	oskgildi1 = oskgildi
	print("Lokaóskgildi: " + str(oskgildi1))

##Reglum við óbreytt óskgildi í 30 sek

	u_0 = 40
	currenttimi = time.time()
	timi = 0
	while (timi <= 30):
		timi = time.time() - currenttimi
		print("timi = " + str(timi))
		e = oskgildi - temp_c
		if (e < 0):
			k = 6
		elif (e > 0):
			k = 12
		fanspeed = u_0 - k*e
		if (fanspeed < 0):
			fanspeed = 0
		elif (fanspeed > 100):
			fanspeed = 100
		setFanSpeed(fanspeed)
		temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		print(temp_c)

	GPIO.cleanup()
	print("FAN IS OFF")

except KeyboardInterrupt:
	setFanSpeed(FAN_OFF)

	## finna meðaltal af mælingunum tíu

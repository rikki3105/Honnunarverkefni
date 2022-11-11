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
RELAY_FAN_GPIO_PIN = 26 # BCM pin used to turn RELAY for FAN ON/OFF


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


#Breytur
maelingar = []         	# Notað til að safna gildum
fjoldiMaelinga = 2	# hvað ætlum við að safna mörgum gildum

PWM_OFF = 0             # the PWM_duty_cycle 0%
PWM_MAX = 100           # the PWM_duty_cycle 100%

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/temperature'
#### Setjum Duty Cycle ####

dutycyclegildi = [10,90]

for i in listi:
		setFanSpeed(i)
		time.sleep(30)
	print("Duty cycle: " + i + "%")

###### Hitanemi ######

	def read_temp_raw():
    	f = open(device_file, 'r')
    	line = f.read()
    	f.close()
    	return line

	while (teljari < 11):
    	temp_string = read_temp_raw()
		temp_c = float(temp_string) / 1000.0
		print(temp_c)
		gildi = []
		gildi.append(temp_c)
    	time.sleep(10)
    	teljari = teljari + 1

	## finna meðaltal af mælingunum tíu
	gildi = sum(hitastig)/10

	## setja meðaltalið í lista með append


#### B - LIÐUR #######
oskgildi = sum(maelingar)/2
	     print("Hitastig mitt á milli gilda: " + oskgildi)

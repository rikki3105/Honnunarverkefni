import digitalio
import board
import time
from board import *
import glob
import adafruit_dht
import RPi.GPIO as GPIO
import os
import datetime

##### A - LIÐUR#####
###### Kveikjum á viftu ######

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

#### Setjum Duty Cycle1 ####

	duty_cycle1 = 10
		setFanSpeed(duty_cycle1)
		time.sleep(8)
	print("Duty cycle: 10%)
	picking = [hitastig]
	maelingar.append(picking)

###### Hitanemi ######

dhtDevice = adafruit_dht.DHT22(board.D5)

teljari = 1

while (teljari < 11):
    try:
        hitastig = dhtDevice.temperature
        print("Hitastig: {:.1f} C  mæling nr. {}".format(hitastig, teljari))

    except RuntimeError as error:
        # Villur koma reglulega upp - getur verið erfitt að lesa gildi nemans, bara reyna aftur
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
    teljari = teljari + 1


    #### Setjum Duty Cycle2 ####

	duty_cycle2 = 90
		setFanSpeed(duty_cycle2)
		time.sleep(8)
	print("Duty cycle: 90%")
	picking = [hitastig]
	maelingar.append(picking)

###### Hitanemi ######

dhtDevice = adafruit_dht.DHT22(board.D5)

teljari = 1

while (teljari < 11):
    try:
        hitastig = dhtDevice.temperature
        print("Hitastig: {:.1f} C  mæling nr. {}".format(hitastig, teljari))

    except RuntimeError as error:
        # Villur koma reglulega upp - getur verið erfitt að lesa gildi nemans, bara reyna aftur
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
    teljari = teljari + 1
	      
	      
#### B - LIÐUR #######
oskgildi = sum(maelingar)/2
	     print("Hitastig mitt á milli gilda: " + oskgildi)

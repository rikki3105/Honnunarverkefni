#!/usr/bin/python -u

#!/usr/bin/python -u
import RPi.GPIO as GPIO
import time
import datetime
import board
import adafruit_dht
import os

RELAY_FAN_GPIO_PIN = 26
FAN_GPIO_PIN = 20
IR_GPIO_PIN = 6
PWM_FREQ = 125
PWM_OFF = 0
PWM_MAX = 100
TACH_GPIO_PIN = 21
count_time = 2

def setFanSpeed(PWM_duty_cycle):
  fan.start(PWM_duty_cycle)
  return()

def tach_count(sec,GPIO_PIN):
  duration = datetime.timedelta(seconds=sec)
  end_time = (datetime.datetime.now()+duration)
  current_pin_status = GPIO.input(GPIO_PIN)
  last_pin_status = 2
  counter = 0
  while ( datetime.datetime.now() < end_time):
    current_pin_status=GPIO.input(GPIO_PIN)
    if (current_pin_status != last_pin_status):
     # print(current_pin_status)
      last_pin_status = current_pin_status
      counter += 1
  return (counter)

try:
  print("PWM_FREQ = ",PWM_FREQ)
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(RELAY_FAN_GPIO_PIN, GPIO.OUT, initial=GPIO.HIGH)
  GPIO.setup(FAN_GPIO_PIN, GPIO.OUT, initial=GPIO.HIGH) # var low
  GPIO.setup(TACH_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(IR_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  fan = GPIO.PWM(FAN_GPIO_PIN,PWM_FREQ)
  setFanSpeed(PWM_OFF)


  GPIO.output(RELAY_FAN_GPIO_PIN,GPIO.LOW)
  counter2= 0
  while (counter2 < 5):
    duty_cycle = PWM_MAX*counter2/4
    setFanSpeed(duty_cycle)
    time.sleep(4)
    print("Duty cycle:: {:.2f}".format(duty_cycle))
    tach_hall_rpm = float(tach_count(count_time,TACH_GPIO_PIN))/count_time/2/2*60
    print("Hall RPM:: {:.2f}".format(tach_hall_rpm))
    tach_IR_rpm = float(tach_count(count_time, IR_GPIO_PIN))/count_time/2/9*60
    print("IR RPM:: {:.2f}".format(tach_IR_rpm))
    print("hlutfall : ", (tach_hall_rpm/tach_IR_rpm)*100)
    counter2 += 1
  GPIO.output(RELAY_FAN_GPIO_PIN,GPIO.HIGH)


  GPIO.cleanup()

except KeyboardInterrupt:
  setFanSpeed(FAN_OFF)
  GPIO.cleanup()
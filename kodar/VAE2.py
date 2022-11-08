import time
import board
import adafruit_dht
import glob
import digitalio
from board import *

#Athuga birtustig og kveikja á lampa ef það er of dimmt.

LDR_GPIO_PIN = board.D6

LDR = digitalio.DigitalInOut(LDR_GPIO_PIN)
LDR.direction = digitalio.Direction.INPUT
SSR = digitalio.DigitalInOut(D23)
SSR.direction = digitalio.Direction.OUTPUT

if LDR.value == True:
    print("Birtustigið er of lágt, kveikjum á lampanum")
    SSR.value = True
    time.sleep(2)
else:
    print("Birtustigið er hátt, kveikt er á lampanum")
    time.sleep(2)
    SSR.value = True

#Athuga hvort kveikt sé á lampa með því að mæla birtu
print("Er kveikt á lampa? Athugum birtustig")
time.sleep(1)

if LDR.value == True:
    print ("Slökkt á lampa")
else:
    print ("Kveikt á lampa")
time.sleep(1)

# Mæla hitastigið reglulega á meðan kveikt er á lampanum.
# Slökkva á lampanum ef hitastig hefur breyst um 0.3°
print("Mælum hitastig reglulega. Slökkvum þegar hitastig hefur breyst um 0.3°C")
time.sleep(1)
dhtDevice = adafruit_dht.DHT22(board.D5)
teljari = 1
upphafshitastig = dhtDevice.temperature
deltaT = 0
teljari = 0

while (teljari < 20):
    try:
        hitastig = dhtDevice.temperature
        rakastig = dhtDevice.humidity
        deltaT = hitastig - upphafshitastig
        print("Hitastig: {:.1f} C".format(
        hitastig , rakastig, deltaT, teljari))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)
    if (deltaT >= 0.3):
        break
    else: teljari = teljari+1

if(deltaT >= 0.3):
    SSR.value = False
    print("Hitastig hefur breyst um 0.3°C, slökkvum á lampa")
    time.sleep(2.0)

# Staðfesta að slökkt sé á lampanum
if SSR.value == False:
  print ("Slökkt er á lampa")
else:
  print ("Kveikt er á lampa")
  sleep.time(1)
  print ("Slökkvum á lampanum")
  SSR.value = False

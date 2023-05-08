from internet_connect import Wlan
from thermometer import Thermometer
from machine import Pin
import time
import network
import urequests
import dht
import machine

def main():
    Wlan().try_to_connect() # launch the connexion
    compt = 1
    print('connexion on')
    while compt == 1:
            led = Pin(14, Pin.OUT)
            led.off()
            time.sleep(.5)
            led.on()
            Thermometer().take_temp()
            time.sleep(300)


if __name__ == "__main__":
    main()


import network
import time
import urequests


class Wlan:

    def try_to_connect(self):
        timeout = 0
        wifi = network.WLAN(network.STA_IF)
        wifi.active(False)
        time.sleep(0.5)
        wifi.active(True)
        wifi.connect('wifi name', 'password')
        if not wifi.isconnected():
            print('connection...')
            while (not wifi.isconnected() and timeout <5):
                print(5 - timeout)
                timeout = timeout + 1
                time.sleep(1)
        if(wifi.isconnected()):
            print('connected')
        else:
            print('time out')

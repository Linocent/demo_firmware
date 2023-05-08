import dht
import machine
import urequests
import ujson


class Thermometer:

    def take_temp(self):
        uart1 = machine.UART(1, baudrate=115200)
        d = dht.DHT11(machine.Pin(4))
        d.measure()
        url = "Your_url"
        data = 'temperature: {}, humidity: {}'.format(d.temperature(), d.humidity())
        data_to_send = ujson.dumps({'content': data})
        res = urequests.post(url, headers={'content-type': 'application/json'}, data=data_to_send)
        res.close()  #Connexion close for memory

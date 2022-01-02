import network
import time
import machine

def connect_wifi():
    global wifi
    wifi = network.WLAN(mode=network.WLAN.STA)
    reconnect_count = 0
    print("Connecting to wifi")
    wifi.connect('SSID', auth=(network.WLAN.WPA2, 'PASSWORD'))
    while not wifi.isconnected():
        print(".",end="")
        time.sleep(1)
        reconnect_count += 1
        if reconnect_count == 15:
            print("rebooting")
            machine.reset()
    print("connection established!")

connect_wifi()

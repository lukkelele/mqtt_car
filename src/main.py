import network
import time
from machine import PWM
from machine import Pin
from mqtt import MQTTClient

# Define pins on the LoPy4

powerpin = Pin("P8", mode=Pin.OUT)
servo = machine.PWM(0, frequency=50)
servo_c = servo.channel(0, pin='P12', duty_cycle=0.09)              # duty_cycle operates within 0.02-0.12
mqtt_check = False
CLIENT_NAME = " "                                                   #  User info required to be able to use Adafruit IO
USER_NAME = " "                    
IO_KEY = " "                        
PING_INTERVAL_MS =                                                  # Enter in milliseconds 

# Steering and motor controls           
# If car is understeering/oversteering, increase/decrease the duty_cycle.
# We used these three --> Left, 0.070 -- Default/forward, 0.090 -- Right, 0.105

def turn_left():
    servo_c.duty_cycle(0.070)

def turn_left_forward():
    servo_c.duty_cycle(0.070)
    powerpin.value(1)

def turn_right_forward():
    servo_c.duty_cycle(0.105)
    powerpin.value(1)

def turn_right():
    servo_c.duty_cycle(0.105)

def default_position():
    servo_c.duty_cycle(0.09)

def reset_car():
    default_position()
    powerpin.value(0)

def sub_cb(topic, msg):
    global last_ping
    print(msg)
    if msg == b'{"feeds":{"myfeed":"1"}}':                  # Forward
        powerpin.value(1)
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"left-turn":"0"}}':             # Release motor
        powerpin.value(0)
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"left-turn":"2"}}':             # Left turn, amount of steering depending on duty cycle.
        turn_left()
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"right-turn":"4"}}':            # Right
        turn_right()
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"right-turn":"5"}}' or b'{"feeds":{"left-turn":"7"}}' or b'{"feeds":{"right-turn":"9"}}' or b'{"feeds":{"left-turn":"3"}}':
        reset_car()
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"left-turn":"6"}}':
        turn_left_forward()
        last_ping = utime.ticks_ms()
    elif msg == b'{"feeds":{"right-turn":"8"}}':
        turn_right_forward()
        last_ping = utime.ticks_ms()

client = MQTTClient("RC-car", "io.adafruit.com",user="USER_NAME", password="PASSWORD", port=1883)
client.set_callback(sub_cb)

while True:
    if not wifi.isconnected():
        connect_wifi()
    elif wifi.isconnected():
        try:
            if mqtt_check == False:
                print("Connecting to mqtt")
                client.connect()
                time.sleep(1)
                client.subscribe(topic="FEEDS/CONNECTION")
                client.publish("FEEDS/CONNECTION", "ping", retain=True)
                time.sleep(2)
                mqtt_check = True
                last_ping = utime.ticks_ms()                                        # Timed last recieved message from Adafruit.IO
                print("MQTT connected!")
                while mqtt_check == True:
                    if utime.ticks_ms()-last_ping < PING_INTERVAL:
                        client.check_msg()
                    else:
                        try:                                                                        
                            client.publish("FEEDS/CONNECTION", "ping", qos=2)          # If publish fails, exception  runs
                            last_ping = utime.ticks_ms()                                           # Resetting ping timer
                        except Exception:
                            print("Connection lost to Adafruit. Trying to reconnect")
                            mqtt_check = False                                  # Reloop
        except Exception:
            print("unable to connect to mqtt server" + "\nMaking sure wifi is connected..",end="")
            if wifi.isconnected():                          # updating to check connection, rebooting if wifi is signal is lost
                print("... wifi is connected")
                time.sleep(1)
                print("rebooting in 5 seconds..",end=" ")
                for number in range(5):
                    print(5-number,end=" ")
                    time.sleep(1)
                machine.reset()
            else:
                print("wifi disconnected. Trying to reconnect")     

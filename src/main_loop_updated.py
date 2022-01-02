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

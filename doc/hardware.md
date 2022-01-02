### Hardware

**Pycom LoPy4** - Development board with access to WiFi, bluetooth, LoRa and Sigfox.

**Pycom Expansion board 3.0** - Expansion board used with the LoPy4. Pins with PWM makes it possible to use a servo for steering.

**Parallax Standard Servo 4-6 V** - Basic motor servo with 180 degree turn radius.

**DC motor 6-12V** - Basic DC motor, direction of current determines which way it spins. ![Picture of DC motor](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/electrical%20parts/20210121_002307.jpg)

**5 V relay** - The 3V pin on the Lopy4 cant sustain a motor on its own. The relay used is a 5V arduino relay, the GPIO pins on the expansion board output high enough current to activate the relay. ![Picture of relay](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/electrical%20parts/20210121_001918.jpg)

**Batteries 6V, 9V, 5V** - The batteries need to be within the requirements of the components and can be replaced to higher voltage batteries if the voltage is stepped down before entering the devices/devices.

**Breadboard** - Easy to manage and no soldering needed.

### Assembly
It's not required to use 3d printed parts. As long as the electronic devices can communicate with the MQTT server the variations of building the RC car is infinite. Given that the 3d printed parts are used, the assembly shall be done like this:
1. Put glue on both of the base pieces and press them together. Make sure they fit the jigsaw pattern with hotglue in between and make sure they are firmly pressed together. Because of warping that occured on both pieces when they were being printed, I used sandpaper before gluing and then applied tape to make sure the base was solid.
2. Mount breadboard on one of the sides were it is accessible and not in the way for the servo or motor.
3. Put together rear axle with all accessories and place the mount for the motor where it can sit and connect to the big gear.
4. Add the relay to the breadboard and wire an external battery in circuit with the motor and the relay. The wiring with the relay must be NO which stands for Normally Open. The circuit with the external battery powering the motor is closed when the relay is activated and activates the motor. ![Relay wiring](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring_relay_dc_motor.png)
5. Put together the steering mechanism at the front axle and mount the servo and wire another external battery to power it as well. ![Wiring of servo by itself](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring/20210121_001041.jpg)
6. Add the Lopy4 to the base with the last battery. The lopy4 needs between 3.4-5.4 V to function properly. Wire the battery and make sure the polarity of the battery is facing the right way. Plus terminal goes to Vin and the negative terminal goes to ground which is wired to the breadboard.
7. Make sure to wire such that all equipment is within operating range and wired properly on the breadboard and continue with the remaining parts. 

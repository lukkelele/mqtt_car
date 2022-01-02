## Important information
The car relies on the servo and motor to function. Both rely on voltages over 3 V which makes additional power sources a must. 
It is very important to have a structure when wiring because the Lopy functions within 3.4-5.5 V and by connecting a battery wrongly to it can cause it to malfunction and stop working. As always it's also necessary to make sure that no short circuits take place to prevent damaged equipment and fires.  \
Relevant pictures, also featured in file: ![Whole circuit](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring/WIRING.png)   |   [Servo wiring to Lopy](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring/servos_wiring.jpg)  |  ![Breadboard relay wire to DC motor](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring/wire_dc_motor_first.png)
## Testing 
Try out all the components one by one before making bigger circuits. I did the testing in this [manner](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/img/wiring/WIRING.png).
1. Wiring the relay to the breadboard with the external circuit to the motor (powered by an external power source). Have the lopy connected with correct wiring from the 3V, ground and a pin used to signal the relay. Set the value of the pin connected to signal the relay to 1. If the motor is being activated the relay is fully functional. Set the value of signal pin to 0 and disconnect the the external battery and dc motor from the relay.
2. The servo is tested in the same manner. Not all servo frequencies are universal so make sure to check the specifications of the servo you are using. Connect the 3V and ground in the same manner as with the relay and a pin with PWM to the signal wire of the servo. Both servos that were used on the car had 50Hz was convinient since I had no experience with servos or pulse width modululation in general. The duty cycles used were between 0.02-0.12. I placed the servo in the desired position in the middle of the steering mechanism and tested different duty cycles to get a feeling of how it behaved when different values were used. When done calibrating the servo disconnect all wires the servo.
3. This step is very important. When powering the Lopy (or any electronic device in general) with a power source that's not manufactured by the device's company, all electrical criterias regarding the output/input must be met. Test the battery with a multimeter and make sure the voltage output is within the range of the device's accepted voltages. Pay attention to wire the positive terminal of the battery to the Vin pin. If the voltage is above the maximum of the device's range a voltage regulator can be used to step the voltage down. When I first had this issue when I was to test the lopy I had no access to a voltage regulator. Instead I used a voltage divider circuit which worked fine until I switched the battery to a more convinient one that operated within the recommended ranges.
4. With all components working as intended with some testing, the next step is to make a circuit with the lopy where the motor and servo are connected and can be activated. The placement of ground and the 3V output of the lopy play a big role in being able to make sense out of all the wires and decrease the risk of damaging any of the equipment. Wire as in the first 3 steps. Make sure to have one common ground where all grounded/negative wires go. When a whole circuit is formed, test all devices given that the lopy already is powered externally. 
<img src="img/wiring/WIRING.png" alt="img/wiring/WIRING.png" width="768"/>
<img src="img/wiring/wiring_assembly.jpg" alt="Clean wiring" width="420"/>
<img align="center" width="526" height="526" src="img/wiring/wiring_overview.jpg">
  























OBS! The servo is not glued directly on the base. It's sitting firmly in a 3d printed box which in turn is glued. Take care of your electrical devices!

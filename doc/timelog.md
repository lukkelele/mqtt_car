# Timelog

## 3/12 - 2020
 3d modeling front and back axle with their needed functionalites (steering and power transfer).
Deciding which wireless setup would work. Since we currently have no transmitters / recievers the LoPy4 is the best bet to use with the antenna. 
Checking AdafruitIO to try to set up joystick controls somehow.  \
 https://i.gyazo.com/b660e9c44b3ad1076a74874b1f657fdb.png, https://i.gyazo.com/21bdcccc6ad21998192edfab26a60c48.png
## 13/12 - 2020
Since last update the rear axle has been printed with the necessary gears to make the car move. 
The pieces I ordered (Lukas) came in the mail during this week, which was the two DC motors, batteries and a multimeter. 
Using a relay-module I could make the DC-motor start spinning via AdafruitIO, using MQTT. The setup on AdafruitIO's website is such that I have made an reset-button which sends '1' whenever the button is pressed, and a '0' when the button is released. By writing code so that during the time that the button is pressed, the DC motor will start to rotate, until the button is released. This worked very well. One issue was that when pressing the button in high frequency the website would stop responding since too much information was being sent, hence making the DC motor spin even though the button was released.
I was very intrigued by all the cables and coding, setting it all up to see it work so I added an IR-reciever on the breadboard which will sit on the car. This IR-reciever will activate some kind of lights on the car, and I managed to activate the reciever with an IR-led that I had attached to a seperate breadboard connected to a 9V battery. To make sure I had the wiring right, I used a laser module beforehand using the IR-led. At this moment I'm thinking about adding some features, what sort I'm not really sure of at this moment, but some kind of failsafe would be nice.
IR-led connected to a seperate breadboard powered by 9V. <br/>
https://gyazo.com/12b66b4a834f060b08ba11e97dacd40b  \
https://gyazo.com/28f867457fb9a54864892ea4bcc7bd74

Main breadboard with 5V-relay, IR-reciever and the DC motor. DC motor powered by 6V and the rest by the 3.3V and output pins by the Lopy4.  \
https://gyazo.com/7fbc0f1969fa3fed38deaacc8d971fec?token=d364c01db06674a06c9b60827a9de8a3

#### Total time put into project at this time, estimated 14 hours.

## 22/12-2020
Further designing on the car parts in Fusion360. The base of the car can contain batteries, the LoPy4, breadboard, servo, DC motor and a wifi antenna if needed.
## Update 7/1-2021
All parts for steering and driving the car is being printed. Lots of different prototypes, will link pics from CAD. Final touches on the base/frame for the RC-car will be done before that is printed. Dedicated spots for the lopy4, breadboard, wifi-antenna, batteries, DC motor with gears plus the servo must be carefully planned. The servo which controls the steering and its code will be provided. The servo is quite jittery so it must be secured firmly. Since me and Fardin can't meet up before the project shall be submitted, the only way to control the car will be via WIFI. Control via bluetooth is also possible since Fardin made an android application to use via phone, but the car is located at my place so WIFI will be the only option as of just now. For the video showing our results I thought it would be cool to showcase the car driving inside my apartment when Fardin is the one driving it from Växjö. I tested the code for the driveline and when problems occured with the connection or if I somehow managed to timeout the dashboard (adafruit.io) the motor would sometimes not stop spinning since the OFF-signal couldn't be recieved. This could easily happen if Fardin were to drive it from Växjö since we are about 80km apart. Solution to this would be a backup, some sort of last-will code to run if a timeout or disconnection was to occur.

## 9/1-2021
Deadline is closing in with another exam two days before. Parts have been printed with some being redesigned after flaws within the design.

# Total time and comments
I (**Lukas**) have updated gitlab poorly during the project and I wish I would've put more work in to it since by using Gitlab the work feels way more structured. I have yet to learn all the functions to effectively make the work done and progress made public. The lack of a timeline and progress has made it a thousand times harder to work especially when the deadline is closing in. So much work and effort it takes just to remind yourself of were you are, what's left and what needs to be updated causing ineffective work. Even though the results are somewhat different from what we envisioned I can safely say that I've learnt so much because of this project. Integrating code with projects like this has opened up so many doors for me and has given me a hobby for life.
<img align="right" width="482" height="394" src="img/bluetooth/timelog_chart.png">



## Improvement

This project has been somewhat of an eyeopener regarding planning and structure. Not only for schoolwork but to have an organized work        environment. To further learn from the mistakes done in this project, learning to use all features within GitLab will be interesting.
Things to think of in the future:
* Start a project by planning, noting what is to be achieved etc.
* Update reguarly
* Have an organized structure
* Accessable content
* Document activity, make us of a timelog
 ---- 


  


<br/>
<br/>

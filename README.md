## Note: This was a school project from 2020 in the course 'Introductory project'

<table align="center"><tr><td align="center" width="9999">
<img src="img/3d models/upper_view_with_breadboard.png" align="center" width="200" alt="img/3d models/upper_view_with_breadboard.png">

# MQ(ar)TT 

### a wireless mini car made entirely from 3d printed parts 
#### school project, 2020
</td></tr></table>



 <img align="center" width="306" height="192" src="img/results/sideview_finished.png"> <img align="center" width="264" height="192" src="img/results/sidepic_low.jpg"> <img align="right" width="306" height="192" src="img/results/car_overview.jpg"> 


    
    
## Abstract
With the help of 3d modeling, we have created something straight from scratch. Instead of using the base of an RC car with its steering mechanics, driving axle, and mounting our electronics we made something out of nothing and visualized a functional car made entirely from us.
We wanted to control the car by an application running via bluetooth but we ran into some issues with connectivity so we changed the direction of our connection to MQTT servers instead. During the late stages of the project problems were stacking up but we managed them.

## Background and Idea
When we were to decide what to create for this task the both of us were sure that we wanted something that wasn't static. There was many projects that couldn't move and there were no reason for them to move either since they could be a weather station or an alarm system. Both me and Fardin had no previous experience with electronics and thus we thought it would be good to keep it simple and basic. A RC-car sounded like a fun and interesting project idea that fit our reasoning and since I have a 3d printer and experience within Fusion360 the choice was made.

## Method

[Requiremments](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/doc/requirements.md)  \
[Hardware](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/doc/hardware.md)  \
[Setup](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/doc/setup.md)  \
[Timelog](https://gitlab.lnu.se/1dt308/student/team-15/-/blob/master/doc/timelog.md)  \
[Source](https://gitlab.lnu.se/1dt308/student/team-15/-/tree/master/src)  \
[Images](https://gitlab.lnu.se/1dt308/student/team-15/-/tree/master/img)  \
[Pictures of the results](https://gitlab.lnu.se/1dt308/student/team-15/-/tree/master/img/results)  \
[Fusion360 design and 3d models](https://gitlab.lnu.se/1dt308/student/team-15/-/tree/master/img/3d%20models)

## Results

Being our very first project of this kind it was very hard to get a grasp on what to do, what needed to be done and *when* it was to be done. E. Lazy updates here on gitlab created a work environment that compromised effectiveness and quality of our work. 
Starting the project with the 3d modeling which took about a total of 25-30hours, we said that the entire car was to be made out of us, all mechanical parts were included. Making different steering mechanics, gears, ball and roller bearings and mechanical parts in general in such a small size as of a RC car was a real challenge. 

The initial servo used was way too weak to be able to make the car steer left and right. It was unfortunate that we realized it very late in to the project, when all parts already had been printed. Instead of designing and printing another prototype we used lots of glue to secure crucial parts of the car that were exposed. With a little cage printed for the second servo it found it's place in the center in the front. It worked very well with the steering mechanism. It weighed a lot more than the first servo and demanded higher voltages which added lots of extra weight. If we were to consider small things like that from the beginning the end results could've been better.  <img align="right" width="380" height="380" src="img/3d models/servo_size_difference.png">

The flaws that caused the most trouble were design related. The first prototype of the driving axle hade many issues. We didn't get an accelerometer in time so we couldn't regulate the speed without directly modifying the voltages on the battery. All it took was a little gap between the gears for them to completely seperate and spin like two beyblades. By printing some small adjustments with somewhat bigger gears we could use these with the old prints and make the driving axle steady with the gears aligned. 
We knew that traction would be an issue but it was not a priority since many solutions were available and we eventually went with the rubber bands.    





 <img src="img/results/bearings.jpg" alt="img/results/bearings.jpg" width="334" height="298">



# Software , code
The code worked very well. Initially we thought that Adafruit.IO on a mobile phone could be used to press more than one button at a time but the use of momentary buttons did not work like that. The reasoning behind the three feeds *left-turn*, *right-turn* and *myfeed* was that by all being seperated one button could be pressed and another one still be held down and the information would reach the lopy. This wasn't the case and instead of buttons only triggering one function each, some values being recieved would activate both the steering and the motor. It worked well but wasn't optimal.
To remain connection to both the wifi and mqtt server was very tricky. Lots of different code was written for this loop and still it could need some work. Since the mqtt library didn't have any methods like network with .isconnected(), checking the connection status was hard. We tried many approaches, one were AdafruitIO triggers that would publish a certain value when we were connected. If we were successfully connected and subscribed to desired topics we would recieve a value or a message instead of *None* when .check_msg() or wait_msg() was active which would indicate that connection was established. The ping() method from the mqtt library was not successful either and in the end we went with try except and made our own pinging method. Using the code on the finished car worked very well and the car had great response to the input from AdafruitIO.

<br/>


<img align="center" width="612" height="454" src="img/results/car_overview.jpg">

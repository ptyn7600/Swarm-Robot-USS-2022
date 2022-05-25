# Swarm-Robot-USS-2022

## Progression
I will update what I had for a week in this section
|   Week      | Date        | Completion  |
| ----------- | ----------- | ----------- |
|     1       | May 18th - May 20th   | - Use puTTy to connect w/ the BBBlue <br/> - Connect the BBBlue to wifi <br/> - Connect the BBB wirelessly|
|     2        | May 23th - May 30th   | - Run C/Python code on the BBBlue by using RC library <br/> - Be able to control the GPIO Pins (Blink the LEDs, read the Buttons) <br>|

Note for tommorow:
- Cannot read the ECHO pin of the ultrasonics -> Attach the button to check if the GPIO is set up correctly (check the TRIG pin already by attaching the LED to it)

## What I learned

### BBBlue Pinout

<p align = "center">
<img src = "https://user-images.githubusercontent.com/92234542/169590214-6d848bc9-e1a7-4a60-bb77-7550e176be5a.jpg" height="300">
<p/>

### Connect to the BBBlue 

There are 3 ways to connect to the BBBlue:
1. Use PuTTy to connect to the BBBlue via USB cable. In PuTTY window, go to Serial connection and put in your COM port. Speed is 9600.
2. Once you connect to Use PuTTy to connect to the BBBlue wireless. Use SSH and IP address is 172.25.55.88, port is 22. Your IP address may differ from mine, and you can find it by 

## Pin map
For BonseScript,  some pin map is available in this [link](https://groups.google.com/g/beagleboard/c/xE-ntPE-jnI).

### RC Library
RC library is used, and the documentation on the library can be found [here](http://strawsondesign.com/docs/librobotcontrol/).


## Material
1. [Basic Tutorial How to log in Beagle Bone Blue](https://static.packt-cdn.com/downloads/BeagleBoneRoboticProjectsSecondEdition_ColorImages.pdf)
2. [BBBlack LED Blink](http://derekmolloy.ie/beaglebone-controlling-the-on-board-leds-using-c/)
3. [Youtube link to blink a LED on BBBlack](https://www.youtube.com/watch?v=pJWcRPcqk3g)

# Swarm-Robot-USS-2022

## Progression
I will update what I had for a week in this section
|   Week      | Date        | Completion  |
| ----------- | ----------- | ----------- |
|     1       | May 18th - May 20th   | - Use puTTy to connect w/ the BBBlue <br/> - Connect the BBBlue to wifi <br/> - Connect the BBB wirelessly|
|     2        | May 23th - May 30th   | - Run C/Python code on the BBBlue by using RC library <br/> - Be able to control the GPIO Pins (Blink the LEDs, read the Buttons) <br> - [Interface with the HC-SR04 ultrasonic sensor]()|

Note for tommorow (Friday May 27th, 2022):
- 
## What I learned

### BBBlue Pinout

<p align = "center">
<img src = "https://user-images.githubusercontent.com/92234542/169590214-6d848bc9-e1a7-4a60-bb77-7550e176be5a.jpg" height="300">
<p/>

### Connect to the BBBlue 

There are 3 ways to connect to the BBBlue:
1. Use PuTTy to connect to the BBBlue via USB cable. In PuTTY window, go to Serial connection and put in your COM port. Speed is 9600.
2. Once you connect to BBBlue via the USB cable, you can find the wifi IP address that allow you to connect the BBBlue via wifi. Refer to this [link](https://static.packt-cdn.com/downloads/BeagleBoneRoboticProjectsSecondEdition_ColorImages.pdf) to enable wifi and find the wifi IP address. Then, you can connect to the BBBlue wireless. I use SSH and IP address is 172.25.55.88, port is 22. Your IP address may differ from mine, and you can find it by "ifconfig" wanl0 in the terminal.
3. The third way is to use [cloud9](https://beagleboard.org/support/bone101). But you need to connect the BBBlue via cable to allow the cloud9 to detect your device. Cloud9 is prefer to use while programming the board because it provides a GUI that we can write code much easier than to write it in the linux window.

### Pin map
For BonseScript,  some pin map is available in this [link](https://groups.google.com/g/beagleboard/c/xE-ntPE-jnI).

### RC Library
RC library is used, and the documentation on the library can be found [here](http://strawsondesign.com/docs/librobotcontrol/).

## Ultrasonic HC-SR04 Interface w/ BBBlue

First, I get the sensor to work with the Arduino by following this [tutorial](https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6). This link also explained how the sensor works.

Then I applied the same logic and wrote it in C to work with the BBBlue. Here is [the source code](https://github.com/ptyn7600/Swarm-Robot-USS-2022/tree/main/ultrasonic_RC_Nhu).

## Some notes 
1. The 5V port is not activated if you just plug in the USB cable to power the board. You can plug both the USB cable to use cloud9 and 12V adapter to activate the 5V power port. 
2. While using functions in the GPIO library, most functions will ask for the chip and pin number of the GPIO pins. Refer to this [pin schematics](https://user-images.githubusercontent.com/92234542/169590214-6d848bc9-e1a7-4a60-bb77-7550e176be5a.jpg). For example, for port BLUE_GP0_PIN3(GPIO1_25), the chip number is 1, and pin id is 25. It's also corresponding to GPIO57 (1 * 32 + 25 = 57) in some application.


## Material
1. [Basic Tutorial How to log in Beagle Bone Blue](https://static.packt-cdn.com/downloads/BeagleBoneRoboticProjectsSecondEdition_ColorImages.pdf)
2. [BBBlack LED Blink](http://derekmolloy.ie/beaglebone-controlling-the-on-board-leds-using-c/)
3. [Youtube link to blink a LED on BBBlack](https://www.youtube.com/watch?v=pJWcRPcqk3g)

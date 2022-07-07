# Swarm-Robot-USS-2022
## LaTex Write Up 
Here is the [link](https://www.overleaf.com/read/xbrwbcxrjdyh) to the description of all experiments I have conducted.

## Progression
I will update what I had for a week in this section
|   Week      | Date        | Completion  |
| ----------- | ----------- | ----------- |
|     1       | May 18th - May 20th   | - Use puTTy to connect w/ the BBBlue <br/> - Connect the BBBlue to wifi <br/> - Connect the BBB wirelessly|
|     2       | May 23th - May 27th   | - Run C/Python code on the BBBlue by using RC library <br/> - Be able to control the GPIO Pins (Blink the LEDs, read the Buttons) <br> - [Interface the HC-SR04 ultrasonic sensor with BBBLue](https://github.com/ptyn7600/Swarm-Robot-USS-2022/tree/main/ultrasonic_RC_Nhu)|
|     3       | May 30th - June 3rd   | - Interface the IR sensor with the BBBlue <br/> - Collect data for the IR sensor |
|     4       | June 6th - June 10th    |- Collect data for the IR sensor <br/> - Analyze the IR sensor data|
|     5       | June 13th - June 17th    |- Analyze the IR sensor data <br> - Got the surface for the mean of the IR<br/>-Got the surface(line best fit) for the std of the IR <br/> - Got the distribution when we move the object to change the angle to the sensor|
|     6       | June 21th - June 24th    |- Tried plotting the distribtion of the data (the shape's not consistant among distances) <br/> - Tried to conduct the experiment with more open and empty space to double check the data (the distribution is still not promising)<br/> - Tried to plot the probability of getting the correct results|
|     7       | June 27th - June 30th    |- Finish characterize the ultrasonic sensor (only for distance)|
|     8       | July 5th - July 8th    |- Got the graph for Ultrasonic to be included in paper <br/> - C Model for the IR |


Goal for week 8 :
- Graph for ultrasonic to be included in paper ---> Done
- C Model for the IR ---> Done
- Got the graph for IR ( the same as what we have for the ultrasonic) 
- Latex Setup

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

## Ultrasonic HC-SR04 Interface w/ BBBlue([Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf))

First, I get the sensor to work with the Arduino by following this [tutorial](https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6). This link also explained how the sensor works.

Then I applied the same logic and wrote it in C to work with the BBBlue. Here is [the source code](https://github.com/ptyn7600/Swarm-Robot-USS-2022/tree/main/ultrasonic_RC_Nhu). 

Please refer to this [wiki page](https://github.com/ptyn7600/Swarm-Robot-USS-2022/wiki/Ultrasonic-Sensor---Attempts) to find more information about the Ultrasonic Sensor.

*One note while collecting hundreds or thousands of samples for analysis is that the sensor need at 0.5 seconds to reset to give accurate reading. Therefore, it will take more time to collect data for the ultrasonic than for the IR sensor. 

## IR Distance Sensor SHARP 0A41SK Interface w/ BBBlue ([Datasheet](https://www.pololu.com/file/0J713/GP2Y0A41SK0F.pdf))

First, I get the sensor to work with the Arduino by following this [tutorial]([https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6](https://create.arduino.cc/projecthub/jenniferchen/distance-measuring-sensor-900520)). This link also explained how the sensor works. I initially calibrate my sensor by following this [link](https://aleksandarhaber.com/noise-reduction-and-calibration-of-distance-sensors-sharp-infrared-sensors/).
The ADC pins can be found in below image.
<p align = "center">
<img src = "https://user-images.githubusercontent.com/92234542/170564906-142d1ee4-2e32-400f-a749-13df2335e59c.png" height="300">
<p/>

IR sensor needs more work than the ultrasonic one. Indeed, I need to collect data, generate the graph of the sensor's reading and the distane, and come up with the estimate equation for it. I follow [this link](https://aleksandarhaber.com/noise-reduction-and-calibration-of-distance-sensors-sharp-infrared-sensors/) to calibrate my IR sensor. Below is the left graph that I have for my raw data, and the right graph shows the estimation matches with the real data:

<img src = "https://github.com/ptyn7600/Swarm-Robot-USS-2022/blob/main/raw_data_graph.png" width="400" height="300" align="left">

<img src = "https://github.com/ptyn7600/Swarm-Robot-USS-2022/blob/main/estimate_graph_IR.png" width="400" height="300">

The function to estimate the distance based on the raw data is shown as follows:
<p align = "center">
<img src = "https://latex.codecogs.com/png.image?\dpi{110}\bg{white}d&space;=&space;(\frac{rawData}{k_1})^{\frac{1}{k_2}}">
<p/>
where k1 = 10599.39878314 and k2 = -0.91937492

*Note: Please refer to note 3 in Some notes section.

Please refer to this [wiki page](https://github.com/ptyn7600/Swarm-Robot-USS-2022/wiki/IR---Angle-of-the-Object-Characterization) to find more detail on how I characterize the IR sensor.

## Some notes 
1. The 5V port is not activated if you just plug in the USB cable to power the board. You must use the barrel 12V to activate the 5V power port. Since the BBBlue is fragile, do not use the 12V and the micro-USB connection simultaneously.
2. While using functions in the GPIO library, most functions will ask for the chip and pin number of the GPIO pins. Refer to this [pin schematics](https://user-images.githubusercontent.com/92234542/169590214-6d848bc9-e1a7-4a60-bb77-7550e176be5a.jpg). For example, for port BLUE_GP0_PIN3(GPIO1_25), the chip number is 1, and pin id is 25. It's also corresponding to GPIO57 (1 * 32 + 25 = 57) in some application.
3. While interfacing the IR sensor, the output voltage from the sensor output can be up to 3V. However, the Analog port of the BBBlue can only take maximum of 1.8V. Therefore, breadboard a voltage dividor for the ouptut pin of the sensor to reduce the voltage into the BBBlue. I use two 10K resistors.  


## Material
1. [Basic Tutorial How to log in Beagle Bone Blue](https://static.packt-cdn.com/downloads/BeagleBoneRoboticProjectsSecondEdition_ColorImages.pdf)
2. [BBBlack LED Blink](http://derekmolloy.ie/beaglebone-controlling-the-on-board-leds-using-c/)
3. [Youtube link to blink a LED on BBBlack](https://www.youtube.com/watch?v=pJWcRPcqk3g)


https://machinelearningmastery.com/probability-density-estimation/

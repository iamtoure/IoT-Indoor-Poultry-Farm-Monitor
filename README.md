###### Author: `Nuhuman Abubakar` `(na222nx)`

###### tags: `IoT` `LoRaWAN` `Datacake` `Helium`


# IoT Poultry Farm Monitoring

This tutorial provides steps  to build an IoT device that monitors poultry farm conditions and sends collected data over the internet. This tutorial will present on how to; 
* use sensors to collect data on; (*temperature*, *relative humidity (RH)*, *light intensity*
* store collected data from sensors on cloud
* visualize the data on a data visualization platform (that can be used for analysis purposes)

**Estimated time to build:** 4-5 hours from start to completion. 

:::info
:information_source: A basic understanding of sensors (e.g. sensor communication protocols) and sensor data gathering, python programming, LoRa communication protocol is required
:::



## Objective



Quality and safety of poultry birds have been critical to both consumers and farmers. For indoor poultry, controlled environment is necessary to maintain the quality and safety of the poultry. In poultry farming, there are four most important parameters  which are critical for the growth and health conditions of chicken. These parameters are air quality, light, temperature and humidity. 

The purpose of this project is to build an IoT device to monitor for sensoring light, temperature and humidity of indoor poultry farm.The sensor data collected will be sent over the internet to through a gateway to a cloud database which will be displayed on a dashboard. This could aid in real-time monitoring and facilitate decision making to ensure the best environmental conditions for the poultry birds.

With this device, farmers could determine critical environment conditions that need enhancements to reduce negative effects with indoor poultry




## Materials

The table below shows list of hardware used in the project, specification and price.



| Hardware                                                                                                           | Specifications                                                                                                                                | Price (SEK) |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [FiPy and sensors bundle](https://www.electrokit.com/en/product/lnu-1dt305-tillampad-iot-fipy-and-sensors-bundle/) | FiPy Development Board, Pysense 2.0 X Expansion Board, Breadboard, Antenna, Photoresistor Sensor, Resistor 10 kohm, Micro USB Data Cable, Jumper Wires | 1499.00     |
| [3 x AAA Battery holder](https://www.electrokit.com/en/product/battery-holder-3xaaa-with-switch-and-jst-connector/)|    Battery holder 3xAAA with switch and JST-connector|    29.00  


| Hardware(Datasheet)                                                                       | Function                                                                                                                                        |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [FiPy](https://docs.pycom.io/gitbook/assets/specsheets/Pycom_002_Specsheets_FiPy_v2.pdf)  | Micropython-programmable development board with five networks; WiFi, Bluetooth, LoRa, Sigfox and dual LTE-M (CAT-M1 and NB-IoT)                 |
| [Pysense 2.0 X](https://docs.pycom.io/gitbook/assets/PySense2X_specsheet.pdf)             | A  sensor shield  compatible with the FiPy. It comes with built-in sensors; Accelerometer, Light, pressure and temperature and humidity sensors |
| [Photoresistor sensor](https://www.electrokit.com/uploads/productfile/40850/40850001.pdf) | Light dependent resistor (LDR) for measuring intensity of  light.                                                                               |
| Resistor 10 kohm                                                                          | To have lower power consumption of the LDR sensor circuit                                                                                       |
| Breadboard                                                                                | Facilitates connecting multiple sensors                                                                                                         |
| Antenna  |   Omni-directional antenna for 2.4GHz for connecting to LoRaWAN                                                                                                                                              |
| Jumper Wires                                                                              | Male - Male to connect the FiPy to to Pysense and photoresistor to the breadboard                                                               |
| 3 x AAA Battery holder                                                                    | Battery holder 3xAAA with switch and JST-connector                                                                                              |
| Micro USB Data Cable                                                                      | Used to connect the development board to the computer                                                                                           |

::: info
Click on a hardware for the complete datasheet
:::


## Computer Setup

### Install Integrated Development Environment (IDE)
#### Requirement
* Computer 
* Internet connectivity

#### Steps to download and install IDE
Atom was used in this project. Follow these steps to download Atom and the required plugin

* Download and install Node JS [here](https://nodejs.org/en/)
* Download and install Atom [here](https://atom.io)
    * In Atom menu bar, navigate to `Atom >> Preferences >> Install`
    * In the search bar, search for **pymakr** and install it. (This may take some time to finish)

:::success
:thumbsup: Now ready for the next step; Device Firmware Update
:::

### Device Firmware Update
#### Requirement
* FiPy development board
* Pysense expansion board 2.0 X
* Micro USB Data cable

:::info
Pycom recommends upgrading the firmware to the latest version
:::

#### Steps to update the firmware
* Mount the FiPy to the PySense 2.0 X (push to make sure the FiPy sits in properly) as shown in the image below 
![](https://i.imgur.com/vCmbuf4.png)
* Using the Micro USB data cable, connect the device to the computer
* Download and install the updating tool [here](https://docs.pycom.io/updatefirmware/device/)
* Open the installed  application 
* Follow the steps below to update(upgrade) the device firmware:
    * Check `Include development releases` and click **Continue** and **Continue** again on the next screen
    ![](https://i.imgur.com/58vTxoa.png)
    * In the `Port` dropdown on the **Communication** screen, select **/dev/cu.usbmodemPy...**
    * Check **High speed transfer**
    * Check **Show Advanced Settings**
    ![](https://i.imgur.com/NgAc45c.png)
    * Select **development** under the **Type** dropdown and click **Continue**
    ![](https://i.imgur.com/BESiDIR.png)
    * The tool detects the board and its information automatically. Check `Erase during update`, `CONFIG partition` and `NVS partition` and click **Continue** 
    ![](https://i.imgur.com/y09h0Z3.png)
    *  The device firmware version is now upgraded to the latest version. Click on **Done** to close the tool.
    ![](https://i.imgur.com/v2If2SP.png)

    
:::success
:thumbsup: Ready to upload and run code in IDE (Python)
:::

### Upload code and run code in IDE
*  Open Atom
*  Disconnect and reconnect the device to the computer
*  The device should be connected automatically, if not click on the `Connect Device`. The device port should be in the dropdown, click to connect it as shown in the image below
![](https://i.imgur.com/9EEJSzE.png)
* Once connected, REPL is accessible, type `print(1+1)` and enter which should output the answer `2`
![](https://i.imgur.com/ORKpuR0.png)
* All set to create first project. On the computer, create a new folder and name it e.g. `IoT Project`
* On the left pane in Atom, click `Add Folder` and select the `IoT Project` folder created earlier and click open to add to Atom
* The folder should be added in the left pane, right-click on it to add`New File`. Type `main.py` to name the file and press enter, this should create a file with the name `main.py` under the `IoT Project` folder
* On the right pane of Atom `main.py` should be opened, copy and paste the below code in it and save it using `File` in the menu bar
```

import pycom
import time

pycom.heartbeat(False)

while True: #Forever loop
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    
#Source: https://hackmd.io/@lnu-iot/rk4qNlajd
``` 
* Upload the project to the device by following these 3 simple steps 
    1. Click on the project and make sure to select `IoT Project`
    1. Ensure the device is connected to Atom. (It is connected when there is a green dot as shown in the image)
    1. Click on `Upload Project`
    ![](https://i.imgur.com/01wOc75.png)
* By doing everything right, the LED on the FiPy will blink Red, Orange and Green continuosly. Click anywhere in the REPL and press `Ctrl-c` on the keyboard to interrupt (stop the blink)

:::success
The code test on the device is successful and ready for the next step of putting things together 
:::

## Putting everything together

:::info
Disconnect device from the computer before proceeding with the next steps
:::

### Expanding pin for extra sensor connection
* Dismount FiPy on PySense 2.0 X
* Mount FiPy on breadboard (overlapping gap across the breadboard to bridge it)



![](https://i.imgur.com/NfTk5zT.png)



:::danger
**Check the connections if they are as in the schema as many times as possible before connecting USB cable. Cannot be overcautious here**
:::
### Main Power Connections
* 5V from expansion board to the breadboard (indicated with red wire in the schematics).
* Ground (GND) from the expansion board to the GND pin of the FiPy connected on the breadboard (black wire in the schematics).
* 3.3V from the expansion board to the 3V3 pin of the FiPy connected on the breadboard (Blue wire in the schematics).

### Data Connection
* Connect **Universal Asynchronous Receiver/Transmitter - UART** between the PySense 2.0 X and FiPy. Orange and Yellow wires from the FiPy to the PySense 2.0 X. 
* Connect SCL and SDA pins between the FiPy and PySense 2.0 X as shown with White and Green wires respectively in the image above.

### Sensor/Resistor Connections
The sensors are connected according to the schematics above. The setup allows for using built-in sensors as well as extral sensors.
#### Photoresistor

* The photoresistor is connected directly on the breadboard
* Blue wire is drawn from one of the pins of the photoresistor to provide the required 3.3V power of the photoresistor.
* Black wire from the second pin of the photoresistor is connected to the GND pin of the FiPy on the breadboard.
* A 10 kohm resistor is connected adjacent to the second pin of the photoresistor along the breadboard reserving available pins between the photoresistor and the 10 kohm resistor.
* Yellow wire drawn from  a reserved pin between the photoresistor and the 10 kohm resistor for data transmission to Pin 16 (as selected in the code) of FiPy on the breadboard. 

:::warning
Connect the pins exactly as connected in the schematics above. refer to datasheets if unsure
:::


#### Power Consumption


| Component             | Mode    | Current Draw |
| --------------------- | ------- | ------------ |
| FiPy                  | Idle    | ~62.7 mA     |
| FiPy*                  | LoRA Tx | ~28  mA    |
| PySense Sensors (All) | Active  | ~7           |
| PySense Sensors (All) | Sleep   | ~9uA         |
| Photoresistor         | Active  | ~0.5 mA      |

*Source: [RS-Online](https://docs.rs-online.com/77c6/0900766b815d0a8d.pdf)

* Each AAA battery provide 1000mWh at 1.2V translating to 3000mWh at 3.6V required for the JST battery connector which is `~833.33mAh`
* For this project, the device reads once every 5 minutes lasting ~15seconds. Therefore in a every one hour, the device will be powered on 450 seconds and sleeps 3150 seconds. 

#### Electrical Calculations of Device
The dissipitated power of the device is the sum of the power draw of all sensors while sensing, microcontroller power(while active and in standby modes) and power for transmitting to gateway

`[(sensors) + device] * In/active time/hour  = hourly current draw for device to use all sensors`. 
* #####  Transmitting over LoRA
`((0.5mA + 7mA + 28mA) * 450 seconds = 35.5mA * 0.125h = ~4.44mAh`
* ##### While idle/standby
`62.7mA + 0.009 * 3150 seconds = 62.709mA * 0.875h = ~54.87mAh`
* Total current draw is therefore `4.44mAh + 54.87mAh = ~59.31mAh `
The battery can  power the device continuously for ~ 14 hours. `833.33/59.31 = ~14 hours` 

NB: An increased time between readings will reduce current draw hence prolong the hours in which the battery pack can power the device and vice versa. However, an increased time between readings may result in missing significant data. A reduced reading interval could also lead to redundant data and maximize bandwidth and power usage.  


:::info
:bulb: No data on individual power draw for built-in Pysense sensors, but for "All sensors", therefore it was assumed all the sensors will be used instead of just one. This means overshooting of power draw 
:::


## Platform
### Datacake
For this project, [Pybytes](https://sso.pycom.io/login/?client_id=pycom&redirect_uri=https%3A%2F%2Fpyauth.pybytes.pycom.io%2Fauth_code%2Fcallback&scope=profile&response_type=code&state=pybytes-browser) and [Datacake](https://datacake.co) were tested. Like Pybytes, Datacake is a low-code platform that requires little to no programming skill. Datacake was chosen over the former as it has enhanced dashboards and easy dashboard configuration. Also, it has the ability to set rules at predetermined thresholds. Above all, less time is required to create applications. It is as functional as easy to use. Even though other self-hosted platforms like TIG-Stack, [Node-RED](https://nodered.org) provide advanced and more improved dashboards and much control over data, the coding level required is higher and due to time constraints, these platforms are not suitable for this project. However, they offer better options than Datacake which can be used to upscale or enhance this project.

## The Code

All codes used in this project can be found at this Github [link](https://github.com/iamtoure/IoT-Indoor-Poultry-Farm-Monitor).

The GitHub repository contains
* `lib` folder which has two libraries for the Temperature/ Humidity sensor which was adopted from the [Pycom github repository](https://github.com/pycom/pycom-libraries) and the Pycoproc 2,   a supporting library for the Pysense 2.0 X 
* `boot.py` to connect to LoRaWAN
* `main.py` holds the working code of the project
* `Payload Decoder` code for Datacake configuration
* Other test codes for initial setup



## Transmitting the data / Connectivity

### Connectivity

The device is connected to the Datacake using [LoRaWAN](https://lora-alliance.org/about-lorawan/). LoRaWAN offers a long range wide area network coverage. With this, the device can be connected over a long distance of up to three miles (five kilometers) in urban areas, and up to 10 miles (15 kilometers) or more in rural areas (line of sight). Also, its low power consumption means more device can run on battery longer. Data is sent to Helium once every five minutes and sleeps after each sleeps after each transmission to save power.

#### Steps to connect to LoRaWAN on Helium
* Create a Helium account [here](https://console.helium.com)
* Add the device to Helium. Click on the button **Add Device** ![](https://i.imgur.com/Aa5oY8d.png)
* Give the device a name. NB: Helium generates Dev EUI, App EUI and App Key
* Click save to add the device

![](https://i.imgur.com/Vyoavsb.jpg)


::: success
Device added successfully
:::

#### Connect Device

::: danger
**LoRa Antenna must be connected properly before running LoRa code to avoid breaking the device**
:::
* Connect antenna to LoRa antenna connector. If unsure, refer to  datasheet [here](https://docs.pycom.io/gitbook/assets/specsheets/Pycom_002_Specsheets_FiPy_v2.pdf)
* Open Atom IDE and add a `boot.py` file. Copy and paste this [snippet](https://github.com/iamtoure/IoT-Indoor-Poultry-Farm-Monitor/blob/6549805b2f294423b02d2a2c23b221ad6fbfe0cf/LoRa) in it
* Replace the 0s in line 7 and 9 with the generated `Dev EUI` and `App Key` from Helium.
* Connect device and run the `boot.py` file.
* Once the device connects, REPL will print `Network Joined` else `Not joined yet...`

:::info
Check if Helium has hotspot around. It can take up to 20 mins the first time connecting.
:::

### Transmitting the data

The device transmits data over LoRa to Datacake using [Helium](https://www.helium.com/console).

To transmit the data, Datacake needs to be integrated to Helium and create a connection flow. Below steps will describe the process 

* Tutorials on adding device to Helium [here](https://docs.helium.com/use-the-network/console/adding-devices)
* [Here](h[ttps://docs.helium.com/use-the-network/console/adding-devices](https://docs.helium.com/use-the-network/console/integrations/datacake/)) are tutorials to integrate Datacake to Helium
* Final step to create a connection is to add a Flow. More information can be found on [Helium](https://docs.helium.com/use-the-network/console/flows/)
* After creating a flow, follow these steps to update these settings; 
    * Click on device name
    * Navigate to `Configuration`
    * Scroll to `Payload Decoder` and paste this [code](https://github.com/iamtoure/IoT-Indoor-Poultry-Farm-Monitor/blob/6549805b2f294423b02d2a2c23b221ad6fbfe0cf/Payload%20Decoder) in. It will save automatically
    * Scroll further down to `Fields`. Here, fields will be created using the same field identifier as in the code used in the Payload Decoder. Any typos will affect data transmission.


Also, in the `main.py` code uploaded to the device, the data is packaged using the `struct.pack()` to reduce the size of data being sent due to the limited bandwidth.

![](https://i.imgur.com/pEqWRH2.png)


## Presenting the data
Screenshots of the dashboards for the monitored parameters. Datacake supports mobile view for dashboards. Dashboards can be shared through a public link or QR Code. An example of the [dashboard](https://app.datacake.de/pd/a8916264-3e92-4411-ae21-429836c3cbf7) 


* Temperature
* Relative Humidity 
* Light Intensity

![](https://i.imgur.com/rQ6SqRw.jpg)




*Mobile view dashboard*


![](https://i.imgur.com/BSnMujI.png)



*Desktop view dashboard*

### Rules
In Datacake, rules are set with few clicks. Different measures can be set under rules following set conditions. The measures include, webhook, Email, SMS etc. However, Email option was used in this project. Emails are sent to specified receivers to alert critical conditions. Datacake allows for rules to "Deactivate" the rules temporarily, which could be good for debugging or other maintenance purposes. 

Here is a screenshot of alerts received in email when conditions were met in the Rules

![](https://i.imgur.com/vmlEMzG.jpg)


### Data Retention
Datacake offers a Free Plan which is limited to 2 devices per user account. This plan was used for this project. The Free Plan also means a cap on the amount of datapoints which is 500 datapoints/ day and a 7-day data retention. This is enough for the purposes of prototyping this project. But for scalability, this is not enough and the paid plans will be opted for which provides optimized services in terms of datapoints, data retention and number of users.

## Conclusion
### Final Design
Some selected images for the finalized design of the device
![](https://i.imgur.com/j1W21Na.jpg)
 

![](https://i.imgur.com/MK1KxN8.jpg)

![](https://i.imgur.com/mH3vmMS.jpg)

![](https://i.imgur.com/FWpwGLH.jpg)




### Reflections

#### Project Specific

The initial project was to measure much more parameters, however, after procuring a sensor, it brought about a lot of challenges which time did not permit to overcome before the deadline. With that said, it does not stop there but continue to probe further and discuss with other IoT experts and enthusiasts to troubleshoot and find a solution and/or work around the problem. 

Insights from the data collected can be used in diverse ways especially machine learning algorithms to detect health of birds and other useful information on the birds.

Although the project has been streamlined to focus on poultry farms, it can be implemented and adjusted to different areas that require similar parameters to be measured.


#### General Reflection

The purpose for joining this course has been met which is to learn while having fun 🤩. Like every learning journey, it has had its highs and lows. Like a space shuttle, it starts from a low point to reach the space and sometimes do not lift off at all until after several tries. But when it finally does and reaches its destination, the data obtained is worth the struggle. What I have learned in this course will go a long way to help in shaping my career objective.

Joining this course has exposed me to different knowledge sharing platforms on IoT and other areas which I have not known existed before. The knowledge sharing open platforms have provided a different perspective of the world to me.  

###### YouTube Video Links:
###### https://youtu.be/C4Mk48ZZExs
###### https://youtu.be/9Oy-O60Tsjk
###### https://youtu.be/OOrDG_gI1Xg
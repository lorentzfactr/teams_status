# Description

A simple python script that parses the MSFT Teams log file for the users current Teams status and then outputs the status color to a MQTT connected light. 


## Project: Teams Light
## Written By: Lorentz Factr
## Date: 2/1/2022


### Instructions & Prerequisites:

  **1.** Setup an MQTT broker service with a TOPIC called "TEAMS_STATUS"
  **2.** Setup an MQTT controlled light source that subscribes to your MQTT broker with topic "TEAMS_STATUS" on port 1883.
  **3.** The default settings of this program assumes your light source accepts instructions as a formated string "R,G,B" (line 24).
  **4.** If your light source is not setup to accept the format I designed, you will need update to the key values in the 
          custom_return dictionary with what your subcriber expect (line 28).
  **5.** Update the mqtt_broker variable with YOUR MQTT broker IP address (DONT USE 'localhost') or public domain (line 35)
  **6.** Update the filepath to the logs.txt location in your computer (line 38).
  **7.** Not required: update the hard interval update to the desired amount of time in seconds (line 49)
  **8.** If you want to run this on startup... Make a shortcut to teams_light.py, move the short cut here: %appdata%\Microsoft\Windows\Start Menu\Programs\Startup

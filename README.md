#About


Mausam is a weather monitoring system using Iot to monitor and analyse the various parameters of the surrounding
Live Demo mausam.freetzi.com


#Installation

Download Arduino IDE
Python 3.5 and above 
httplib2 (pip install)
serial (pip install)
requests (pip install)
time (pip install)
install twilio

#Usage

import httplib2
import serial
import requests
import time

#Installation Guide

1.	Uplode the code into the arduino
2.	Once uploaded successfully, run the pycode.py to read andupload the code to cloud and even trigger sms alert if conditio are met.
3.	The data is sent to channel whose API key is provided with channel number
4.	For sms slert create an account in twilio and set the virtual number in pycode.py
5.	Data is the read from the cloud by the website mausam.freetzi.com and displayed
6.	Machine learning is applied for processing 

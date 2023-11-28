#!/usr/bin/env python3
"""
A very basic simple system for sending Raspberry Pi GPIO pin input information over OSC.
This example uses an accompanying Pure Data patch, though you could pair this with any OSC compatible software.

Currently set up for two buttons, but could be expanded of course.

Input only, this does not do output. 

I am an extremely inexperienced Python coder so I probably can't answer any questions. 
But you are welcome to get in touch if you like: yann@yannseznec.com

Requires Python-OSC and RPi.Gpio. Install those first.

- Yann, November 2023

"""
from pythonosc import udp_client
from pythonosc import osc_message_builder
import time
import random
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM) # make sure you are connected to the right Pi pins, there are different ways and they are all slightly different and it is stupid
chan_list = [3,4] # what pins you are using
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) # this throws a weird message about hardware pullups, but also seems to activate software pullups and helps clean the data. hardware pullup resistors appear optional...
GPIO.add_event_detect(3, GPIO.BOTH) # i couldn't figure out how to make this automatic for each pin listed in the array above, because i'm bad at python
GPIO.add_event_detect(4, GPIO.BOTH)


def main():
  oscSender = udp_client.UDPClient("localhost", 2222) # change the number to whatever you are using in your other software
  while True:
    # one day i will figure out how to do for loops in python and make this easier. for now you have to copy and paste and change values:
    if GPIO.event_detected(3):
        msg = osc_message_builder.OscMessageBuilder(address = "/buttonPress1")
        msg.add_arg(GPIO.input(3))
        oscSender.send(msg.build())
        # print(GPIO.input(2))
    if GPIO.event_detected(4):
        msg = osc_message_builder.OscMessageBuilder(address = "/buttonPress2")
        msg.add_arg(GPIO.input(4))
        oscSender.send(msg.build())
        # print(GPIO.input(2))
    
  #  print(n)
  #  print(GPIO.input(2))
    
    

if __name__ == "__main__":
  main()
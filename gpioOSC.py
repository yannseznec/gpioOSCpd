#!/usr/bin/env python3
"""
OSC/Random Example: send random numbers to OSC.

This example sends a pseudo-random number between 0 and 1024
to the OSC receiver on UDP port 2222.
"""
from pythonosc import udp_client
from pythonosc import osc_message_builder
import time
import random
import RPi.GPIO as GPIO

chan_list = [2]
#check that this channel is correct vis-a-vis the board definition
# add as many channels as you want!
# you can tuples instead i.e.:
#   chan_list = (11,12)
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO) 

def main():
    oscSender = udp_client.UDPClient("localhost", 2222)
    GPIO.add_event_detect(2, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(2):
    print('Button pressed') #put the OSC
    while True:
        n = random.randint(0, 1024)
        print(n)
        msg = osc_message_builder.OscMessageBuilder(address = "/rand")
        msg.add_arg(n)
        oscSender.send(msg.build())
        time.sleep(0.1)  

if __name__ == "__main__":
  main()
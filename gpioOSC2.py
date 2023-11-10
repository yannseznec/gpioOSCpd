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
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)
GPIO.add_event_detect(2, GPIO.BOTH)


def main():
  oscSender = udp_client.UDPClient("localhost", 2222)
  while True:
    
    if GPIO.event_detected(2):
        msg = osc_message_builder.OscMessageBuilder(address = "/buttonPress1")
        msg.add_arg(GPIO.input(2))
        oscSender.send(msg.build())
        # print(GPIO.input(2))
    
  #  print(n)
  #  print(GPIO.input(2))
    
    

if __name__ == "__main__":
  main()
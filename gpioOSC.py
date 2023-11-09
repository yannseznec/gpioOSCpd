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


def main():
  oscSender = udp_client.UDPClient("localhost", 2222)
  while True:
    b = GPIO.input(2)
    n = random.randint(0, 1024)
  #  print(n)
  #  print(GPIO.input(2))
    msg = osc_message_builder.OscMessageBuilder(address = "/buttonPress")
    msg.add_arg(b)
    oscSender.send(msg.build())

    time.sleep(0.01)  

if __name__ == "__main__":
  main()
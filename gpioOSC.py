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


def main():
  oscSender = udp_client.UDPClient("localhost", 2222)
  while True:
    n = random.randint(0, 1024)
  #  print(n)

    msg = osc_message_builder.OscMessageBuilder(address = "/rand")
    msg.add_arg(n)
    oscSender.send(msg.build())

    time.sleep(1)  

if __name__ == "__main__":
  main()
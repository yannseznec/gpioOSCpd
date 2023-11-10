# gpioOSCpd
summary: 
Raspberry Pi -> GPIO -> OSC -> Pure Data

This is a bare-bones system for sending Raspberry Pi GPIO pin input information over OSC to Pure Data.

This example uses an accompanying Pure Data patch, though you could pair this with any OSC compatible software.

Input only, this does not do output. Output is possible but I'm just trying to keep this as bare-bones as possible for my current purposes.

I am an extremely inexperienced Python coder so I probably can't answer any questions. 
But you are welcome to get in touch if you like: yann@yannseznec.com

Off the top of my head, this requires:
- Python-OSC: https://pypi.org/project/python-osc/
- RPi.Gpio: https://pypi.org/project/RPi.GPIO/
- Pure Data (or other OSC software as mentioned above): http://puredata.info

You can install those all by using apt-get or pip. Running these on the command line on the Raspberry Pi should work: 
 sudo apt-get install python-rpi.gpio python3-rpi.gpio
 sudo apt-get install puredata
 sudo pip install pythonosc

For some reason on my Raspberry Pi I could not install via pip until I ran this:
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

I have no idea why, so I would suggest being careful about that.

to run this example, get the python code and Pd patch onto your Pi somehow. Then run:

python gpioOSC.py &
pd -nogui osc.pd

Connect a button to pin 2 and ground on the Raspberry Pi. Pressing the button should print 0 and 1 to the command line while the system is running.

To run this on startup, copy those two lines and put add them to the bottom of /etc/rc.local just above the "exit 0" line. Make sure you have set the Pi to auto-login at startup.


import os
from gpiozero import Button
button = Button(2)

def send2Pd(message=''):
	os.system("echo '" + message + "' | pdsend 3000")

button.wait_for_press():
def audioOn():
	message = '0 1;'
	send2Pd(message)

import os

def send2Pd(message=''):
	os.system("echo '" + message + "' | pdsend 3000")

def audioOn():
	message = '0 1;'
	send2Pd(message)
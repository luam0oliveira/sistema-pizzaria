import os
import time


def clear_console():
	os.system('cls' if os.name == 'nt' else 'clear')

def delay(sec = 0.1):
	time.sleep(sec)

def emptyToNone(string):
	if string == '':
		return None
	return string

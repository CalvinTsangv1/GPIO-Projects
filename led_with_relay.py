'''
lgpio (Linux- General Purpose Input/Output) is a library for controlling GPIO pins

allow user to read and write to GPIO pins
support PWM (Pulse Width Modulation), is used for dimming LEDs, controlling motors etc
'''


from gpiozero import LED
from time import sleep

makerobo_RelayPin = LED(17)

def makerobo_setup():
	makerobo_RelayPin.off()
	
def makerobo_loop():
	while True:
		makerobo_RelayPin.on()
		sleep(2)
		makerobo_RelayPin.off()
		sleep(2)
		()

def makerobo_destroy():
	makerobo_RelayPin.close()
	
if __name__ == "__main__":
	makerobo_setup()
	try:
		makerobo_loop()
	except KeyboardInterrupt:
		makerobo_destroy()

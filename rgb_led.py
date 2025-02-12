from gpiozero import RGBLED
from colorzero import Color
from time import sleep

colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black','gray','orange','pink','olive', 'aqua','gold','purple','brown']

led = RGBLED(17,18,27)

def makerobo_loop():
	while True:
		for color in colors:
			led.color = Color(color)
			print(f"color{led.color}")
			sleep(1)
def makerobo_destroy():
	led.close()
	
if __name__ == "__main__":
	try:
		makerobo_loop()
	except KeyboardInterrupt:
		makerobo_destroy()

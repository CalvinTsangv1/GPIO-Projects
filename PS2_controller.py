from gpiozero import Button, MCP3008
from gpiozero.tools import absoluted, scaled
from signal import pause
from time import sleep

pot_x = MCP3008(channel=0)
pot_y = MCP3008(channel=1)
pot_z = MCP3008(channel=2)

def MAP(x, in_min, in_max, out_min, out_max):
	return (

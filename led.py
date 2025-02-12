'''
lgpio (Linux- General Purpose Input/Output) is a library for controlling GPIO pins

allow user to read and write to GPIO pins
support PWM (Pulse Width Modulation), is used for dimming LEDs, controlling motors etc
'''


import lgpio
from time import sleep

makerobo_pins = (12, 18)

h = lgpio.gpiochip_open(0)

PWM_FREQ = 2000

lgpio.gpio_claim_output(h, makerobo_pins[0])
lgpio.gpio_claim_output(h, makerobo_pins[1])

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]

def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max - out_min)  / (in_max - in_min) + out_min)
    
def makerobo_set_Color(color):
    R_val = (color >> 8) & 0xFF
    G_val = color & 0xFF
    
    R_val = int(makerobo_pwm_map(R_val, 0, 255, 0, 100))
    G_val = int(makerobo_pwm_map(G_val, 0, 255, 0, 100))
    
    print(f"Setting color: R={R_val}, G={G_val}")
    
    lgpio.tx_pwm(h, makerobo_pins[0], PWM_FREQ, R_val)
    lgpio.tx_pwm(h, makerobo_pins[1], PWM_FREQ, G_val)
    
def makerobo_loop():
    try:
        while True:
            for col in colors:
                makerobo_set_Color(col)
                sleep(5)
                print("----")
    except KeyboardInterrupt:
        makerobo_destroy()
        
def makerobo_destroy():
    lgpio.gpiochip_close(h)
    
if __name__ == "__main__":
    makerobo_loop()
    

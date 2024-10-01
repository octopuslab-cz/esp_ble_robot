# basic OctopusLAB library for ws RGB neopixel led - single/strip/ring
# (c) octopusLAB 2017-23

__version__ = "2.0.3"

from time import sleep, sleep_ms
import urandom
from random import randint
from machine import Pin
from neopixel import NeoPixel
from components.ws_rgb.colors_rgb import *


def wheel(pos, dev = 1):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (int((255 - pos * 3)/dev), int((pos * 3)/dev), 0)
        if pos < 170:
            pos -= 85
            return (0, int((255 - pos * 3)/dev), int((pos * 3)/dev))
        pos -= 170
        return (int((pos * 3)/dev), 0,  int((255 - pos * 3)/dev))

"""
def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val
"""

def random_color():
    #return wheel(urandom(1)[0])
    return wheel(randint(0,255))


def random_color_one(col="G"):
    if col == "R": num = 0
    if col == "G": num = 80
    if col == "B": num = 128
    add = randint(1,30)
    return wheel(num+add)



class Rgb(NeoPixel):
    def __init__(self, pin, num=1):
        self.pin = pin
        self.num = num
        self.np = NeoPixel(Pin(self.pin, Pin.OUT), self.num)
        # self.np = super().__init__(Pin(self.pin, Pin.OUT), self.num)

    def simpleTest(self, wait_ms=500):
        self.np[0] = RED
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = GREEN
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = BLUE
        self.np.write()
        sleep_ms(wait_ms)

        self.np[0] = (0, 0, 0)
        self.np.write()


    def color(self, color=RED, i=0):
        self.np[i] = color
        self.np.write()


    def color_chase(self, np, num_pixels, color, wait):
        for i in range(self.num):
            self.np[i] = color
            self.np.write()
            sleep(wait)

    def rainbow_cycle(self, wait=3, intensity = 2):
        for j in range(255):
            for i in range(self.num):
                rc_index = (i * 256 // self.num) + j
                self.np[i] = wheel(rc_index & 255, dev = intensity)
            self.np.write()
            sleep_ms(wait)

    
    def fill(self, color):
        for i in range(self.num):
            self.np[i] = color
            self.np.write()     
    
    
    def test(self):
        #https://github.com/maxking/micropython/blob/master/rainbow.py
        self.simpleTest()

        self.color_chase(self.np, self.num,RED, 0.1)  # Increase the number to slow down the color chase
        self.color_chase(self.np, self.num,YELLOW, 0.1)
        self.color_chase(self.np, self.num,GREEN, 0.1)
        self.color_chase(self.np, self.num,CYAN, 0.1)
        self.color_chase(self.np, self.num,BLUE, 0.1)
        self.color_chase(self.np, self.num,PURPLE, 0.1)

        self.rainbow_cycle()  # Increase the number to slow down the rainbow
        sleep(1)

        self.np.fill(BLACK)
        self.np.write()

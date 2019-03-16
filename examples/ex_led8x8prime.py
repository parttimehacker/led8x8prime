#!/usr/bin/python3
""" Example of the prime number 8x8 LED matrix dispplay class """

from threading import Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

from led8x8prime.led8x8prime import Led8x8Prime

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = BicolorMatrix8x8.BicolorMatrix8x8()
    PRIME = Led8x8Prime(DISPLAY, LOCK)
    PRIME.reset()
    while True:
    	PRIME.display()


"""
Scope: Blinking an LED
Uses: Micropython
G. Papalambrou
File: picoL1.py
"""


import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
while True:
    led.toggle()
    time.sleep(1)



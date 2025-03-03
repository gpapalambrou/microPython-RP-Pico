"""
Blink external LED
Read button if pressed

GP, 3/3/25
File: L2-1.py
"""


import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Only LED blinks
"""
while True:
    led_external.toggle()
    utime.sleep(1)
"""


# Combined actions
while True:
    if button.value() == 1:
        led_external.value(1)
        utime.sleep(2)
    led_external.value(0)    
#!/usr/bin/env python

import colorsys
import time
import os

from blinkt import set_clear_on_exit, set_brightness, set_pixel, show


spacing = 360.0 / 16.0
hue = 0

set_clear_on_exit()
set_brightness(0.1)

S = float(os.getenv('SVAL', '1.0'))
V = float(os.getenv('VVAL', '1.0'))

while True:
    hue = int(time.time() * 100) % 360
    for x in range(8):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, S, V)]
        set_pixel(x,r,g,b)
    show()
    time.sleep(0.001)

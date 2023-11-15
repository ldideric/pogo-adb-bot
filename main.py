#!/usr/bin/env python3

import io
import subprocess
from ppadb.client import Client
from PIL import Image
import numpy
import time

# Setup adb

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# Finding search bar

image = Image.open(io.BytesIO(device.screencap()))

width, height = image.size

middle_x = width // 2

with open("pixels.txt", "w") as f:
    for y in range(height):
        pixel_color = image.getpixel((middle_x, y))
        f.write(f"{pixel_color}\n")

def find_occurrence(image, middle_x, height, direction):
    occurrence = None
    for y in direction(height):
        pixel_color = image.getpixel((middle_x, y))
        if pixel_color == (222, 233, 214, 255):
            if occurrence is None:
                occurrence = y
            if abs(occurrence - y) >= 10:
                break
    return occurrence

first_occurrence = find_occurrence(image, middle_x, height, range)
last_occurrence = find_occurrence(image, middle_x, height, lambda x: reversed(range(x)))

middle_y = (first_occurrence + last_occurrence) // 2

device.shell(f"input tap {middle_x} {middle_y}")

device.shell("input text '!traded&1*,2*'")

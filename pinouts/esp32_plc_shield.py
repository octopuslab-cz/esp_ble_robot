# (c) OctopusLAB 2017-23 - MIT
"""
This is octopusLab basic library for PLC Shield on ESP32board
"""
from micropython import const
from pinouts.esp32_base import *

# PIN as on octopusLAB LAN board 1 with built-in ESP32

#I2C:
I2C_SCL_PIN = const(16)
I2C_SDA_PIN = const(2)

# Input pins
I39_PIN = const(39)
I34_PIN = const(34)
I35_PIN = const(35)

BUTT1_PIN = const(0) # up

# UART 1
RXD1 = const(36)
TXD1 = const(4)

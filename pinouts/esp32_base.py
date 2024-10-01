# (c) OctopusLAB 2017-23 - MIT
# Base Octopuslab based board, some basic interfaces like I2C, SPI

from pinouts.base import *

BUILT_IN_LED = const(2)
HALL_SENSOR = const(8)

#I2C:
I2C_SCL_PIN = const(22)
I2C_SDA_PIN = const(21)

# SPI:
SPI_CLK_PIN  = const(18)
SPI_MISO_PIN = const(19)
SPI_MOSI_PIN = const(23)
SPI_CS0_PIN  = const(5)

# UART 0
RXD0 = const(3) # Used for REPL
TXD0 = const(1) # Used for REPL
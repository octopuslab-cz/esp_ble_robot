# upyp > mip / v1.19.1803+
# https://docs.micropython.org/en/latest/reference/packages.html
# mip: micropython installs packages

print("init")

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)

wlan.active(True)
sleep(5)

# wlan.connect('ssid', 'password')
print("wifi connect")
#wlan.connect("Monastery", "t0pm0nkswifi")
#wlan.connect("UPCDEA3B7C", "fudbexMj8xas")
# wlan.connect("O2-internet-5G-975","OrLzmCnd")
# wlan.connect("UPCDC21985","fuu2rFefzw6t")
wlan.connect("IoT", "octopus19")
sleep(5)


print("--> [github:octopuslab-cz/esp32_micropython_framework]")
mip.install("github:octopuslab-cz/esp32_micropython_framework", target=".")

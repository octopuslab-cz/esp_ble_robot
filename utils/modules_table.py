# (c) OctopusLAB 2017-23 - MIT

import gc

LW=29 # LEFT_WIDTH


def get_ver(module,subdir="components."):
    try:
        imported_module = __import__(subdir + module)
        return getattr(imported_module, module).__version__
    except (ImportError, AttributeError):
        return "Version information not available."

"""
    import components.led as led
    print("{:<{width}}{}".format("components.led", led.__version__, width=LW))
"""

    
def print_ver(module,subdir="components."):
    print("{:<{width}}{}".format(f"{subdir}{module}", get_ver(module,subdir), width=LW))
    
# print(get_ver("led"))
print("-"*LW)
print_ver("octopus_lib","lib.")
print_ver("octopus_decor","lib.")
print_ver("octopus_digital","lib.")
print_ver("octopus_transform","lib.")
print_ver("octopus_api","lib.")
print_ver("pubsub","lib.")
gc.collect()

print("-"*LW)
print_ver("led")
print_ver("button")
print_ver("ws_rgb")
print_ver("pwm")
print_ver("buzzer")
print_ver("i2c_expander")
# #print_ver("servo")
print_ver("display4")
print_ver("display8")
print_ver("display_i2c_lcd")
print_ver("display_i2c_oled")
print_ver("display_serial")
print_ver("ds18b20")
print_ver("i2c_eeprom_24xxx")
gc.collect()

print("-"*LW)
print_ver("","config.")

print("-"*LW)
print_ver("pinout","utils.")
print_ver("setup","utils.")
print_ver("sys_info","utils.")
print_ver("wifi_connect","utils.")
gc.collect()

# import components.display7 as display7
# print("{:<{width}}{}".format("components.display7", display7.__version__, width=LW))
# ImportError: no module named 'octopus_lib'

# import components.oled as oled
# print("{:<{width}}{}".format("components.oled", oled.__version__, width=LW))
# ImportError: no module named 'ssd1306'

print("-"*LW)
import components.servo as servo
print("{:<{width}}{}".format("components.servo", servo.__version__, width=LW))

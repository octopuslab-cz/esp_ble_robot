
# from utils.sys_info import sys_info
# sys_info()

__version__ = "1.0.9" # 15.07.2023

import machine
import os, ubinascii
import gc #mem_free

rtc = machine.RTC() # real time

def get_eui():
    id = ubinascii.hexlify(machine.unique_id()).decode()
    return id #mac2eui(id)

def add0(sn):
    ret_str=str(sn)
    if int(sn)<10:
       ret_str = "0"+str(sn)
    return ret_str

def get_hhmm():
    #print(str(rtc.datetime()[4])+":"+str(rtc.datetime()[5]))
    hh=add0(rtc.datetime()[4])
    mm=add0(rtc.datetime()[5])
    return hh+":"+mm

def sys_info():
   print("> unique_id: "+str(get_eui()))
   #print("--- MAC: "+str(mac2eui(get_eui())))
   print("> uPy version: "+str(os.uname()[3]))
   #print("> octopus() ver: " + ver)

   print("[device]")
   try:
        with open('config/device.json', 'r') as f:
            d = f.read()
            f.close()
            print(" > config/device: " + d)
            # device_config = json.loads(d)
   except:
        print("Device config 'config/device.json' does not exist, please run setup()")
   
   print("[wifi]")
   try:
        with open('config/wifi.json', 'r') as f:
            d = f.read()
            f.close()
            print(" > config/wifi: " + d)          
   except:
        print("'config/wifi.json' does not exist")
   
   print("[mqtt]")
   try:
        with open('config/mqtt.json', 'r') as f:
            d = f.read()
            f.close()
            print(" > config/mqtt: " + d)
   except:
        print("'config/mqtt.json' does not exist")

   print("[mqtt_io]")
   try:
        with open('config/mqtt_io.json', 'r') as f:
            d = f.read()
            f.close()
            print(" > config/mqtt_io: " + d)
   except:
        print("'config/mqtt_io.json' does not exist")     

   print()

   gc.collect()
   print("> mem_free: "+str(gc.mem_free()))
   print("> flash: "+str(os.statvfs("/")))
   print("> flash free: "+str(int(os.statvfs("/")[0])*int(os.statvfs("/")[3])))
   print("> machine.freq: "+str(machine.freq()))
   print("> active variables:")
   print(dir())
   print("> datetime RAW: "+str(rtc.datetime()))

   wait = input(" >> Press ENTER to continue")
   

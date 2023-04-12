from machine import Pin
import time

led = Pin(25, Pin.OUT)

led.on()

time.sleep(.25)
led.off()
time.sleep(.25)
led.on()
time.sleep(.25)
led.off()
time.sleep( .25)
led.on()
print('This is Raspberry PICO')




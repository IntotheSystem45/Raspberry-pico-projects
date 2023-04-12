import time #needed for led to blink
from machine import Pin #needed for (GPIO)Pin interaction

led=Pin(13, Pin.OUT)

var = int(input("Type in 1 or 2 or 3 "))
x = True
if(var == 1): #Normal speed
    while(x): #Allows the led to flash on and off repeatably 
        led.value(1)
        time.sleep(.5)
        led.value(0)
        time.sleep(.5)
elif(var == 2): # Faster speed
      while(x):
        led.value(1)
        time.sleep(.3)
        led.value(0)
        time.sleep(.3)
elif(var == 3): # Fastest2 speed
      while(x):
        led.value(1)
        time.sleep(.1)
        led.value(0)
        time.sleep(.1)
elif(var != 1 or 2 or 3): # Response is none of the above
      print("invalid response")
      led.value(0)
        
        


    
  



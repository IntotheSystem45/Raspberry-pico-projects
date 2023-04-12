import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


# Clear screen with BLACK color and pen
display.set_pen(BLACK)
display.clear()

display.set_pen(GREEN)
#display.text("Hello", 100, 70, scale = 6)
display.circle(20, 20, 20)
display.update()



for i in range (0, 20):
    time.sleep(.1)
    x = i*10 + 20
    y = 20
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(GREEN)
    display.circle(x, y, 20)
    display.update()
    
for i in range (0, 20):
    time.sleep(.1)
    x = 210
    y = i*5 + 20
    print(y)
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(GREEN)
    display.circle(x, y, 20)
    display.update()

for i in range (0, 20):
    time.sleep(.1)
    x = 210 - i*10
    y = 115
    print(x)
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(GREEN)
    display.circle(x, y, 20)
    display.update()
    
for i in range (0, 20):
    time.sleep(.1)
    x = 20
    y = 115 - i*5
    print(x)
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(GREEN)
    display.circle(x, y, 20)
    display.update()

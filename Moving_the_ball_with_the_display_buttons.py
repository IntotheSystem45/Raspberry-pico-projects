# This is an example for how you can use the buttons on a PICO display to move a ball around.
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8") # Allows the use of the screen on the PICO display

# the variable are set equal to how the PICO understands the buttons
button_a = Button(12) 
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# Allows the PICO to recognize the colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


# sets up a function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


# set up
clear()
# The following displays the circle on the top left corner.
display.circle(20, 20, 20)  
display.update()
x = 20
y = 20
condition = True
while (condition):
    if button_a.read():                                 # if a button press is detected then...
        x = x - 20                                    # ball moves to the left 
        display.set_pen(WHITE)                         # change the pen colour 
        display.update()                                # update the display to the new position of the circle 
        time.sleep(.1)                                  # pause for a sec
        clear()                                         # clears the last circle and only the updated position remains
    elif button_b.read():
        y = y + 20
        display.set_pen(WHITE)
        display.update()
        time.sleep(.1)
        clear()
    elif button_x.read():
        x = x + 20
        display.set_pen(WHITE)                     
        display.update()                         
        time.sleep(.1)                                 
        clear() 
    elif button_y.read():
        y = y - 20
        display.set_pen(WHITE)
        display.update()
        time.sleep(.1)
        clear()
    else:
        display.set_pen(WHITE)
        display.circle(x, y, 20)
        if (x > 240) or (x < 0) or (y < 0) or (y > 135):
            condition = False
        display.update()
        time.sleep(0.1)  # this number is how frequently the Pico checks for button presses

clear()
display.set_pen(YELLOW)
display.text("You went out of bounds", 10, 10, 240, 4)
display.update()
time.sleep(1)
clear()

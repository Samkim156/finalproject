
from graphics import Window
from graphics import Rectangle, Circle, Textbox


window = Window(width=300, 
                height=400, 
                title="TELEGRAFF")                        
lightbulb = Circle(diameter=200, 
                   fill_color="darkgray", 
                   outline_color="black")
button = Rectangle(width=150, height=50,
                   fill_color="gray", 
                   outline_color="black")
window.paste(lightbulb, 50, 30) 
window.paste(button, 75, 300)

quit_now = False
while not quit_now:
    quit_now = window.refresh()
telegraff.py
Displaying telegraff.py.

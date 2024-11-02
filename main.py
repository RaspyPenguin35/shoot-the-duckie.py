import pgzrun
import random
WIDTH=500
HEIGHT=500
TITLE="SHOOT THE DUCKIE GAMESHOW"
message=""
duckie=Actor("alien")
duckie.pos=50,50
def draw():
    screen.clear()
    screen.fill(color=(0,0,0))
    duckie.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
def place_duckie():
    duckie.x=random.randint(50,WIDTH-50)
    duckie.y=random.randint(50,WIDTH-50)
def on_mouse_down(pos):
    global message
    if duckie.collidepoint(pos):
        message="Good Shot!"
        place_duckie()
    else:
        message="You Missed!"
place_duckie()
pgzrun.go()

import pgzrun
import random
WIDTH=500
HEIGHT=500
TITLE="SHOOT THE DUCKIE GAMESHOW"
message=""
duckie=Actor("shoottheduckie")
duckie.pos=50,50
def draw():
    screen.clear()
    screen.fill(color=(0,0,0))
    duckie.draw()

pgzrun.go()
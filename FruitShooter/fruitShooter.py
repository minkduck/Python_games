import pgzrun
from random import randint
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
def draw():
    screen.clear()
    screen.fill("pink")
    apple.draw()
    orange.draw()
    pineapple.draw()
def place_apple():
    apple.x = randint(10,300)
    apple.y = randint(10,200)
def place_orange():
    orange.x = randint(50,400)
    orange.y = randint(60,600)
place_orange()
def place_pineapple():
    pineapple.x = randint(100,800)
    pineapple.y = randint(100,300)
place_pineapple()
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shoot")
        place_apple()
    elif orange.collidepoint(pos):
        print("Good shoot")
        place_orange()
    elif pineapple.collidepoint(pos):
        print("Good shoot")
        place_pineapple()
    else:
        print('Missed')
pgzrun.go()
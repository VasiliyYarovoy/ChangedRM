import turtle
import time

moveUp = False
moveDown = False
moveRight = False
moveLeft = False

COLIN_PATH = "Characters\\Colin\\"
COLIN_IDLE_UP = COLIN_PATH + "Colin-up.gif"
COLIN_UP_01 = COLIN_PATH + "Colin-up-01.gif"
COLIN_UP_02 = COLIN_PATH + "Colin-up-02.gif"
COLIN_IDLE_DOWN = COLIN_PATH + "Colin-down.gif"
COLIN_DOWN_01 = COLIN_PATH + "Colin-down-01.gif"
COLIN_DOWN_02 = COLIN_PATH + "Colin-down-02.gif"
COLIN_IDLE_RIGHT = COLIN_PATH + "Colin-Right.gif"
COLIN_RIGHT_01 = COLIN_PATH + "Colin-Right-01.gif"
COLIN_RIGHT_02 = COLIN_PATH + "Colin-Right-02.gif"
COLIN_IDLE_lEFT = COLIN_PATH + "Colin-left.gif"
COLIN_LEFT_01 = COLIN_PATH + "Colin-left-01.gif"
COLIN_LEFT_02 = COLIN_PATH + "Colin-left-02.gif"


turtle.addshape(COLIN_IDLE_UP)
turtle.addshape(COLIN_UP_01)
turtle.addshape(COLIN_UP_02)
turtle.addshape(COLIN_IDLE_DOWN)
turtle.addshape(COLIN_DOWN_01)
turtle.addshape(COLIN_DOWN_02)
turtle.addshape(COLIN_IDLE_RIGHT)
turtle.addshape(COLIN_RIGHT_01)
turtle.addshape(COLIN_RIGHT_02)
turtle.addshape(COLIN_IDLE_lEFT)
turtle.addshape(COLIN_LEFT_01)
turtle.addshape(COLIN_LEFT_02)

char = turtle.Turtle()
turtle.delay(0)
step = 30
charX = 0
charY = 0
camX = 0
camY = 0
char.shape(COLIN_IDLE_DOWN)
char.penup()

def Update():
    global charX
    global charY
    global moveUp
    global moveDown
    global moveRight
    global moveLeft
    if moveUp:
        while moveUp:
            if charY > 240:
                for i in range(2):
                    for i in range(2):
                        char.shape()
                        char.shape(COLIN_UP_01)
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_UP_02)
                        char.goto(charX, charY)
                        time.sleep(0.05)
            else:
                 for i in range(2):
                    for i in range(2):
                        char.shape(COLIN_UP_01)
                        charY += step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_UP_02)
                        charY += step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
        char.shape(COLIN_IDLE_UP)
    if moveDown:
        while moveDown:
            if charY < -240:
                for i in range(2):
                    for i in range(2):
                        char.shape(COLIN_DOWN_01)
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_DOWN_02)
                        char.goto(charX, charY)
                        time.sleep(0.05)
            else:
                for i in range(2):
                    for i in range(2):
                        char.shape(COLIN_DOWN_01)
                        charY -= step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_DOWN_02)
                        charY -= step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
        char.shape(COLIN_IDLE_DOWN)
    if moveRight:
        while moveRight:
            for i in range(2):
                if charX > 240:
                    for i in range(2):
                        char.shape(COLIN_RIGHT_01)
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_RIGHT_02)
                        char.goto(charX, charY)
                        time.sleep(0.05)
                else:
                    for i in range(2):
                        char.shape(COLIN_RIGHT_01)
                        charX += step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_RIGHT_02)
                        charX += step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
        char.shape(COLIN_IDLE_RIGHT)
    if moveLeft:
        while moveLeft:
            if charX < -240:
                for i in range(2):
                    for i in range(2):
                        char.shape(COLIN_LEFT_01)
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_LEFT_02)
                        char.goto(charX, charY)
                        time.sleep(0.05)
            else:
                for i in range(2):
                    for i in range(2):
                        char.shape(COLIN_LEFT_01)
                        charX -= step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
                    for i in range(2):
                        char.shape(COLIN_LEFT_02)
                        charX -= step/5
                        char.goto(charX, charY)
                        time.sleep(0.05)
        char.shape(COLIN_IDLE_lEFT)
    char.clearstamps()

def goUp():
    global moveUp
    moveUp = True
def goDown():
    global moveDown
    moveDown = True
def goRight():
    global moveRight
    moveRight = True
def goLeft():
    global moveLeft
    moveLeft = True
    moveUp = False
def stopUp():
    global moveUp
    moveUp = False
def stopDown():
    global moveDown
    moveDown = False
def stopRight():
    global moveRight
    moveRight = False
def stopLeft():
    global moveLeft
    moveLeft = False

def moveCam(x, y, sec):
    global charX
    global charY
    for i in range(sec):
        charX -= x/sec
        charY -= y/sec

turtle.onkeypress(goUp, "Up")
turtle.onkeypress(goDown, "Down")
turtle.onkeypress(goLeft, "Left")
turtle.onkeypress(goRight, "Right")

turtle.onkeyrelease(stopUp, "Up")
turtle.onkeyrelease(stopDown, "Down")
turtle.onkeyrelease(stopLeft, "Left")
turtle.onkeyrelease(stopRight, "Right")

turtle.listen()

while True:
    Update()

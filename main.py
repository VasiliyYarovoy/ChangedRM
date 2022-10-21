import turtle
import time

moveUp = False
moveDown = False
moveRight = False
moveLeft = False

turtle.addshape("ProgramFiles\\Character\\Colin\\Up\\Colin-up.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Up\\Colin-up-01.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Up\\Colin-up-02.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down-01.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down-02.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right-01.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right-02.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Left\\Colin-Left.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Left\\Colin-left-01.gif")
turtle.addshape("ProgramFiles\\Character\\Colin\\Left\\Colin-left-02.gif")

char = turtle.Turtle()
turtle.delay(0)
step = 30
charX = 0
charY = 0
camX = 0
camY = 0
char.shape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down.gif")
char.penup()


def Update():
    global charX
    global charY
    global moveUp
    global moveDown
    global moveRight
    global moveLeft
    if moveUp:
        for i in range(2):
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Up\\Colin-up-01.gif")
                charY += step/5
                char.goto(charX, charY)
                time.sleep(0.06)
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Up\\Colin-up-02.gif")
                charY += step/5
                char.goto(charX, charY)
                time.sleep(0.06)
            char.shape("ProgramFiles\\Character\\Colin\\Up\\Colin-up.gif")
    if moveDown:
        for i in range(2):
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down-01.gif")
                charY -= step/5
                char.goto(charX, charY)
                time.sleep(0.06)
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down-02.gif")
                charY -= step/5
                char.goto(charX, charY)
                time.sleep(0.06)
            char.shape("ProgramFiles\\Character\\Colin\\Down\\Colin-Down.gif")
    if moveRight:
        for i in range(2):
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right-01.gif")
                charX += step/5
                char.goto(charX, charY)
                time.sleep(0.06)
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right-02.gif")
                charX += step/5
                char.goto(charX, charY)
                time.sleep(0.05)
        char.shape("ProgramFiles\\Character\\Colin\\Right\\Colin-Right.gif")
    if moveLeft:
        for i in range(2):
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Left\\Colin-left-01.gif")
                charX -= step/5
                char.goto(charX, charY)
                time.sleep(0.05)
            for i in range(2):
                char.shape("ProgramFiles\\Character\\Colin\\Left\\Colin-left-02.gif")
                charX -= step/5
                char.goto(charX, charY)
                time.sleep(0.05)
        char.shape("ProgramFiles\\Character\\Colin\\Left\\Colin-Left.gif")
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

def MoveCam(x, y):
    global charX
    global charY
    charX += x
    charY += y

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

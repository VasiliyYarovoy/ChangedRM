import turtle
import time

char = turtle.Turtle()
turtle.delay(0)
step = 30
charX = 0
charY = 0
camX = 0
camY = 0
char.shape("square")
char.penup()

moveUp = False
moveDown = False
moveRight = False
moveLeft = False

def Update():
    global charX
    global charY
    global moveUp
    global moveDown
    global moveRight
    global moveLeft
    if moveUp:
        for i in range(5):
            char.shape("circle")
            charY += step/5
            char.goto(charX, charY)
            time.sleep(0.05)
        if moveUp:
            for i in range(5):
                char.shape("triangle")
                charY += step/5
                char.goto(charX, charY)
                time.sleep(0.05)
    if moveDown:
        for i in range(5):
            char.shape("circle")
            charY -= step/5
            char.goto(charX, charY)
            time.sleep(0.05)
        if moveDown:
            for i in range(5):
                char.shape("triangle")
                charY -= step/5
                char.goto(charX, charY)
                time.sleep(0.05)
    if moveRight:
        for i in range(5):
            char.shape("circle")
            charX += step/5
            char.goto(charX, charY)
            time.sleep(0.05)
        if moveRight:
            for i in range(5):
                char.shape("triangle")
                charX += step/5
                char.goto(charX, charY)
                time.sleep(0.05)
    if moveLeft:
        for i in range(5):
            char.shape("circle")
            charX -= step/5
            char.goto(charX, charY)
            time.sleep(0.05)
        if moveLeft:
            for i in range(5):
                char.shape("triangle")
                charX -= step/5
                char.goto(charX, charY)
                time.sleep(0.05)
    char.shape("square")

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
def StopUp():
    global moveUp
def StopDown():
    global moveDown
    moveDown - False
def StopRight():
    global moveRight
    moveRight = False
def StopLeft():
    global moveLeft
    moveLeft = False

def MoveCam(x, y):
    global charX
    global charY
    charX += x
    charY += y

goLeft()

MoveCam(100, 100)

while True:
    Update()
    print(charX)
    print(charY)

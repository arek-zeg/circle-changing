from graphics import *
from time import sleep
from random import randint




winMain = GraphWin(title = 'Circle changing color/size', height=400, width=400)
winMain.setBackground('black')
textMessage = Text(Point(winMain.getWidth()/2, winMain.getHeight() - 20), 'Click anywhere to close')
textMessage.setTextColor('white')
textMessage.draw(winMain)

while True:
    circle = Circle( Point(winMain.getWidth()/2, winMain.getHeight()/2), randint(1, (winMain.getHeight()/2) - 20))
    circle.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    circle.draw(winMain)
    if winMain.checkMouse() != None:
        break
    sleep(0.05)
    circle.undraw()


winMain.close()

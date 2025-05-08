from koch import Koch
import turtle


class Sneeuwvlok:
    def __init__(self, startx, starty):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(10)
        self.pen.goto(startx, starty)
        self.pen.pendown()

    def teken(self, orde, grootte):
        for i in range(3):
            zijde = Koch(self.pen)
            zijde.teken(orde, grootte)
            self.pen.right(120)
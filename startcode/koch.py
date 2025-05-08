class Koch:
    def __init__(self, pen):
        self.pen = pen

    def teken(self, orde, lengte):
        if orde == 0:
            self.pen.forward(lengte)
            self.pen.ht()
        else:
            volgende_lengte = lengte / 3
            volgende_orde = orde - 1
            self.teken(volgende_orde, volgende_lengte)
            self.pen.left(60)
            self.teken(volgende_orde, volgende_lengte)
            self.pen.right(120)
            self.teken(volgende_orde, volgende_lengte)
            self.pen.left(60)
            self.teken(volgende_orde, volgende_lengte)
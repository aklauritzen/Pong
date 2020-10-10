from turtle import *


class GameElement(Turtle):
    def __init__(self, gotox, gotoy, shape_size_wid=1, shape_size_len=1, spd=0, col="white", shap="square",
                 hide_turtle=False):
        # Inherits all methods and properties from Turle()
        super().__init__()

        # Sets speed for maximum speed
        self.speed(spd)

        self.shape(shap)
        self.color(col)

        if shape_size_wid != 0 | shape_size_len != 0:
            self.shapesize(stretch_wid=shape_size_wid, stretch_len=shape_size_len)

        self.penup()
        self.goto(gotox, gotoy)

        if hide_turtle:
            self.hideturtle()

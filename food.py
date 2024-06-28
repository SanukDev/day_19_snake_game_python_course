from turtle import Turtle
from random import randint
# The Class tcheck if the snake touch in the food


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        position_x = randint(-280, 280)
        position_y = randint(-280, 280)
        self.goto(position_x, position_y)
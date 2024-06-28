from turtle import Turtle, Screen

DISTANCE_SNAKES = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
# The class create the object snake and initialize the snake


class Snake:
    def __init__(self):
        self.segment = []
        self.start_snake()
        self.screen = Screen()

    def start_snake(self):
        for position in DISTANCE_SNAKES:
            snake2 = Turtle(shape="square")
            snake2.color("white")
            snake2.penup()
            snake2.goto(position)
            self.segment.append(snake2)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_nex = self.segment[seg_num - 1].xcor()
            y_nex = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_nex, y_nex)
        self.segment[0].forward(20)

    def new_snake(self):
        snake2 = Turtle(shape="square")
        snake2.color("white")
        snake2.penup()
        self.segment.append(snake2)
        self.move()

    def move_right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def move_left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def move_back(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def move_forward(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def cont_snake(self):
        self.screen.listen()
        self.screen.onkey(key="Right", fun=self.move_right)
        self.screen.onkey(key="Left", fun=self.move_left)
        self.screen.onkey(key="Down", fun=self.move_back)
        self.screen.onkey(key="Up", fun=self.move_forward)

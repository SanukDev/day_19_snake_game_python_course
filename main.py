from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Configurate the Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

# Class I create
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# The recursion
stop_snake = True
while stop_snake:
    screen.update()
    time.sleep(0.1)

    snake.move()
    snake.cont_snake()

    # Detect collision with food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.new_snake()

    # Detect collision with wall
    if snake.segment[0].xcor() > 296 or snake.segment[0].xcor() < -296 or snake.segment[0].ycor() > 296 or snake.segment[0].ycor() < -296:
        stop_snake = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment_number in snake.segment[1:]:
        if snake.segment[0].distance(segment_number) < 10:
            stop_snake = False
            scoreboard.game_over()
# Out of image
screen.exitonclick()

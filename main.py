from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake(move_length=20, num_segs=5)
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()

    # Detect food consumption
    if snake.head.distance(food) < 15:
        food.position_food()
        snake.extend()
        scoreboard.increment_score()


    # Detect Collision with Wall or tail
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280 or snake.detect_self_collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

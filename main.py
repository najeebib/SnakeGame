import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
# initialize snake food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# listen to arrow keys click
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# update screen
screen.update()
game_is_on = True
while game_is_on:
    # move snake while game is on
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if the snake collided with food
    if snake.head.distance(food) < 15:
        # move food to new random location
        food.refresh()
        # update score
        scoreboard.increase_score()
        # extend the snake tail
        snake.extend()
    # detect if the snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # detect if the snake it's tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

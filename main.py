from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

GAME_OVER_WALL = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Screen de olan her şey sırayla olmasını sağlıyor. 0 Verdiğimiz zaman hepsi aynı anda olacak
is_game_finished = False


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while not is_game_finished:
    # Delay for 0.1 second and then refresh the screen.
    screen.update()
    time.sleep(0.05)
    # Every time the screen refreshes, move the snake automatically forwards.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_scoreboard()

    # Detect collision with wall.
    if snake.head.xcor() > GAME_OVER_WALL or snake.head.xcor() < -GAME_OVER_WALL or \
            snake.head.ycor() > GAME_OVER_WALL or snake.head.ycor() < -GAME_OVER_WALL:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Sliced the list. It now doesn't given the segment at the index[0]
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

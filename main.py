import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import ScoreBoard


def end_game():
    global game_is_on
    game_is_on = False


scr = Screen()
snake = Snake()
food = Food()
score_count = ScoreBoard()
scr.setup(width=600, height=630)
scr.bgpic("pixil-frame-0.gif")
scr.title("SlitherIt")
scr.tracer(0)
scr.listen()

# Keys mapping
scr.onkey(snake.up, "w")
scr.onkey(snake.down, "s")
scr.onkey(snake.left, "a")
scr.onkey(snake.right, "d")
scr.onkey(end_game, "Escape")
game_is_on = True

# # Checking food position
# check = Turtle("circle")
# check.penup()
# check.color("white")
# check.shapesize(0.5, 0.5)
# check.goto(0, 280)

while game_is_on:
    scr.update()
    time.sleep(0.15)
    snake.move_snake()

    # Detecting collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_count.increase_score()

    # Detect collision with wall
    if (snake.snake_head.xcor() > 260 or snake.snake_head.xcor() < -260 or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280):
        score_count.reset_score()
        snake.reset_snake()
        time.sleep(2)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scr.update()
            score_count.reset_score()
            snake.reset_snake()
            time.sleep(2)

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# segment = []
#
# for x in starting_position:
#     tim = Turtle("square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(x)
#     segment.append(tim)
snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        snake.extend()
        score.increase_score()


# detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

# detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


    # for x in range(len(segment) - 1, 0, -1):
    #     nex_x = segment[x - 1].xcor()
    #     new_y = segment[x - 1].ycor()
    #     segment[x].goto(nex_x, new_y)
    # segment[0].forward(20)
    # segment[0].left(90)

screen.exitonclick()

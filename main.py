from turtle import Screen
from Food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


newsnake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(newsnake.up,'Up')
screen.onkey(newsnake.down,'Down')
screen.onkey(newsnake.left,'Left')
screen.onkey(newsnake.right,'Right')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    newsnake.move()

    # collision with food with turtle.distance method
    if newsnake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        newsnake.increase_length()

    # detect collision with wall
    if newsnake.head.xcor() > 290 or newsnake.head.xcor() <-290 or newsnake.head.ycor()> 290 or newsnake.head.ycor()<-290:
        game_on = False
        score.game_over()
    # detect collision with tail
    for seg in newsnake.segments[1::]:

        if  newsnake.head.distance(seg) <10:
            game_on=False
            score.game_over()

screen.exitonclick()
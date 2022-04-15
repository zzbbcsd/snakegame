from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()


    def update(self):
        self.write(f"Score = {self.score} ", False, align="center", font = ('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False,align="center", font = ('Courier', 24, 'normal'))



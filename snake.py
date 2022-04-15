from turtle import Turtle
starting_position = [(0,0),(-20,0),(-40,0)]
moving_distance = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in starting_position:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(moving_distance)

    def up(self):
        if self.head.heading()!= 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def increase_length(self):
        new = Turtle("square")
        new.color("white")
        new.penup()
        neweat_x = self.segments[len(self.segments) - 1].xcor()+20
        neweat_y = self.segments[len(self.segments) - 1].ycor()+20
        new.goto(neweat_x,neweat_y)
        self.segments.append(new)
        self.move()
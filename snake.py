from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.head.color("red")

    def create_snake(self):
        for x in STARTING_POSITION:
            self.add_segment(x)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for x in self.segment:
            x.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        self.head.color("red")

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        segment = self.segment
        for x in range(len(segment) - 1, 0, -1):
            nex_x = segment[x - 1].xcor()
            new_y = segment[x - 1].ycor()
            segment[x].goto(nex_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

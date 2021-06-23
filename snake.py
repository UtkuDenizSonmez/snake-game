from turtle import Turtle
SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    """Constructor method."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creating the snake and giving it the positions"""
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Snake's last piece's coordinates = last -1 piece coordinates."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)







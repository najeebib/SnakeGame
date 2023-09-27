from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # this will have all the turtles
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # add new segment to tail
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    # extend the tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # move the snake to forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # change the snake direction up when up arrow clicked
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # change the snake direction down when up arrow down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # change the snake direction left when left arrow clicked
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # change the snake direction right when right arrow clicked
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

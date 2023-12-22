from turtle import Turtle
STARTING_POSITION = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
        self.snake_appearance()
        self.last_direction = self.snake_head.heading()

    def create_snake(self):
        """Create snake in middle of the window"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def snake_appearance(self):
        """Set color and shape of the snake"""
        self.snake_head.color("green")
        self.snake_head.shape("square")
        for segment in self.segments[2::2]:
            segment.color("indianred")

    def extend(self):
        """Increase the size of the snake"""
        self.add_segment(self.segments[-1].position())
        self.snake_appearance()

    def add_segment(self, position):
        """Add the segments to the snake"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def move_snake(self):
        for seg_in in range(len(self.segments) - 1, 0, -1):
            x_cords = self.segments[seg_in - 1].xcor()
            y_cords = self.segments[seg_in - 1].ycor()
            self.segments[seg_in].setposition(x=x_cords, y=y_cords)
        self.snake_head.forward(MOVE_DISTANCE)
        self.last_direction = self.snake_head.heading()

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]
        self.snake_appearance()

    def up(self):
        if self.snake_head.heading() != DOWN and self.last_direction != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP and self.last_direction != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT and self.last_direction != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT and self.last_direction != LEFT:
            self.snake_head.setheading(RIGHT)

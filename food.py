from turtle import Turtle
from random import randint


class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Set next food on new random position"""
        random_x = randint(-250, 250)
        random_y = randint(-270, 270)
        self.goto(random_x, random_y)

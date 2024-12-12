import random
from turtle import Turtle
from screen import WIDTH, HEIGHT


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.setRandomCoor()

    def setRandomCoor(self):
        return self.goto(random.randint(-1 * WIDTH//2, WIDTH//2), random.randint(-1 * HEIGHT//2, HEIGHT//2))

    def refresh(self):
        self.clear()
        self.setRandomCoor()
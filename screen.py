from turtle import Screen
from snake import Snake

WIDTH = 800
HEIGHT = 600

class MyScreen:

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.screen.setup(WIDTH, HEIGHT)


    def addListenersToSnake(self, snake: Snake):
        self.screen.listen()
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")
from time import sleep
from turtle import Screen
from snake import Snake

snake = Snake()
screen = Screen()


while True:
    snake.move()
    sleep(0.1)



screen.exitonclick()
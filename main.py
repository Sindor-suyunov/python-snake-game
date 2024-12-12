from screen import MyScreen
from snake import Snake
import time

snake = Snake()
screen = MyScreen()
screen.addListenersToSnake(snake)

game_over = False

while not game_over:
    screen.screen.update()
    time.sleep(0.1)
    snake.move()


screen.screen.exitonclick()




from food import Food
from screen import MyScreen
from snake import Snake, DISTANCE
import time

snake = Snake()
screen = MyScreen()
food = Food()
screen.addListenersToSnake(snake)

game_over = False

while not game_over:
    # moving snake
    screen.screen.update()
    time.sleep(0.1)
    snake.move()

    # eat the food
    if snake.head.distance(food.xcor(), food.ycor()) < DISTANCE:
        snake.eat()
        food.refresh()


screen.screen.exitonclick()




from turtle import Turtle
import screen

DISTANCE = 10
MOVE_DISTANCE = 20
BEGIN_ITEMS_COORDS = ((0,0), (-20,0), (-40,0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.score = 0
        self.items = []
        for coor in BEGIN_ITEMS_COORDS:
            self.createItem(coor)
        self.head = self.items[0]
        self.head.color("red")

    def createItem(self, position):
        item = Turtle()
        item.penup()
        item.goto(position)
        item.color('white')
        item.shape('circle')
        self.items.append(item)

    def move(self):
        for item in range(len(self.items) - 1, 0, -1):
            new_x = self.items[item - 1].xcor()
            new_y = self.items[item - 1].ycor()
            self.items[item].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    def eat(self):
        self.score += 1
        self.createItem(self.items[-1].position())

    def isNearToWall(self)->bool :
        xCor = int(self.head.xcor())
        yCor = int(self.head.ycor())

        WIDTH = screen.WIDTH // 2
        HEIGHT = screen.HEIGHT // 2

        return xCor + DISTANCE > WIDTH or xCor - DISTANCE < -1 * WIDTH or yCor + DISTANCE > HEIGHT or yCor - DISTANCE < -1 * HEIGHT

    def isNearToTail(self):
        for index in range(1, len(self.items)):
            if self.head.distance(self.items[index].position()) < DISTANCE:
                return True
        return False

    def showGameOver(self):
        score = Turtle()
        score.color("white")
        score.hideturtle()
        score.write(f"GAME OVER.(your score: {self.score})", align="center", font=("Courier", 24, "normal"))
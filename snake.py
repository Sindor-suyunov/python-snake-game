from turtle import Turtle

DISTANCE = 20
BEGIN_ITEMS_COORDS = ((0,0), (-20,0), (-40,0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.items = []
        for coor in BEGIN_ITEMS_COORDS:
            self.createItem(coor[0], coor[1])
        self.head = self.items[0]

    def createItem(self, x: int, y: int):
        item = Turtle()
        item.penup()
        item.goto(x, y)
        item.color('white')
        item.shape('square')
        self.items.append(item)

    def move(self):
        for item in range(len(self.items) - 1, 0, -1):
            new_x = self.items[item - 1].xcor()
            new_y = self.items[item - 1].ycor()
            self.items[item].goto(new_x, new_y)
        self.head.forward(DISTANCE)

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
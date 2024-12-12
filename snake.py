from turtle import Turtle

DISTANCE = 20
BEGIN_ITEMS_COORDS = ((0,0), (-20,0), (-40,0))

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
        item.color('red')
        item.shape('')
        self.items.append(item)

    def move(self):
        for item in self.items:
            item.forward(DISTANCE)
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

#create paddle class
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.setheading(UP)
        self.shapesize(stretch_len=5, stretch_wid=1)


    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)
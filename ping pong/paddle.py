from turtle import  Turtle

class paddle(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(postion)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
              self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
              self.goto(self.xcor(), new_y)
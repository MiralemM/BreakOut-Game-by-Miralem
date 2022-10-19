from turtle import Turtle

colors = ["yellow", "green", "orange", "red"]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(x=x_cor, y=y_cor)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_lanes()

    def create_lane(self, y_cor):
        for i in range(-570, 570, 87):
            brick = Brick(i, y_cor)
            if y_cor < 50:
                brick.color(colors[0])
            elif y_cor > 50 and y_cor < 100:
                brick.color(colors[1])
            elif y_cor > 100 and y_cor < 180:
                brick.color(colors[2])
            elif y_cor > 180:
                brick.color(colors[3])

            self.bricks.append(brick)

    def create_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)

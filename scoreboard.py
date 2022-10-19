from turtle import Turtle

FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.lives = 3
        self.game_over = "GAME OVER"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-420, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(380, 250)
        self.write(f"High Score: {self.high_score}", align="center", font=FONT)
        self.goto(0, 250)
        self.write(f"Lives: {self.lives}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def points_3(self):
        self.score += 3
        self.update_scoreboard()

    def points_5(self):
        self.score += 5
        self.update_scoreboard()

    def points_7(self):
        self.score += 7
        self.update_scoreboard()

    def evaluate_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.update_scoreboard()

    def end_game(self):
        self.lives -= 1
        self.update_scoreboard()

    def gm_ovr(self):
        self.goto(0, 0)
        self.write(self.game_over, align="center", font=("Ariel", 70, "bold"))

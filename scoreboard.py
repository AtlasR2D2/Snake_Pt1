from turtle import Turtle

FONT = {"Arial", 12, "Bold"}
ALIGNMENT = "Center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.score = 0
        self.show_score()

    def increment_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)


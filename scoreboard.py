from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # initialize the score and put it on the top
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    # update the scoreboard
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # write game over in the middle
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    # increment the score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 16, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("blue")
        self.ht()
        self.penup()
        self.show_score()

    def show_score(self):
        self.goto(0, 270)
        self.clear()
        self.write("Score: " + str(self.score) + "; High Score: " + str(self.high_score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
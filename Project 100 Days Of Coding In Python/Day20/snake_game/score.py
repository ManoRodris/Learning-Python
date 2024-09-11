from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("blue")
        self.ht()
        self.penup()
        self.show_score()

    def show_score(self):
        self.goto(0, 260)
        self.write("Score: " + str(self.score), align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score_p1 = 0
        self.score_p2 = 0
        self.show_scoreboard()

    def show_scoreboard(self):
        self.goto(100, 180)
        self.write(self.score_p1, True, "center", ("Courier", 80, "normal"))
        self.goto(-100, 180)
        self.write(self.score_p2, True, "center", ("Courier", 80, "normal"))

    def increase_score(self, player_one_scored):
        if player_one_scored:
            self.score_p1 += 1
            self.clear()
            self.show_scoreboard()
        else:
            self.score_p2 += 1
            self.clear()
            self.show_scoreboard()

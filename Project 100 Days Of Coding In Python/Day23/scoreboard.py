from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.score = 1
        self.show_level()

    def show_level(self):
        self.goto(-210, 250)
        self.write("Level: " + str(self.score), align="center", font=FONT)

    def increase_level(self):
        self.score += 1
        self.clear()
        self.show_level()

    def show_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

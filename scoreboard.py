from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.pu()
        self.ht()
        self.setposition(0, 260)
        self.write(f"Your Score: {self.current_score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Your Score: {self.current_score} ", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.color("red")
        self.write(f"Game Over\nYour Final Score: {self.current_score} ", align="center", font=("Arial", 24, "normal"))

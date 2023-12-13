from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.pu()
        self.ht()
        self.setposition(0, 260)
        self.write(f"Your Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Your Score: {self.score}  High Score: {self.highest_score}",
                   align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open("data.txt", "w") as data:
            data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

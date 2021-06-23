from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.setposition(-20, 260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.increase_scoreboard()

    def increase_scoreboard(self):
        self.score += 1
        self.write_score()

    """
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", True, align=ALIGNMENT, font=FONT)
    """


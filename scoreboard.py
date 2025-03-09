from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 40, "bold")
DOWN = 270

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.setheading(DOWN)
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.write_scoreboard()
        self.separator()

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1

    def write_scoreboard(self):
        self.goto(-50, 240)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(50, 240)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def separator(self):
        self.goto(0, 300)
        for _ in range(25):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def print_winner(self, message):
        self.clear()
        self.write_scoreboard()
        self.goto(0,0)
        self.write(message, align=ALIGN, font=FONT)

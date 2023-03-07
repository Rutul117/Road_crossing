from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-200,250)
        self.update_score_board()
        
    def update_score_board(self):
        self.setposition(-260, 260)
        self.write(f"Level: {self.level}",font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_score_board()
        
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER 😜",align="center" , font=FONT)
        self.setposition(30,260)
        self.write(f"Highest Score : {self.level}", font=FONT)

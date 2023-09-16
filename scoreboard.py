from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count_s = 0
        self.color('white')
        self.penup()
        self.setposition(0, 260)
        self.hideturtle()
        self.update_scoreboard()        

    def update_scoreboard(self):
        self.write(f"score: {self.count_s}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)


    def count_score(self):
        self.count_s += 1
        self.clear()
        self.update_scoreboard()  
        


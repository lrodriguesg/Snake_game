from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open('data.txt') as file:
            self.hight_score = int(file.read())

        self.color('white')
        self.penup()
        self.setposition(0, 260)
        self.hideturtle()
        self.update_scoreboard()        

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} | Hight Score: {self.hight_score}", align=ALIGNMENT, font=FONT)


    def reset (self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open('data.txt', mode='w') as file_w:
                file_w.write(str(self.hight_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)


    def count_score(self):
        self.score += 1
        self.update_scoreboard()  
        


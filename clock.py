from tkinter import *

class Clock:
    def __init__(self):
        self.screen = Tk()
        self.screen.title("Time is running out!")
        self.screen.geometry("350x150+785+465")
        self.screen.configure(bg = "black")
        self.screen.resizable(False, False)
        self.timeRemaining = 30
        
        self.timeLabel = Label(self.screen, bg = "black", fg = "white", text="30", font = ("Comic Sans", 12, "bold"))
        self.timeLabel.place(x = 15, y = 0, width = 20, height = 150) #5/8 of the whole size
        self.secondsLabel = Label(self.screen, bg = "black",fg = "white", text="seconds remaining", font = ("Comic Sans", 12, "bold")).place(x = 35, y = 0, width = 250, height = 150)
        

        self.timeLabel.after(1000, self.updateTime)

        

    def updateTime(self):
        self.timeRemaining -= 1

        if self.timeRemaining >= 0:
            self.timeLabel.configure(text=(self.timeRemaining))
            self.timeLabel.after(1000, self.updateTime)

        else:
            self.timeLabel = Label(self.screen, bg = "black", fg = "white", text="Time Up", font = ("Comic Sans", 12, "bold"))
            self.timeLabel.place(x = 15, y = 0, width = 270, height = 150) #5/8 of the whole size

    def destroyScreen(self):
        self.screen.destroy()


if __name__ == "__main__":
    clock = Clock()
    

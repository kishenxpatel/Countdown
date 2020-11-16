from tkinter import *
import random
import letters as Letters
import numbers as Numbers

class MainScreen():
    
    def __init__(self, score):
        self.score = score
        self.main_screen = Tk()
        self.main_screen.title("Select an option!")
        self.main_screen.geometry("1920x1080")
        self.main_screen.configure(bg = "aqua")
        self.main_screen.resizable(False, False)


        Label(self.main_screen, bg = "white", fg = "red",
                                           text= "Score: ", font = ("Comic Sans", 12, "bold")).place(x = 845, y = 20, width = 180, height = 150) #5/8 of the whole size
        Label(self.main_screen, bg = "white", fg = "red",
                                           text= self.score, font = ("Comic Sans", 12, "bold")).place(x = 1025, y = 20, width = 50, height = 150) #5/8 of the whole size

        
        self.displayChoices()

        self.main_screen.mainloop()
    

    def displayChoices(self):
        self.letters_button = Button(self.main_screen, text = "Letters Round", command = lambda: self.runLettersGame(),
                                bg = "grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 200, y = 290, width = 400, height = 500)

        Button(self.main_screen, text = "End Game",command = lambda: self.endGame(), relief = SUNKEN,
                                bg = "grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 860, y = 650, width = 200, height = 100)

        
        self.rules_button = Button(self.main_screen, text = "Rules", command = lambda: self.runRules(), 
                                bg = "grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 760, y = 440, width = 400, height = 200)
        
        self.numbers_button = Button(self.main_screen, text = "Numbers Round",command = lambda: [self.main_screen.destroy(), Numbers.NumbersGame(self.score)], 
                                bg = "grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 1320, y = 290, width = 400, height = 500)



    def endGame(self):
        end_screen = Tk()
        end_screen.geometry("600x700+660+190")
        end_screen.configure(bg = "white")
        end_screen.resizable(False, False)
        title = "You currently have a score of: ", self.score
        end_screen.title(title)

        endGame = Button(end_screen, text = "Are you sure?",command = lambda: quit(),
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 10, y = 50, width = 580, height = 680)


        
    def runLettersGame(self):
        self.main_screen.destroy()
        Letters.LettersGame(self.score)

    
        




    def runRules(self):

        rules_screen = Tk()
        rules_screen.geometry("1050x700+435+190")
        rules_screen.configure(bg = "white")
        rules_screen.resizable(False, False)
        title = "You currently have a score of: ", self.score



        
        rulesText = """
LETTERS
The aim of the Letters round is to make the longest word using the letters in the given selection.
Pick whether you would like to choose your letter selection or have the computer randomly generate one
for you.
You should have a total of nine letters in the selection, and letters may be repeated.
You then have thirty seconds to think of a word that uses as many letters as possible. It must be an
English word, and no names or proper nouns are included.
If you manage to think of a valid word, your score will be the length of the word. Invalid words, such
as those not included in the dictionary will give you zero points.

NUMBERS
In the Numbers round you are given six numbers and have to use arithmetic to reach a target
three-digit number.
Start by picking your numbers; you cannot pick more than four 'Large numbers'.
You will then have thirty seconds to try and reach the target number using any or all of the six numbers
just once by means of any combination of addition, subtraction, multiplication and division.
After the thirty seconds, you can input your answer. An exact calculation
match will give you five points, and if you are within five of the number, you get two points. One point
is scored if your answer is within ten of the required number.
No points are scored otherwise.



Good Luck! Get your brain working!


"""

        
        Label(rules_screen, text = rulesText,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 5, y = 10, width = 1040, height = 680)
        

if __name__ == "__main__":

    MainScreen(0)

















    

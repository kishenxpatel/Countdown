import random as rand
import tkinter
from tkinter import *
from tkinter import messagebox
import Clock as Clock
import main_screen as mainScreen
import time


class NumbersGame():

    def __init__(self, score):

        self.numbers_screen = Tk()
        self.numbers_screen.geometry("1920x1080")
        self.numbers_screen.configure(bg = "purple")
        self.numbers_screen.resizable(False, False)

        self.largeNumbers = 0
        self.smallNumbers = 0

        self.large = Button(self.numbers_screen, text = "Large Number",command = lambda: self.chooseLarge(),
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 100, y = 200, width = 1720, height = 300)
        
        self.small = Button(self.numbers_screen, text = "Small Number",command = lambda: self.chooseSmall(),
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 100, y = 580, width = 1720, height = 300)
        
        self.largeNum = [25 , 50 , 75 , 100]
        self.smallNum = [1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5 , 6 , 6 , 7 , 7 , 8 , 8 , 9 , 9 , 10 , 10]
        self.numberList= []
        self.score = score
        self.total = 0
    def chooseLarge(self):
        if len(self.numberList) <= 5:
            if len(self.largeNum) > 0:
                position = rand.randint(0, len(self.largeNum)-1)
                self.numberList.append(self.largeNum[position])
                self.largeNum.pop(position)
                self.largeNumbers += 1
                Label(self.numbers_screen, text = self.largeNumbers,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 1650, y = 200, width = 170, height = 300)

            else:
                Label(self.numbers_screen, text = "Maximum number of large numbers chosen",
                                    bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 100, y = 200, width = 1550, height = 300)
        else:
            self.unchangedNumberList = list(self.numberList)
            self.total = self.createNumber()
            self.displayNumbers()

    def chooseSmall(self):
        if len(self.numberList) <= 5:
            position = rand.randint(0, len(self.smallNum))
            self.numberList.append(self.smallNum[position])
            self.smallNum.pop(position)
            self.smallNumbers += 1
            Label(self.numbers_screen, text = self.smallNumbers,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 1650, y = 580, width = 170, height = 300)
        else:
            self.unchangedNumberList = list(self.numberList)
            self.total = self.createNumber()
            self.displayNumbers()


    def displayNumbers(self):

        screen = Tk()
        screen.geometry("900x125+510+50")
        screen.title("These are your numbers! You need to try and get as close as possible to the number on the very right!")
        screen.resizable(False, False)
        pos = 0
        for i in self.unchangedNumberList:
            Label(screen, text = i,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = pos*100, y = 0, width = 100, height = 125)
            pos += 1
        Label(screen, text = self.total,
                                bg = "white", foreground = "red", font = ("Comic Sans", 16, "bold")).place(x = 600, y = 0, width = 300, height = 125)

       
        clock = Clock.Clock() #display the clock


        self.numbers_screen.destroy()
        self.numbers_screen.after(30000, lambda: [self.timesUp(clock), screen.destroy()])
        

    
    def timesUp(self, clock):
        clock.destroyScreen()
        
        selected = Selection(self.unchangedNumberList, self.score, self.total)
        selected.displayNumbers()
        



    def createNumber(self):
        
        x = 0

        pos = rand.randint(0, len(self.numberList) - 1)
        self.total = self.numberList[pos]
        self.numberList.pop(pos)

        
        while x < 5:
            operator = rand.randint(0,3)
            position = rand.randint(0, len(self.numberList)-1)

            if operator == 0:
                self.total = self.total + self.numberList[position]
                self.numberList.pop(position)
                x += 1
                
            elif operator == 1:

                if self.total - self.numberList[position] > 0:
                    self.total = self.total - self.numberList[position]
                    self.numberList.pop(position)
                    x += 1 
                    
            elif operator == 2:
                self.total = self.total * self.numberList[position]
                self.numberList.pop(position)
                x += 1
                
            elif operator == 3:
                if type(self.total / self.numberList[position]) == int and (self.total / self.numberList[position] != 0):
                    self.total = self.total / self.numberList[position]
                    popped = self.numberList.pop(position)

                    x += 1

        return self.total



class Selection():

    def __init__(self, numberList, score, toMake):

        self.numberList = numberList
        self.score = score
        self.toMake = toMake
        self.total = 0
        self.temp = ""
        

    def displayNumbers(self):

        self.screen = Tk()
        self.screen.configure(bg = "light grey")
        self.screen.geometry("900x525+510+50")
        self.screen.resizable(False, False)

        
        
        Button(self.screen, text = self.numberList[0], command = lambda: self.addChosenNumber(0),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 0*100, y = 0, width = 100, height = 125)
        Button(self.screen, text = self.numberList[1], command = lambda: self.addChosenNumber(1),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 1*100, y = 0, width = 100, height = 125)
        Button(self.screen, text = self.numberList[2], command = lambda: self.addChosenNumber(2),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 2*100, y = 0, width = 100, height = 125)
        Button(self.screen, text = self.numberList[3], command = lambda: self.addChosenNumber(3),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 3*100, y = 0, width = 100, height = 125)
        Button(self.screen, text = self.numberList[4], command = lambda: self.addChosenNumber(4),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 4*100, y = 0, width = 100, height = 125)
        Button(self.screen, text = self.numberList[5], command = lambda: self.addChosenNumber(5),
                            bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 5*100, y = 0, width = 100, height = 125)
        Label(self.screen, text = self.toMake, bg = "white", foreground = "red", font = ("Comic Sans", 16, "bold")).place(x = 750, y = 0, width = 150, height = 125)
        Label(self.screen, text = " = ", bg = "white", foreground = "red", font = ("Comic Sans", 16, "bold")).place(x = 600, y = 0, width = 25, height = 125)
        Label(self.screen, text = self.total, bg = "white", foreground = "red", font = ("Comic Sans", 16, "bold")).place(x = 625, y = 0, width = 125, height = 125)



        Button(self.screen, text = "+", command = lambda: self.addChosenOperator("+"),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 16, "bold")).place(x = 0, y = 125, width = 225, height = 200)
        Button(self.screen, text = "-", command = lambda: self.addChosenOperator("-"),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 16, "bold")).place(x = 225, y = 125, width = 225, height = 200)
        Button(self.screen, text = "x", command = lambda: self.addChosenOperator("*"),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 16, "bold")).place(x = 450, y = 125, width = 225, height = 200)
        Button(self.screen, text = "/", command = lambda: self.addChosenOperator("/"),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 16, "bold")).place(x = 675, y = 125, width = 225, height = 200)



        Button(self.screen, text = "Undo", command = lambda: self.undo(),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 0, y = 325, width = 450, height = 200)
        Button(self.screen, text = "Confirm", command = lambda: self.confirmed(),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 450, y = 325, width = 450, height = 200)


    def undo(self):

        self.screen.destroy()
        self.total = 0
        self.temp = ""
        self.displayNumbers()

    def confirmed(self):

        difference = self.toMake - self.total
        if difference == 0:
            self.score += 5
        elif -5 < difference < 5:
            self.score += 2
        elif -10 < difference < 10:
            self.score += 1


        self.backToMain()

    def backToMain(self):
        self.screen.destroy()

        time.sleep(1)
        mainScreen.MainScreen(self.score)
        

    def addChosenNumber(self, i):
        operators = ["+", "-", "/", "*"]
        if len(self.temp) < 1:
            Label(self.screen, bg = "light grey").place(x = i*100, y = 0, width = 100, height = 125)
            self.temp += str(self.numberList[i])
        else:
            if self.temp[-1] in operators:
                Label(self.screen, bg = "light grey").place(x = i*100, y = 0, width = 100, height = 125)
                self.temp += str(self.numberList[i])
                self.performCalc()
                    

    def addChosenOperator(self, operator):

        if operator not in self.temp:
            if self.temp[-1].isnumeric():
                self.temp += operator

    def performCalc(self):

        
        self.total = eval(self.temp)
        self.temp = str(self.total)
        if self.total < 0 or type(self.total) != int:
            self.undo()
        else:
            Label(self.screen, text = self.total, bg = "white", foreground = "red", font = ("Comic Sans", 16, "bold")).place(x = 625, y = 0, width = 150, height = 125)

if __name__ == "__main__":
    NumbersGame(0)




from tkinter import *
import time
import Clock as Clock
from english_words import english_words_set
import random
import threading

import main_screen as mainScreen


class LettersGame():

    def __init__(self, score):
        self.letters_screen = Tk()
        self.letters_screen.geometry("1920x1080")
        self.letters_screen.configure(bg = "purple")
        self.randomButton = Button(self.letters_screen, text = "Select Letters",command = lambda: self.chooseSelected(), relief = SUNKEN,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 100, y = 200, width = 1720, height = 300)
        
        self.chooseButton = Button(self.letters_screen, text = "Randomly Selected Letters",command = lambda: self.randomSelected(), relief = SUNKEN,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 100, y = 580, width = 1720, height = 300)

        
        
        self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k",
                  "l", "m", "n", "p", "q", "r", "s", "t",
                  "v", "w", "x", "y", "z"]

        self.vowels = ["a", "e", "i", "o", "u"]

        self.score = score

        self.vowelCount = 0
        self.consonantCount = 0

        # total of nine letters; at least 3 self.vowels and 4 self.consonants
        self.letterList = []

        self.letters_screen.mainloop()

        
    def getVowel(self):
        index = random.randint(0, 4)
        letter = self.vowels[index]
        self.vowelCount += 1
        
        return letter


    def getConsonant(self):
        index = random.randint(0, 20)
        letter = self.consonants[index]
        self.consonantCount += 1
        
        return letter


    def getRandomLetter(self):
        choice = random.randint(0, 1)
        if choice == 0:
            return self.getVowel()
        else:
            return self.getConsonant()


    def selectLetters(self):

        select = Tk()
        select.geometry("600x700+660+190")
        consonantButton = Button(select, text = "Consonant",command = lambda: self.addToLetterList(select, "c"),
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 10, y = 50, width = 580, height = 275)
        
        vowelButton = Button(select, text = "Vowel",command = lambda: self.addToLetterList(select, "v"),
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 10, y = 375, width = 580, height = 275)

      
    def addToLetterList(self, screen, letterType):

        if letterType == "c":
            self.letterList.append(self.getConsonant())
            Label(screen, text = self.consonantCount,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 500, y = 50, width = 80, height = 275)
            
        else:
            self.letterList.append(self.getVowel())
            Label(screen, text = self.vowelCount,
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = 500, y = 375, width = 80, height = 275)
        if len(self.letterList) == 9: #when it reaches max size
            screen.destroy()
            print(self.letterList)
            self.displaySelected()

    def displaySelected(self):
        screen = Tk()
        screen.geometry("900x125+510+50")
        for i in range(0, 9):
            Label(screen, text = self.letterList[i],
                                bg = "black", foreground = "white", font = ("Comic Sans", 12, "bold")).place(x = i*100, y = 0, width = 100, height = 125)

       
        clock = Clock.Clock() #display the clock
        self.letters_screen.destroy()
        self.letters_screen.after(30000, lambda: [self.timesUp(clock), screen.destroy()])
        

    
    def timesUp(self, clock):
        clock.destroyScreen()
        
        selected = Selection(self.letterList, self.score)
        selected.displayLetters()

    def updateScore(length):

        self.score += length
        print("new score is: ", self.score)
        
      


            
    
        
            
        
    # total of nine letters; at least 3 self.vowels and 4 self.consonants
    def randomLetters(self):
        vowelCount = 0
        consonantCount = 0
        while vowelCount < 3:
            self.letterList.append(self.getVowel())
            vowelCount += 1
        while consonantCount < 4:
            self.letterList.append(self.getConsonant())
            consonantCount += 1
        for i in range(2):
            self.letterList.append(self.getRandomLetter())
        random.shuffle(self.letterList)
        return self.letterList

   


    

    def validLetters(self, word):
        for i in word:
            if i in self.letterList:
                return True
            else:
                return False


    def win(self, word):
        if self.validWord(word):
            if self.validLetters(word):
                length = len(word)
                self.score = self.score + length

        return self.score


    
    def randomSelected(self):
        letterSelection = self.randomLetters()
        self.displaySelected()

    def chooseSelected(self):
        letterSelection = self.selectLetters()





class Selection():

    def __init__(self, letterList, score):
        self.word = ""
        self.letterList = letterList
        self.indexOfAdded = []
        self.score = score #score should be passed in
        

    def displayLetters(self):

        screen = Tk()
        screen.configure(bg = "light grey")
        screen.title("Try and find words from these letters!")
        screen.geometry("900x525+510+50")
        
        Button(screen, text = self.letterList[0], command = lambda: self.addChosenLetter(0, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 0*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[1], command = lambda: self.addChosenLetter(1, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 1*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[2], command = lambda: self.addChosenLetter(2, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 2*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[3], command = lambda: self.addChosenLetter(3, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 3*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[4], command = lambda: self.addChosenLetter(4, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 4*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[5], command = lambda: self.addChosenLetter(5, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 5*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[6], command = lambda: self.addChosenLetter(6, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 6*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[7], command = lambda: self.addChosenLetter(7, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 7*100, y = 0, width = 100, height = 125)
        Button(screen, text = self.letterList[8], command = lambda: self.addChosenLetter(8, screen),
                            bg = "black", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 8*100, y = 0, width = 100, height = 125)

        Button(screen, text = "Undo", command = lambda: self.undo(screen),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 0, y = 125, width = 900, height = 200)
        Button(screen, text = "Confirm", command = lambda: self.confirmed(screen),
                            bg = "light grey", foreground = "white", font = ("Comic Sans", 20, "bold")).place(x = 0, y = 325, width = 900, height = 200)


        
    def addChosenLetter(self, i, screen):
        Label(screen, bg = "light grey").place(x = i*100, y = 0, width = 100, height = 125)
        self.word += self.letterList[i]
        self.indexOfAdded.append(i)

    def undo(self, screen):

        screen.destroy()
        self.word = ""
        self.displayLetters()

    def confirmed(self, screen):
        if self.validWord():
            self.updateScore()
            
        self.backToMain(screen)

        
    def backToMain(self, screen):
        screen.destroy()
        time.sleep(1)
        
        mainScreen.MainScreen(self.score)

        

    def validWord(self):
        if len(self.word) > 1 and self.word in english_words_set:
            
            return True
        else:
            return False
        
    def updateScore(self):
        self.score += len(self.word)
        print(self.score)

            

        

        



        



if __name__ == '__main__':
    letters = LettersGame(0)


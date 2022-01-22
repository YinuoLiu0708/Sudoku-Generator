"""Pygame setting to create an interactive Sudoku board."""

from curses import window
from operator import imod
import pygame, sys
from sudoku_solver import *
import copy

class Board:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku Player")
        self.window = pygame.display.set_mode((600, 600))
        self.running = True
        self.mousePos = None
        self.selected = None
        self.font = pygame.font.SysFont("arial", 25)
        self.mistake = 0
        self.sudoku = generate()
        self.ori_sudoku = copy.deepcopy(self.sudoku)
        self.solution = copy.deepcopy(self.sudoku)
        solve(self.solution)
        self.lockedCells = []
        self.incorrectNum = []
        self.correct = False
        self.game_time = 0
        self.start_tick = pygame.time.get_ticks() 
        self.complete = False

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
               
    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                # user clicks
                if event.type == pygame.MOUSEBUTTONDOWN:                   
                    boardPos = self.mouseOnBoard()
                    if boardPos:
                    
                       self.selected = boardPos
                    else:
                       self.selected = None
                
                # user types into number
                if event.type == pygame.KEYDOWN:
                    if self.isInt(event.unicode):
                        self.sudoku[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.check(self.selected,int(event.unicode))
                        if self.correct:
                            self.lockedCells.append(self.selected)
                        else:
                            self.incorrectNum.append(self.selected)
                            self.mistake += 1

    def draw(self):
        self.window.fill("White")
        if self.selected:
            self.drawCell(self.window, self.selected)
        self.findLockedCells()
        self.redIncorrect()
        self.shadeCells()
        self.drawNumbers(self.sudoku)
        self.showMistake()
        self.showTime()
        self.checkComplete()
        self.drawBoard()
        pygame.display.update()

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def drawBoard(self):
    # draw a 9x9 board on window
        pygame.draw.rect(self.window, "Black", (75, 100, 450, 450), 2)
        for x in range(1,9):   
            pygame.draw.line(self.window,"Black",(75+50*x, 100),(75+50*x, 550),2 if x % 3 == 0 else 1)
            pygame.draw.line(self.window,"Black",(75,100+50*x),(525, 100+50*x),2 if x % 3 == 0 else 1)
                 
    def drawCell(self,window,pos):
    # draw cell that the mouse clicks    
        LIGHTBLUE = (135,206,250)
        pygame.draw.rect(window,LIGHTBLUE,(75+pos[0]*50,100+pos[1]*50,50,50))
    
    def drawNumbers(self,numbers):
        for y, row in enumerate(numbers):
            for x, num in enumerate(row):
                if num != 0:
                    pos = [50*x+93,50*y+112]
                    self.textToScreen(self.window,str(num),pos)

    def findLockedCells(self):
        for y, row in enumerate(self.ori_sudoku):
            for x, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([x,y])

    def shadeCells(self):
        GREY = (207,207,207)
        for cell in self.lockedCells:
            pygame.draw.rect(self.window,GREY,(75+cell[0]*50,100+cell[1]*50,50,50))

    def redIncorrect(self):
        RED = (255,182,193)
        for cell in self.incorrectNum:
            pygame.draw.rect(self.window,RED,(75+cell[0]*50,100+cell[1]*50,50,50))

    def showMistake(self):
        pos = [410,55]
        text = f"mistake: {self.mistake}"
        self.textToScreen(self.window,text,pos)

    def textToScreen(self,window,text,pos):
        font = self.font.render(text,True,"Black")
        window.blit(font,pos)

    def mouseOnBoard(self):
        if self.mousePos[0] < 75 or self.mousePos[1] < 100:
            return False
        elif self.mousePos[0] > 525 or self.mousePos[1] > 550:
            return False
        else:
            return ((self.mousePos[0]-75)//50, (self.mousePos[1]-100)//50)

    def isInt(self, str):
        try:
            int(str)
            return True
        except:
            return False

    def check(self,po,num):
        # Check to see the correctness of the filled number
        x = po[1]
        y = po[0]
        if num == self.solution[x][y]:
            self.correct = True
        else:
            self.correct = False

    def showTime(self):
        seconds = (pygame.time.get_ticks() - self.start_tick) // 1000
        if self.game_time != seconds: 
            self.game_time = seconds
        
        minutes = self.game_time // 60
        secs = str(self.game_time % 60) if (self.game_time % 60) > 9 else "0"+str(self.game_time % 60)
        
        pos = [410,20]
        text = f"time: {minutes}:" + secs
        self.textToScreen(self.window,text,pos)

    def checkComplete(self):
        blank = find_empty(self.sudoku)
        pos = [250,50]
        text = "You did it!"
        if not blank and self.sudoku == self.solution:
            self.complete = True
        if self.complete == True:
            self.textToScreen(self.window,text,pos)
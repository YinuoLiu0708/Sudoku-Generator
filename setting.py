"""Pygame setting to create an interactive Sudoku board."""

from curses import window
import pygame, sys
from sudoku_solver import *

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

                if event.type == pygame.MOUSEBUTTONDOWN:                   
                    boardPos = self.mouseOnBoard()
                    if boardPos:
                    
                       self.selected = boardPos
                    else:
                       self.selected = None
    
    def draw(self):
        self.window.fill("White")
        if self.selected:
            self.drawCell(self.window, self.selected)
        self.drawNumbers()
        self.drawBoard()
        pygame.display.update()

    def drawBoard(self):
    # draw a 9x9 board on window
        pygame.draw.rect(self.window, "Black", (75, 100, 450, 450), 2)
        for x in range(1,9):   
            pygame.draw.line(self.window,"Black",(75+50*x, 100),(75+50*x, 550),2 if x % 3 == 0 else 1)
            pygame.draw.line(self.window,"Black",(75,100+50*x),(525, 100+50*x),2 if x % 3 == 0 else 1)
        
                
    def drawCell(self,window,pos):
    # draw cell that the mouse clicks    
        LIGHTBLUE = (100,149,237)
        pygame.draw.rect(window,LIGHTBLUE,(75+pos[0]*50,100+pos[1]*50,50,50))
    
    def drawNumbers(self):
        for y, row in enumerate(self.sudoku):
            for x, num in enumerate(row):
                if num != 0:
                    pos = [50*x+93,50*y+112]
                    self.textToScreen(self.window,str(num),pos)


    def textToScreen(self,window,text,pos):
        font = self.font.render(text,True,"Black")
        window.blit(font,pos)

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def mouseOnBoard(self):
        if self.mousePos[0] < 75 or self.mousePos[1] < 100:
            return False
        elif self.mousePos[0] > 525 or self.mousePos[1] > 550:
            return False
        else:
            return ((self.mousePos[0]-75)//50, (self.mousePos[1]-100)//50)
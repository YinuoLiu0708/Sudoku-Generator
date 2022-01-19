"""Pygame setting to create an interactive Sudoku board."""

from curses import window
import pygame, sys

class Board:
    # variables
    testBoard = [[0 for x in range(9)] for x in range(9)]

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku Player")
        self.window = pygame.display.set_mode((600, 600))
        self.window.fill("White")
        self.running = True
        self.mousePos = None

       
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
                    # draw cell that the mouse clicks
                       self.drawCell(self.window, boardPos)
                    else:
                       return None
    
    def draw(self):
        # draw a 9x9 board on window
        pygame.draw.rect(self.window, "Black", (75, 100, 450, 450), 2)
        for x in range(1,9):   
            pygame.draw.line(self.window,"Black",(75+50*x, 100),(75+50*x, 550),2 if x % 3 == 0 else 1)
            pygame.draw.line(self.window,"Black",(75,100+50*x),(525, 100+50*x),2 if x % 3 == 0 else 1)
        
        pygame.display.update()
        

    def drawCell(self,window,pos):
        LIGHTBLUE = (100,149,237)
        pygame.draw.rect(window,LIGHTBLUE,(75+pos[0]*50,100+pos[1]*50,50,50))

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def mouseOnBoard(self):
        if self.mousePos[0] < 75 or self.mousePos[1] < 100:
            return False
        elif self.mousePos[0] > 525 or self.mousePos[1] > 550:
            return False
        else:
            return ((self.mousePos[0]-75)//50, (self.mousePos[1]-100)//50)
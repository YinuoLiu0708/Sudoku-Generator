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

       
    def run(self):
        while self.running:
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    
    def draw(self):
        pygame.draw.rect(self.window, "Black", (75, 100, 450, 450), 2)
        for x in range(1,9):   
            pygame.draw.line(self.window,"Black",(75+50*x, 100),(75+50*x, 550),2 if x % 3 == 0 else 1)
            pygame.draw.line(self.window,"Black",(75,100+50*x),(525, 100+50*x),2 if x % 3 == 0 else 1)

        
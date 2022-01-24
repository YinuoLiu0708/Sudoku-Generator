"""Create a button with the function of showing solution."""

import pygame

class Button:
    def __init__(self):
        self.image = pygame.Surface((125,30))
        self.pos = (75,52)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = "show solution"
        self.color = (224,238,238)
        self.hightenedcolor = (240,248,255)
        self.highlighted = False
        self.showSolution = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(self.hightenedcolor if self.highlighted else self.color)
        self.drawText()
        window.blit(self.image, self.pos)

    def drawText(self):
        font = pygame.font.SysFont("arial", 20)
        text = font.render(self.text, True, "Black")
        self.image.blit(text,(2,2)) 

    def click(self):
        self.showSolution = True
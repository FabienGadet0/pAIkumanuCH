import pygame
from pygame.locals import *

WINDOW_NAME = "pAIkumanuCH"
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500


class Graphics:

    def __init__(self):
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.cellx = 0
        self.celly = 0
        self.lastKeyPressed = ""
        pygame.display.set_caption(WINDOW_NAME)
        pygame.mouse.set_visible(0)

    def get_last_key(self):
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.lastKeyPressed = "LEFT"
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.lastKeyPressed = "RIGHT"
            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.lastKeyPressed = "DOWN"
            elif event.type == KEYDOWN and event.key == K_UP:
                self.lastKeyPressed = "UP"
        return self.lastKeyPressed

    def draw_this_shit(self, grid):
        # Draw Everything
        self.cellx = WINDOW_WIDTH//len(grid[0])
        self.celly = WINDOW_HEIGHT//len(grid)
        self.screen.fill((0, 0, 0), rect=None, special_flags=0)
        currenty = 0
        currentx = 0
        for row in grid:
            for cell in row:
                color = self._get_gud_color(cell)
                pygame.draw.rect(
                    self.screen, color,
                    (currentx, currenty, self.cellx, self.celly))
                currentx += self.cellx
            currenty += self.celly
            currentx = 0
        pygame.display.flip()

    def _get_gud_color(self, code):
        if code == "0":
            return (255, 255, 0)
        elif code == "W":
            return (66, 78, 244)
        elif code in '12345678':
            return (255, 255, 255)
        elif code == "C":
            return (249, 168, 4)
        elif code == "S":
            return (138, 25, 214)
        elif code == "V":
            return (0, 0, 0)
        else:
            return (255, 0, 255, 0)

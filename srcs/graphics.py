import pygame
from pygame.locals import *

WINDOW_NAME = "pAIkumanuCH"
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500


class Graphics:

    # Initialize Everything
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.cell = (0, 0)
        self.lastKeyPressed = ""
        self.sprites_list = pygame.sprite.Group()
        pygame.display.set_caption(WINDOW_NAME)
        pygame.mouse.set_visible(0)

    # Handle Input Events
    def get_last_key(self):
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

    # Draw Everything
    def draw_this_shit(self, gridu):
        self._handle_sprites_from_gridu(gridu)
        grid = gridu.grid_
        self.cell = (WINDOW_WIDTH//len(grid[0]), WINDOW_HEIGHT//len(grid))
        self.screen.fill((0, 0, 0), rect=None, special_flags=0)
        currenty = 0
        currentx = 0
        for row in grid:
            for cell in row:
                color = self._get_gud_color(cell)
                pygame.draw.rect(
                    self.screen, color,
                    (currentx, currenty, self.cell[0], self.cell[1]))
                currentx += self.cell[0]
            currenty += self.cell[1]
            currentx = 0
        self.sprites_list.draw(self.screen)
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

    def _handle_sprites_from_gridu(self, gridu):
        self.sprites_list.empty()
        pacu = gridu.get_pacu()
        pacu_rekt = pacu.image.get_rect()
        pacu_rekt.x = 10
        pacu_rekt.y = 10
        self.sprites_list.add(pacu)
        # a decommenter quand on aura les sprites des ghostu
        # ghostu_list = gridu.get_ghostu()
        #   for ghostu in ghostu_list:
        #       ghostu.image;get_rect()
        #       self.sprites_list.add(ghostu)

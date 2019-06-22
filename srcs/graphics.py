import pygame

WINDOW_NAME = "Fenetre de ses morts"
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480

Class Graphics:

    def __init__(self):
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_NAME)
        pygame.mouse.set_visible(0)

    def _update(self, grid):
        """this function is called at every loop and
        redraws according to the grid"""
        self.cellx = WINDOW_WIDTH//len(grid[0])
        self.celly = WINDOW_HEIGHT//len(grid)
        # Draw everything
        self._draw_this_shit(grid)
        # Handle Input Events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEY_LEFT:
                self.lastKeyPressed = "LEFT"
            elif event.type == KEY_RIGHT:
                self.lastKeyPressed = "RIGHT"
            elif event.type == KEY_DOWN:
                self.lastKeyPressed = "DOWN"
            elif event.type == KEY_UP:
                self.lastKeyPressed = "UP"

    def _get_last_key(self):
        return self.lastKeyPressed

    def _draw_this_shit(self, grid):
        # Draw Everything
        screen.fill((0, 0, 0), rect=None, special_flags=0)

        for row in grid:
            currenty = 0
            for cell in row:
                currentx = 0
                pygame.draw.rect(
                    self.screen, self._get_gud_color(cell),
                    (currentx, currenty, self.cellx, self.celly), width=0)
                currentx += self.cellx
            currenty += self.celly
        pygame.display.update()

    def _get_gud_color(self, code):
        if code == "P":
            return (255, 255, 0)
        elif code == "W":
            return (66, 78, 244)
        elif code == "G":
            return (255, 255, 255)
        elif code == "C":
            return (249, 168, 4)
        elif code == "S":
            return (138, 25, 214)
        elif code == "V":
            return (0, 0, 0)

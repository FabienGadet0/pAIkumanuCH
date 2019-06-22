import pygame

WINDOW_NAME = "Fenetre de ses morts"
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000


class Graphics:

    def __init__(self):
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.cellx = 0
        self.celly = 0
        pygame.display.set_caption(WINDOW_NAME)
        pygame.mouse.set_visible(0)

    def update(self, grid):
        """this function is called at every loop and
        redraws according to the grid"""
        # Draw everything
        self._draw_this_shit(grid)
        # Handle Input Events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEY_LEFT:
                self.lastKeyPressed = "LEFT"
            elif event.type == pygame.KEY_RIGHT:
                self.lastKeyPressed = "RIGHT"
            elif event.type == pygame.KEY_DOWN:
                self.lastKeyPressed = "DOWN"
            elif event.type == pygame.KEY_UP:
                self.lastKeyPressed = "UP"

    def get_last_key(self):
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
                print(color)
                print(currentx)
                print(currenty)

            currenty += self.celly
            currentx = 0
        pygame.display.update()

    def _get_gud_color(self, code):
        if code == "P":
            return (255, 255, 0)
        elif code == "W":
            return (66, 78, 244)
        elif code == "Y" or code == "U" or code == "Z" or code == "X":
            return (255, 255, 255)
        elif code == "C":
            return (249, 168, 4)
        elif code == "S":
            return (138, 25, 214)
        elif code == "V":
            return (0, 0, 0)

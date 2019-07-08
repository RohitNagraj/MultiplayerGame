import pygame

# Dimensions of the screen
width = 500
height = 500

# Initializing a new pygame window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")  # Title of the window


# To hold no. of clients created
clientNumber = 0


class Player:
    """
    Main player class to control all player functions
    """

    def __init__(self, x, y, width, height, color):

        """
        :param x: Initial x coordinate of player
        :param y: Initial y coordinate of player
        :param width: Width of player window
        :param height: Weight of player window
        :param color: Color of player
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 0.5

    def draw(self, win):
        """
        Draws the player rectangle on the window
        :param win: the player window object
        :return: None
        """
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """
        Reads for input from keyboard and moves player accordingly
        :return: None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(player, win):
    """
    Draws the player window again
    :param player: Player class object
    :param win: Window to draw player on
    :return: None
    """
    win.fill((0, 0, 0))        # fill with black bg color
    player.draw(win)           # Draw the player rectangle on the window
    pygame.display.update()    # update the window to display the changes


def main():

    run = True

    p = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                run = False

        p.move()
        redraw_window(p, win)


if __name__ == '__main__':
    main()

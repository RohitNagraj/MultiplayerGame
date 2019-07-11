import pygame


class Player:
    """
    Main player class to control all player state & functions
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
        self.vel = 3

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

        self.update()

    def update(self):
        """
        Defines the tuple required to create a rectangle
        :return: tuple
        """
        self.rect = (self.x, self.y, self.width, self.height)

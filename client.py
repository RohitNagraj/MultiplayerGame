import pygame
from network import Network

# Dimensions of the screen
width = 500
height = 500

# Initializing a new pygame window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")  # Title of the window


# To hold no. of clients created
clientNumber = 0

# To count the no. of frames
clock = pygame.time.Clock()


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


def redraw_window(player1, player2, win):
    """
    Draws the player window again
    :param player1: Player1 class object
    :param player2: Player2 class object
    :param win: Window to draw player on
    :return: None
    """
    win.fill((0, 0, 0))        # fill with black bg color
    player1.draw(win)           # Draw the player rectangle on the window
    player2.draw(win)
    pygame.display.update()    # update the window to display the changes


def read_pos(pos):
    """
    Converts string data coming from server to tuple
    :param pos: string data
    :return: position tuple
    """
    pos = pos.split(',')
    return int(pos[0]), int(pos[1])


def make_pos(tup):
    """
    Converts tuple data from client to sendable server string
    :param tup: tuple data
    :return: string data
    """
    return str(tup[0]) + ',' + str(tup[1])


def main():

    run = True

    # Create a new client
    n = Network()
    start_pos = read_pos(n.get_pos())    # Gets the starting position of that client from server

    p1 = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))    # Define the player at that starting position
    p2 = Player(0, 0, 100, 100, (0, 255, 0))    # Defines player 2 at its position

    while run:

        clock.tick(60)

        # Send position of p1. It returns position of p2.
        p2pos = read_pos(n.send(make_pos((p1.x, p1.y))))

        # Update the position of p2 accordingly
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        # To check if the game has to be quit
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                run = False

        # Check for move from p1
        p1.move()
        # Redraw the window with whatever updated positions of p1 and p2 are
        redraw_window(p1, p2, win)


if __name__ == '__main__':
    main()

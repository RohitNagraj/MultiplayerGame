import pygame

from network import Network

# Dimensions of the screen
width = 500
height = 500

# Initializing a new pygame window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")  # Title of the window


# To count the no. of frames
clock = pygame.time.Clock()


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


def main():

    run = True

    # Create a new client
    n = Network()

    # Get initial state of Player1
    p1 = n.get_p()

    while run:

        clock.tick(60)

        # Send the state of Player1 and receive state of Player2
        p2 = n.send(p1)

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

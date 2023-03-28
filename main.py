

# Modules used
import pygame
import time

class henon:
    def __init__(self, y0, a, b):
        self.y0 = y0
        self.a = a
        self.b = b

    # Henon System
    def henon_system(self, x, y):
        return [1 - self.a*x**2 + y, self.b*x]

def main():
    # Initializes display
    pygame.init()
    SIZE = (900, 600)
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Henon Attractor") # Title
    COLOR = (255, 255, 255) # Colour is white
    pygame.display.flip()
    clock = pygame.time.Clock()

    # Initial display states.
    running = True
    pressed_return = False

    # timer starts at 0.
    timer = time.time()

    # Initialised henon Attractor.
    y0 = [0, 0]
    a = 1.4 # Value for `a`
    b = 0.3 # Value for `b`
    hs = henon(y0, a, b)

    while running:
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            # Press the x in the top left corner to quit.
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                
                # press `q` to quit.
                if event.key == pygame.K_q:
                    running = False

                # Press `return` to start.
                if event.key == pygame.K_RETURN:
                    pressed_return = True


        # Sets the initial condition `y0`.
        if not pressed_return:
            [x, y] = hs.y0
        
        # Check if the return key was pressed.
        if pressed_return:

            # henon system
            [x_new, y_new] = hs.henon_system(x, y)

            # Display coordinates
            x_display = int(SIZE[0]/2 + x_new*300)
            y_display = int(SIZE[1]/2 + y_new*400)

            [x, y] = [x_new, y_new]

            pygame.draw.circle(SCREEN, COLOR, (x_display, y_display), 1)

            pygame.display.flip()
            pygame.time.wait(10)

            # Check if the time difference is 60 seconds then game will stop.
            if timer - time.time() == 60:
                running = False
    
    pygame.quit()

if __name__ == '__main__':
    main()
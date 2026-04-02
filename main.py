import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: VERSION")

    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Initialize pygame
    pygame.init()

    #create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock object and delta time variable
    clock = pygame.time.Clock()
    dt = 0

    # Create player object in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
        # Log game state
        log_state()

        # Process pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        # Fill screen with black
        screen.fill("black")

        # Update player
        player.update(dt)
        # Draw the player (after filling the screen, before flipping)
        player.draw(screen)

        #Refresh the screen
        pygame.display.flip()
        
        #Limit to 60 FPS and calculate  delta time
        dt = clock.tick(60) / 1000.0
       # print(dt)

if __name__ == "__main__":
    main()

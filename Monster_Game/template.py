import pygame

def main():
    width = 1000
    height = 500
    purple_color = (128, 0, 128)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Boxes')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(purple_color)

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

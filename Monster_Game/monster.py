import pygame
bg_img = pygame.image.load('images/background.png')
hero_img = pygame.image.load('images/hero.png')
#goblin = pygame.image.load('images/goblin.png')
monster_img = pygame.image.load('images/monster.png')


class Sprite:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def update(self, width, height):
        self.x += self.speed
        self.y += self.speed
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0

    def display(self, image)
        screen.blit(self.image, (x, y))

monster = Sprite(50, 50, 5)


def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(bg_img, (0, 0))
        monster.display(monster_img.image, (50, 50))


        # Game display
        monster.update(width, height)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

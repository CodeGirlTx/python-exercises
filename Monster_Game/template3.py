import pygame

bg_img = pygame.image.load('images/background.png')
monster_img = pygame.image.load('images/monster.png')
hero_img = pygame.image.load('images/hero.png')
goblin_img = pygame.image.load('images/goblin.png')

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Sprite:
    def __init__(self, x, y, radius, speed, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.name = name


    def update(self, dir_x, dir_y):
        self.x += dir_x
        self.y += dir_y
        if self.x + self.radius > 512:
            dir_x = -dir_x
        if self.y + self.radius > 480:
            dir_y = -dir_y
        if self.x - self.radius < 0:
            dir_x = -dir_x
        if self.y - self.radius < 0:
            dir_y = -dir_y


def main():
    hero = Sprite(240, 230, 32, 10, 'hero')
    monster = Sprite(50, 75, 32, 5, 'monster')
    goblin = Sprite(400, 400, 32, 3, 'goblin')

    width = 512
    height = 480
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    pygame.mixer.init()
    sound_win = pygame.mixer.Sound('sounds/win.wav')
    sound_lose = pygame.mixer.Sound('sounds/lose.wav')
    sound_main = pygame.mixer.Sound('sounds/music.wav')
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text = font.render('You WIN!', True, black_color)
    text_2 = font.render('Press enter to play again', True, black_color)
    text_lose = font.render('You lose. :(', True, black_color)
    text_lose_x = -50
    text_lose_y = -50
    text_x = -50
    text_y = -50
    text_2_x = -50
    text_2_y = -50

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    change_dir_countdown = 120
    # monster_dir_x = 5
    # monster_dir_y = 5
    goblin_dir_x = 3
    goblin_dir_y = 3

    sound_main.play()
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero.y += 20
                elif event.key == KEY_UP:
                    hero.y -= 20
                elif event.key == KEY_LEFT:
                    hero.x -= 20
                elif event.key == KEY_RIGHT:
                    hero.x += 20

            hero_rect = pygame.Rect(hero.x, hero.y, 40, 40)
            monster_rect = pygame.Rect(monster.x, monster.y, 40, 40)
            goblin_rect = pygame.Rect(goblin.x, goblin.y, 40, 40)

            if hero_rect.colliderect(monster_rect):
                sound_main.stop()
                monster.x = -50
                monster.y = -50
                hero.x = 240
                hero.y = 300
                goblin.x = -50
                goblin.y = -50
                sound_win.play()
                text_x = 185
                text_y = 200
                text_2_x = 85
                text_2_y = 230

            if hero_rect.colliderect(goblin_rect):
                sound_main.stop()
                monster.x = -50
                monster.y = -50
                goblin.x = 240
                goblin.y = 300
                hero.x = -50
                hero.y = -50
                sound_lose.play()
                text_lose_x = 185
                text_lose_y = 200
                text_2_x = 85
                text_2_y = 230

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'restart'

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        if hero.x + hero.radius >= width:
            hero.x -= 10
        if hero.x + hero.radius <= 0:
            hero.x += 40
        if hero.y + hero.radius >= height:
            hero.y -= 10
        if hero.y + hero.radius <= 0:
            hero.y += 40

        monster.update(5, 5)
        # monster.x += monster_dir_x
        # monster.y += monster_dir_y
        # if monster.x + monster.radius > width:
        #     monster_dir_x = -monster_dir_x
        # if monster.y + monster.radius > height:
        #     monster_dir_y = -monster_dir_y
        # if monster.x - monster.radius < 0:
        #     monster_dir_x = -monster_dir_x
        # if monster.y - monster.radius < 0:
        #     monster_dir_y = -monster_dir_y

        goblin.x += goblin_dir_x
        goblin.y += goblin_dir_y
        if goblin.x + goblin.radius > width:
            goblin_dir_x = -goblin_dir_x
        if goblin.y + goblin.radius > height:
            goblin_dir_y = -goblin_dir_y
        if goblin.x - goblin.radius < 0:
            goblin_dir_x = -goblin_dir_x
        if goblin.y - goblin.radius < 0:
            goblin_dir_y = -goblin_dir_y



        # Draw background
        screen.fill(blue_color)
        screen.blit(bg_img, (0,0))
        screen.blit(hero_img, (hero.x, hero.y))
        monster_show = screen.blit(monster_img, (monster.x, monster.y))
        screen.blit(text, (text_x, text_y))
        screen.blit(text_2, (text_2_x, text_2_y))
        screen.blit(text_lose, (text_lose_x, text_lose_y))
        screen.blit(goblin_img, (goblin.x, goblin.y))


        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    restart = 'restart'
    while restart == 'restart':
        restart = main()

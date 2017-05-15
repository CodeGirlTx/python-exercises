import pygame
import time

bg_img = pygame.image.load('images/background.png')
monster_img = pygame.image.load('images/monster.png')
hero_img = pygame.image.load('images/hero.png')
goblin_img = pygame.image.load('images/goblin.png')

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Sprite:
    def __init__(self, x, y, radius, dir_x, dir_y, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.name = name

    def update(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x + self.radius > 512:
            self.dir_x = -self.dir_x
        if self.y + self.radius > 480:
            self.dir_y = -self.dir_y
        if self.x - self.radius < 0:
            self.dir_x = -self.dir_x
        if self.y - self.radius < 0:
            self.dir_y = -self.dir_y

    def change_dir():
        if self.dir_x == -self.dir_x:
            self.dir_x = self.dir_x
        if self.dir_y == -self.dir_y:
            self.dir_y = self.dir_y

    def hide(self):
        self.x = -50
        self.y = -50

# def countdown():
#     t = 5
#     print("started timer")
#     while t > 0:
#         t -= 1
#         print(t)
#         if t == 0:
#             monster.change_dir()
#             print("changedirection")
def level_counter():
    level = 1
    while level <= 4:
        level += 1

def levels():
    while level == 1:
        return main()
    while level == 2:
        return main2()
    # while level == 3:
    #     return main3()


def main2()
def main():
    # countdown()

    hero = Sprite(240, 230, 32, 10, 10, 'hero')
    monster = Sprite(50, 75, 32, 5, 5, 'monster')
    goblin = Sprite(400, 400, 32, 2, 2, 'goblin')
    #goblin2 = Sprite(50, 150, 32, 1, 1, 'goblin2')
    #goblin3 = Sprite(300, 300, 32, 4, 4, 'goblin3')

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
    text_level = font.render('Level 1', True, black_color)
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

            hero_rect = pygame.Rect(hero.x, hero.y, 32, 32)
            monster_rect = pygame.Rect(monster.x, monster.y, 32, 32)
            goblin_rect = pygame.Rect(goblin.x, goblin.y, 32, 32)
            #goblin2_rect = pygame.Rect(goblin2.x, goblin2.y, 32, 32)
            #goblin3_rect = pygame.Rect(goblin3.x, goblin3.y, 32, 32)

            if hero_rect.colliderect(monster_rect):
                sound_main.stop()
                monster.hide()
                hero.x = 240
                hero.y = 300
                goblin.hide()
                #goblin2.hide()
                #goblin3.hide()
                sound_win.play()
                text_x = 185
                text_y = 200
                text_2_x = 85
                text_2_y = 230

            if hero_rect.colliderect(goblin_rect) or hero_rect.colliderect(goblin2_rect) or hero_rect.colliderect(goblin3_rect):
                sound_main.stop()
                monster.hide()
                goblin.hide()
                #goblin2.hide()
                #goblin3.hide()
                hero.hide()
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

        goblin.update()
        #goblin2.update()
        #goblin3.update()
        monster.update()

        # Draw background
        screen.fill(blue_color)
        screen.blit(bg_img, (0,0))
        screen.blit(hero_img, (hero.x, hero.y))
        screen.blit(monster_img, (monster.x, monster.y))
        screen.blit(text, (text_x, text_y))
        screen.blit(text_2, (text_2_x, text_2_y))
        screen.blit(text_lose, (text_lose_x, text_lose_y))
        screen.blit(goblin_img, (goblin.x, goblin.y))
        #screen.blit(goblin_img, (goblin2.x, goblin2.y))
        #screen.blit(goblin_img, (goblin3.x, goblin3.y))
        # screen.blit(text_level, (text_level_x, text_level_y))


        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    restart = 'restart'
    while restart == 'restart':
        restart = main()

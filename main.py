from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_presed = key.get_pressed()
        if key_presed[K_w]:
            self.rect.y -= self.speed
        if key_presed[K_s]:
            self.rect.y += self.speed
        if key_presed[K_a]:
            self.rect.x -= self.speed
        if key_presed[K_d]:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'right'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >600:
            self.direction = 'left'
        if self.rect.x == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, r, g, b, x , y, w, h ):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b 
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((self.red, self.green, self.blue))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Лабаиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))


hero = Player('hero.png', 105, 105, 5)
cyborg = Enemy('cyborg.png', 300, 300, 3)
gold = GameSprite('treasure.png', 500, 400, 0)
w1 = Wall(255, 0, 0, 100, 20, 5000, 10)#красный
w2 = Wall(255, 20, 147, 100, 20, 10, 450)#розовый
w3 = Wall(0, 128, 0, 100, 200, 100, 10)#зелёный
w4 = Wall(255, 255, 0, 100, 450, 450, 10)#жёлтый
w5 = Wall(0, 0, 255, 300, 20, 10, 300)#синий
w6 = Wall(0, 0, 0, 400, 120, 10, 400)#негр
w7 = Wall(255, 255, 255, 400, 200, 200, 10)#белый
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


font.init()
font = font.Font(None, 70)
win = font.render('Ты читер!', True, (225, 215, 0))
lose = font.render('Ты лох!',True, (180, 0 ,0))
finish = False



game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        cyborg.reset()
        gold.reset()


    cyborg.update()
    gold.reset()
    hero.update()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    if sprite.collide_rect(hero, cyborg):
        finish = True
        window.blit(lose, (200, 200))


    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(60)

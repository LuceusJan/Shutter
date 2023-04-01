#Создай собственный Шутер!
from pygame import *
from random import randint
font.init()

speed = 8
lost = 0
papal = 0

bullets = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
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
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        bullet1 = Bullet("bullet.png", self.rect.centerx, self.rect.top, 2, 3, -15)
        bullets.add(bullet1)
        '''if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed'''


class Enemy(GameSprite):
    '''direction = "left"'''
    def update(self):
        '''if self.rect.x <= 470:'''
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
            '''self.direction = "right"
        if self.rect.x >=  win_width - 82:
            self.direction = "left"
        if self.direction == "left":            
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed''' 

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 72)

'''monsters = sprite.Group() 
monsters.add(monster)
monsters.draw(window)
monsters.update()'''   #функции групп

'''monster = Enemy('ufo.png', 5, win_height - 82, 4)'''
mixer.init()
win_width = 700
win_height = 500
player = Player('rocket.png', 5, win_height - 82, 300, 100,4)
mixer.init()

fire_shot = mixer.Sound('fire.ogg')

text1 = input('Ты кто? Ян?')
print("Ладно тогда играй!")

window = display.set_mode((win_width, win_height))
display.set_caption('Космический Шутер')
mixer.music.load("space.ogg")
mixer.music.play()
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height)) #создай окно игры

luser = font2.render('Лох! Ты сдох!', 1, (255, 255, 255))
losur = font2.render('Выйгрыш!', 1, (255, 255, 255))

x1 = 480
y1 = 120
x2 = 360
y2 = 240
x3 = 500
y3 = 200

monsters = sprite.Group()
for i in range(1, 4):
    monster1 = Enemy('ufo.png', randint(80, win_width - 80), 30, 40, -40, randint(1, 5))
    monsters.add(monster1)
    
game = True
finish = False
clock = time.Clock()
FPS = 120

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if finish != True:
        window.blit(background,(0, 0))
        prop = font1.render('Пропустил: ' + str(lost), 1, (255, 255, 255))
        pop = font1.render('Попал: ' + str(papal), 1, (255, 255, 255))
        window.blit(prop,(0, 0))
        window.blit(pop,(0, 30))
        player.update()
        monsters.update()
        bullets.update()

        player.reset()
        bullets.draw(window)
        monsters.draw(window)
        colilides = sprite.groupcollide(monsters, bullets, True, True)
        for i in colilides:
            papal = papal + 1
            monster1 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster1)
        if lost >= 69:
            finish = True
            window.blit(luser, (170, 200))
            mixer.music.pause()
        if papal >= 10:
            finish = True
            window.blit(losur, (170, 200))
            mixer.music.pause()


        
    display.update()
    clock.tick(FPS)
    


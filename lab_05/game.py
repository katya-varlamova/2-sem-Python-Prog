import random
from os import path
import random as r
import time
import pygame
WIDTH = 480
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Covid19")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Virus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = covid_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
class Mask(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mask_img
        self.image = pygame.transform.scale(mask_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    surf.blit(text_surface, text_rect)
    
num = r.randint(1, 30)
img_dir = path.join(path.dirname(__file__), 'img')
if num < 10:
    player_img = pygame.image.load(path.join(img_dir, "0{}.png".format(num))).convert()
else:
    player_img = pygame.image.load(path.join(img_dir, "{}.png".format(num))).convert()
covid_img = pygame.image.load(path.join(img_dir, "covid.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "stay_home.png")).convert()
mask_img = pygame.image.load(path.join(img_dir, "mask.png")).convert()

all_sprites = pygame.sprite.Group()
viruses = pygame.sprite.Group()
bullets = pygame.sprite.Group()
masks = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    m = Virus()
    all_sprites.add(m)
    viruses.add(m)

for i in range(1):
    m = Mask()
    all_sprites.add(m)
    masks.add(m)
protected = False
running = True
time_beg = 0
while running:
    clock.tick(FPS)
    if protected:
        if time.time() - time_beg > 5:
            protected = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    
    all_sprites.update()
    hits = pygame.sprite.groupcollide(viruses, bullets, True, True)
    for hit in hits:
        m = Virus()
        all_sprites.add(m)
        viruses.add(m)
    
    hits = pygame.sprite.spritecollide(player, viruses, True)
    if hits:
        if protected:
            m = Virus()
            all_sprites.add(m)
            viruses.add(m)
        else:
            running = False
        
    hits = pygame.sprite.spritecollide(player, masks, True)
    if hits:
       protected = True
       m = Mask()
       all_sprites.add(m)
       masks.add(m)
       time_beg = time.time()
        
    screen.fill(WHITE)
    all_sprites.draw(screen)
    if protected:
        draw_text(screen, "0:" + str(int(5 - time.time() + time_beg)), 50, WIDTH / 2, 10)
    pygame.display.flip()
pygame.quit()

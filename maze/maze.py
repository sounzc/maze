#создай игру "Лабиринт"!
from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
window = display.set_mode((700,500))
display.set_caption('Maze')
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load("background.jpg"), (700,500))
hero = GameSprite('hero.png', 30, 430, 10)
cyborg = GameSprite('cyborg.png', 630, 300, 5)
treasure = GameSprite('treasure.png',630,400,0)
game = True
FPS = 60
clock = time.Clock()
while game:
    window.blit(background,(0,0))
    hero.reset()
    cyborg.reset()
    treasure.reset()
    clock.tick(FPS)
    mixer.music.play()






    display.update()
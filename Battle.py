import random
import pygame
import config
from box.entity.MyTank import Tank
from box.entity.Object import Object
from box.entity.enemy import enemy
from box.object.button import Button
from config import height, width
from config import enemy_speed as enemyspeed


class Battle:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.h = height
        self.w = width
        self.FPS = config.gamespeed
        self.enemys = pygame.sprite.Group()
        self.tank = pygame.sprite.GroupSingle()
        self.tank.add(Tank(1180, 360, 0, 0, 20))
        self.bullets = pygame.sprite.Group()
        self.ebullets = pygame.sprite.Group()
        self.x, self.y = 0, 0
        self.objects = pygame.sprite.Group()
        self.Big_shoot_key = True
        self.text = pygame.sprite.Group()


    def addenemy(self):
        self.enemys.add(enemy(int(random.random() * (self.w - 500)), int(random.random() * (self.h - 100) + 50),
                              int(random.random() * enemyspeed - enemyspeed / 2),
                              int(random.random() * enemyspeed - enemyspeed / 2),))
    def add_object(self):
        self.objects.add(Object(int(random.random() * (self.w - 500)), int(random.random() * (self.h - 100) + 50),0,30))

    def animation(self, enemy_count):
        self.done = True
        screen = pygame.display.set_mode((width, height))
        x, y = 0, 0
        for i in range(enemy_count + 2):
            self.addenemy()
        for i in range(3):
            self.add_object()
        while self.done:
            exp = 0
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.done = False
            self.clock.tick(config.gamespeed)
            pressed_keys = pygame.key.get_pressed()
            for tk in self.tank:
                if pressed_keys[pygame.K_SPACE]:
                    tk.shoot(self.bullets)
                if pressed_keys[pygame.K_d]:
                    if self.Big_shoot_key:
                        self.Big_shoot_key = False
                        tk.BIGshoot(self.bullets)
                else:
                    self.Big_shoot_key = True
                x, y = tk.location()
            if pressed_keys[pygame.K_ESCAPE]:
                self.done = False
            self.tank.update()
            text = pygame.sprite.Group()
            for i, enemy in enumerate(self.enemys):
                temp = enemy.armer * "|"
                text.add(Button((0, 20 * i), 20, 0, (0, 0, 0), (255, 255, 255), f"Enemy{i+1}_HP:{temp}",screen))
            text.update()
            text = pygame.sprite.Group()
            for i, tank in enumerate(self.tank):
                temp = tank.armer * "|"
                text.add(Button((0, height-20), 20, 0, (0, 0, 0), (255, 255, 255), f"My_HP:{temp}",screen))
            text.update()
            self.bullets.update()
            self.ebullets.update()
            self.enemys.update(self.ebullets, x, y)
            collided_E_B = pygame.sprite.groupcollide(self.enemys, self.bullets, False, True)
            for hit in collided_E_B:
                exp = hit.hit(self.enemys,hit)
            cokkided = pygame.sprite.groupcollide(self.tank, self.ebullets, False, True)
            for hit in cokkided:
                self.done = hit.hit(self.tank,hit)
            cokkided = pygame.sprite.groupcollide(self.bullets, self.ebullets, True, True)
            cokkided = pygame.sprite.groupcollide(self.objects, self.ebullets, False, True)
            cokkided = pygame.sprite.groupcollide(self.objects, self.bullets, False, True)
            for bullet in self.bullets:
                if bullet.out == True:bullet.remove(self.bullets)
            for bullet in self.ebullets:
                if bullet.out == True:bullet.remove(self.bullets)
            self.ebullets.draw(screen)
            self.tank.draw(screen)
            self.enemys.draw(screen)
            self.bullets.draw(screen)
            self.objects.draw(screen)
            try:
                text.draw()
            except:
                pass
            pygame.display.flip()
            if len(self.enemys) <=0:
                self.done = False


    def run(self):
        self.animation()

    def states(self):
        print(self.enemys)
        print(self.ebullets)
        print(self.tank)
        print(self.objects)
        print(self.bullets)

def run_buttle(ec):
    battle_A = Battle()
    battle_A.animation(ec)
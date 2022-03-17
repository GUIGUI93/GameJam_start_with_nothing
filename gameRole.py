# -*- coding: utf-8 -*-
"""
the class for all the objects in the game
@author: ZHANG Chenyu
"""

import pygame
        
# the class bullet
class Friend(pygame.sprite.Sprite):
    def __init__(self, number, init_pos, font):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.font = font
        self.text = font.render(str(number), True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = init_pos
        self.speed = 2
        self.static = True

    def move(self):
        self.rect.top += self.speed  # 子弹的位置不断的往前

class FriendCross(Friend):
    def __init__(self, number, init_pos, font, WIDTH):
        Friend.__init__(self, number, init_pos, font)
        self.WIDTH = WIDTH
        if init_pos[0] < 400:
            self.move_mode = 0  # 向右移动
        else:
            self.move_mode = 1  # 向左

    def move(self):
        if self.move_mode == 0:
            self.rect.right += self.speed
        if self.move_mode == 1:
            self.rect.left -= self.speed
        if self.rect.left <= 0:
            self.move_mode = 0
        if self.rect.right >= self.WIDTH:
            self.move_mode = 1
        self.rect.top += self.speed/2

class FriendVari(Friend):
    def __init__(self, number, init_pos, font):
        Friend.__init__(self, number, init_pos, font)
        self.static = False
        self.threshold = 50
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count >= self.threshold:
            self.number += 1
            self.text = self.font.render(str(self.number), True, (255, 255, 255))
            self.count = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, number, init_pos, font, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.font = font
        self.text = font.render(str(number), True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = init_pos
        self.speed = 7
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def change_number(self, num):
        self.number += num
        self.text = self.font.render(str(self.number), True, (255, 255, 255))
        # self.rect = self.text.get_rect()

    def move_up(self):  #移动的时候如果要超出屏幕就不能动了
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def move_down(self):
        if self.rect.top >= self.HEIGHT - self.rect.height:
            self.rect.top = self.HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def move_right(self):
        if self.rect.left >= self.WIDTH - self.rect.width:
            self.rect.left = self.WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

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
        self.disappear = False

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

class FriendDisappear(Friend):
    def __init__(self, number, init_pos, font):
        Friend.__init__(self, number, init_pos, font)
        self.disappear = True
        self.count = 0
        self.speed = 1
        self.threshold = 50
        self.show = True

    def show_count(self):
        self.count += 1
        if self.count >= self.threshold:
            self.count = 0
            if self.show:
                self.show = False
            else:
                self.show = True

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
        self.font_list = []
        self.font_list.append(pygame.font.Font('freesansbold.ttf', 12))
        self.font_list.append(pygame.font.Font('freesansbold.ttf', 16))
        self.font_list.append(pygame.font.Font('freesansbold.ttf', 24))
        self.font_list.append(font)
        self.grow_mode = 0
        self.grow_count = 0
        self.grow_threshold = 10

    def change_font1(self):
        self.grow_count += 1
        index = self.grow_count // self.grow_threshold
        flag = self.grow_count % self.grow_threshold
        if flag == 0:
            self.text = self.font_list[index].render(str(self.number), True, (255, 255, 255))
            current_pos = self.rect.center
            self.rect = self.text.get_rect()
            self.rect.center = current_pos
        if self.grow_count > 31:
            self.grow_mode = 0
            self.grow_count = 0

    def change_font2(self):
        self.grow_count += 1
        index = self.grow_count // self.grow_threshold
        flag = self.grow_count % self.grow_threshold
        if flag == 0:
            if index % 2 == 0:
                self.text = self.font_list[0].render(str(self.number), True, (255, 255, 255))
            else:
                self.text = self.font_list[-1].render(str(self.number), True, (255, 255, 255))
            current_pos = self.rect.center
            self.rect = self.text.get_rect()
            self.rect.center = current_pos
        if self.grow_count > 31:
            self.grow_mode = 0
            self.grow_count = 0

    def change_number(self, num):
        self.number += num
        # self.text = self.font.render(str(self.number), True, (255, 255, 255))
        # current_pos = self.rect.center
        # self.rect = self.text.get_rect()
        # self.rect.center = current_pos

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

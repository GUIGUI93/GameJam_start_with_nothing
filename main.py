# -*- coding: utf-8 -*-
"""
My first game, wrote by pygame 
@author: ZHANG Chenyu
"""

import pygame
from sys import exit
from pygame.locals import *
import random
import os
import math
from gameRole import *

# 注意存放文件的文件夹命名不要有中文，不然会找不到同一个文件夹下的文件，比如gameRole
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
# initialize the game
pygame.init()
if os.name == 'posix':   # mac环境中运行必须要这么设置，不然刷新频率太低
    flags = FULLSCREEN | DOUBLEBUF
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
    screen.set_alpha(None)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.set_alpha(None)
pygame.display.set_caption('start with nothing')

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

# 开始画面
def open():
    font = pygame.font.Font('freesansbold.ttf', 24)  # 字体大小的
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        screen.fill(0)
        text1 = font.render(str("You start with nothing in your life"), True, (255, 255, 255))
        text_rect1 = text1.get_rect()
        text_rect1.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100]
        text2 = font.render(str("But you will meet different people"), True, (255, 255, 255))
        text_rect2 = text2.get_rect()
        text_rect2.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50]
        text3 = font.render(str("You should choose wisely"), True, (255, 255, 255))
        text_rect3 = text3.get_rect()
        text_rect3.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ]
        text4 = font.render(str("The one shares the same quality will make you stronger"), True, (255, 255, 255))
        text_rect4 = text4.get_rect()
        text_rect4.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50]
        text5 = font.render(str("Or else it will make you weaker, or even dead"), True, (255, 255, 255))
        text_rect5 = text5.get_rect()
        text_rect5.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100]

        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        screen.blit(text5, text_rect5)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            return

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def fail():
    font = pygame.font.Font('freesansbold.ttf', 32)  # 字体大小的
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        screen.fill(0)
        text = font.render(str("Sorry you failed, now go watch some porns"), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        screen.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def game():
    clock = pygame.time.Clock()
    player_font = pygame.font.Font('freesansbold.ttf', 32)  # 字体大小的
    friend_font = pygame.font.Font('freesansbold.ttf', 32)  # 字体大小的

    player_number = 0
    player_pos = [SCREEN_WIDTH/2, 400]
    player = Player(player_number, player_pos, player_font, SCREEN_WIDTH, SCREEN_HEIGHT)

    friend_group = pygame.sprite.Group()
    friend_frequence = 0
    friend_interval = 100

    time_count = 0
    time_threshold = 100

    while 1:
        # 控制游戏最大帧率为60
        clock.tick(60)
        # 绘制背景
        screen.fill(0)
        # screen.blit(background, (0, 0))


        if friend_frequence == friend_interval:  # 通过这个数字来确定出现的频率
            friend_pos = [random.randint(0, SCREEN_WIDTH - 50), 0]
            offset = max(10, player.number//4)
            friend_number = random.randint(max(2, player.number - offset), max(10, player.number + offset))
            choice = random.randint(0, 10)
            if choice < 6:
                friend = Friend(friend_number, friend_pos, friend_font)
            elif choice < 8:
                friend = FriendCross(friend_number, friend_pos, friend_font, SCREEN_WIDTH)
            else:
                friend = FriendVari(friend_number, friend_pos, friend_font)

            friend_group.add(friend)
            friend_frequence = 0

        else:
            friend_frequence += 1

        for friend in friend_group:
            friend.move()
            if not friend.static:
                friend.increment()
            # 判断玩家是否被击中
            if pygame.sprite.collide_rect(friend, player):
                if player.number == 0 or player.number == 1:
                    player.change_number(friend.number)
                elif is_prime(friend.number) and is_prime(player.number):
                    player.change_number(friend.number)
                elif not is_prime(friend.number) and not is_prime(player.number):
                    player.change_number(friend.number)
                else:
                    player.change_number(-friend.number)
                friend_group.remove(friend)

            if friend.rect.top > SCREEN_HEIGHT:
                friend_group.remove(friend)
            screen.blit(friend.text, friend.rect)

        # screen.blit(timeout_img, (SCREEN_WIDTH - 100, 60))
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            player.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.move_right()

        screen.blit(player.text, player.rect)

        if player.number < 0:
            fail()

        # time_count += 1
        # if time_count >= time_threshold:
        #     if player.number > 0:
        #         player.change_number(-1)
        #     time_count = 0

        # 更新屏幕
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    open()
    game()
        
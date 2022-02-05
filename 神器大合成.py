# coding = utf-8
# @author:yingzhudashu

import pygame
import sys
import random
from pygame.locals import *

# 初始化数值
size = 180
ls = [[], []]
grid = []
dir1 = [0, 4, 8, 12]
dir2 = [3, 7, 11, 15]
dir3 = [0, 1, 2, 3]
dir4 = [12, 13, 14, 15]
win = pygame.image.load('Images/WIN.PNG')
lost = pygame.image.load('Images/LOST.PNG')

#改变位置
def change(dir, n):
    ls0 = ls[1].copy()
    l0 = [grid[0],grid[0],grid[0],grid[0]]
    l1 = [0,0,0,0]
    for i in dir:
        l = 0
        for j in [i, i+n, i+n*2, i+n*3]:
            if ls[1][j] != 0:
                l0[l] = ls[0][j]
                l1[l] = ls[1][j]
                l = l + 1
        if l == 2 and l1[0] == l1[1]:
            l1[0] = l1[0] + 1
            l0[0] = grid[l1[0]]
            l = 1
        elif l == 3:
            if l1[0] == l1[1]:
                l1[0] = l1[0] + 1
                l0[0] = grid[l1[0]]
                l1[1] = l1[2]
                l0[1] = l0[2]
                l = 2
            elif l1[1] == l1[2]:
                l1[1] = l1[1] + 1
                l0[1] = grid[l1[1]]
                l = 2
        elif l == 4:
            if l1[0] == l1[1]:
                l1[0] = l1[0] + 1
                l0[0] = grid[l1[0]]
                if l1[2] == l1[3]:
                    l1[1] = l1[2] + 1
                    l0[1] = grid[l1[1]]
                    l = 2
                else:
                    l1[1] = l1[2]
                    l0[1] = l0[2]
                    l1[2] = l1[3]
                    l0[2] = l0[3]
                    l = 3
            elif l1[1] == l1[2]:
                l1[1] = l1[1] + 1
                l0[1] = grid[l1[1]]
                l1[2] = l1[3]
                l0[2] = l0[3]
                l = 3
            elif l1[2] == l1[3]:
                l1[2] = l1[2] + 1
                l0[2] = grid[l1[2]]
                l = 3
        for j in range(0, l):
            ls[0][i + j*n] = l0[j]
            ls[1][i + j*n] = l1[j]
        for j in range(l, 4):
            ls[0][i + j*n] = grid[0]
            ls[1][i + j*n] = 0
    if ls[1] == ls0:
        return -1
    else:
        return 1

#判断输赢
def judge(screen):
    if ls[1].count(11) == 1:
        return 1
    elif ls[1].count(0) == 0 and change(dir1, 1) ==  -1 and change(dir2,-1) == -1 and change(dir3, 4) == -1 and change(dir4,-4) == -1:
        return 2
    else:
        add()
        return -1

#添加新块
def add():
    x = random.choice([1, 2, 2, 2, 1, 2, 1, 1, 1, 2])
    while True:
        y = random.randint(0, 15)
        if ls[1][y] == 0:
            ls[0][y] = grid[x]
            ls[1][y] = x
            break

#显示界面
def show(screen):
    screen.fill((0, 0, 0))
    screen.blit(ls[0][0], (0, 0, size, size))
    screen.blit(ls[0][1], (0, size, size, size))
    screen.blit(ls[0][2], (0, 2 * size, size, size))
    screen.blit(ls[0][3], (0, 3 * size, size, size))
    screen.blit(ls[0][4], (size, 0, size, size))
    screen.blit(ls[0][5], (size, size, size, size))
    screen.blit(ls[0][6], (size, 2 * size, size, size))
    screen.blit(ls[0][7], (size, 3 * size, size, size))
    screen.blit(ls[0][8], (2 * size, 0, size, size))
    screen.blit(ls[0][9], (2 * size, size, size, size))
    screen.blit(ls[0][10], (2 * size, 2 * size, size, size))
    screen.blit(ls[0][11], (2 * size, 3 * size, size, size))
    screen.blit(ls[0][12], (3 * size, 0, size, size))
    screen.blit(ls[0][13], (3 * size, size, size, size))
    screen.blit(ls[0][14], (3 * size, 2 * size, size, size))
    screen.blit(ls[0][15], (3 * size, 3 * size, size, size))
    pygame.display.update()

#重置数据
def restart(screen):
    for i in range(16):
        ls[0][i] = grid[0]
        ls[1][i] = 0
    add()
    add()
    show(screen)

#主函数
def main():
    #程序初始化
    pygame.init()
    #背景音乐
    pygame.mixer.music.load('Music/ゴンチチ - 春蝉.mp3')
    pygame.mixer.music.play(-1, 0.0)
    #窗口显示
    screen = pygame.display.set_mode((4 * size, 4 * size))
    pygame.display.set_caption("神器大合成")
    #导入图片
    for i in range(12):
        s = "Images/"+str(i) + ".PNG"
        gri = pygame.image.load(s)
        grid.append(gri)
    #初始化界面
    for i in range(16):
        ls[0].append(grid[0])
        ls[1].append(0)
    add()
    add()
    show(screen)

    while True:
        for event in pygame.event.get():
            k = 0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    k = change(dir1, 1)
                elif event.key == K_DOWN:
                    k = change(dir2,-1)
                elif event.key == K_LEFT:
                    k = change(dir3, 4)
                elif event.key == K_RIGHT:
                    k = change(dir4,-4)
                elif event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_SPACE:
                    restart(screen)
                    continue
                else:
                    continue

                if k == -1 and ls[1].count(0) != 0:
                    continue
                else:
                    j = judge(screen)

                if j == 1:
                    screen.blit(win, (size * 0.5, size * 0.5, size, size))
                    pygame.display.update()
                elif j == 2:
                    screen.blit(lost, (size * 0.5, size * 0.5, size, size))
                    pygame.display.update()
                else:
                    show(screen)

if __name__ == '__main__':
    main()
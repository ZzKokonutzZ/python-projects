from perlin_noise import PerlinNoise
import pygame as pg
from math import *
from random import randint
import sys
pg.init()
noise=PerlinNoise(2,69)
t_noise=PerlinNoise(1.5,420)
grid={}
color=(70,70,255)
screen=pg.display.set_mode((600,600))
for i in range(60):
    for j in range(60) :
        grid[i,j]=pg.Vector2(cos(2*pi*(noise((i/10,j/10))+1)),sin(2*pi*(noise((i/10,j/10))+1)))
d_grid={}
for i in range(60) :
    for j in range(60) :
        d_grid[i,j]=pg.Vector2(cos(2*pi*(t_noise((i/10,j/10))+1)),sin(2*pi*(t_noise((i/10,j/10))+1)))
d_vec=pg.Vector2(0,0)
while 1 :
    screen.fill((10,10,10))
    d_vec+=(randint(0,1),randint(0,1))
    
    for i in range(60):
        for j in range(60):
            x=i+d_vec[0]
            if x>59 :
                x-=60
            if x<0 :
                x+=60
            
            y=j+d_vec[1]
            if y>59 :
                y-=60
            if y<0 :
                y+=60
            try :    
                grid[i,j]+=d_grid[x,y]/10
            except KeyError :
                print(j,y,d_vec[1])
            else :
                grid[i,j]+=d_grid[x,y]/10
            grid[i,j]=grid[i,j]/dist((0,0),(grid[i,j]))
            pg.draw.aaline(screen,color,pg.Vector2(i,j)*10+(4.5,4.5),pg.Vector2(i,j)*10+(4.5,4.5)+grid[i,j]*10)
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()
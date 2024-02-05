import pygame as pg
from math import sin, dist, sqrt
import sys
from random import random
screen=pg.display.set_mode((600,600))
x=600
y=600
pixels={}
pixels_buffer={}
for i in range(320) :
    for j in range(164) :
        pixels[i,j]=pg.Vector3(100)
for i in range(320) :
    for j in range(164) :
        pixels_buffer[i,j]=[pg.Vector3(0),0]
white=pg.Vector3(75,175,245)
while 1 :
    screen.fill((10,10,10))
    light_pos=pg.Vector3(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],200)
    for i in range(150) :
        for j in range (150) :
            r=dist((i*4+1,j*4+1),(x/2,y/2))/150
            pixel=pg.Vector3(i*4+1,j*4+1,0)
            if r<=1 :  
                pixel[2]+=sqrt(1-r**2)*150
                normal=(0.5*(dist(light_pos,pixel+(pixel-(x/2,y/2,0))/dist((x/2,y/2,0),pixel))**2-dist(light_pos,pixel)**2-1))/-(dist(light_pos,pixel))
                if normal>=0.92 :
                    pixels[i,j]=pixels_buffer[i,j][0]=white*0.6
                elif normal>= 0.6  :
                    local_normal=0.6
                    if normal==pixels_buffer[i,j][1] :
                        pixels[i,j]=pixels_buffer[i,j][0]
                        pixels_buffer[i,j][0]=pixels[i,j]
                    else :
                        pixels_buffer[i,j][1]=normal
                        if random()<((normal-local_normal)/0.32)**2 :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.6
                        else :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.5
                elif normal >=0.28 :
                    pixels[i,j]=white*0.5
                    pixels_buffer[i,j]=[pixels[i,j],1]
                elif normal>=-0.04 :
                    local_normal=-0.04
                    if normal==pixels_buffer[i,j][1] :
                        pixels[i,j]=pixels_buffer[i,j][0]
                        pixels_buffer[i,j][0]=pixels[i,j]
                    else :
                        pixels_buffer[i,j][1]=normal
                        if random()<((normal-local_normal)/0.32)**3 :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.5
                        else :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.4
                elif normal >=-0.36 :
                    pixels[i,j]=white*0.4
                    pixels_buffer[i,j]=[pixels[i,j],normal]
                elif normal >=-0.68 :
                    local_normal=-0.68
                    if normal==pixels_buffer[i,j][1] :
                        pixels[i,j]=pixels_buffer[i,j][0]
                        pixels_buffer[i,j][0]=pixels[i,j]
                    else :
                        pixels_buffer[i,j][1]=normal
                        if random()<((normal-local_normal)/0.32)**4 :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.4
                        else :
                            pixels[i,j]=pixels_buffer[i,j][0]=white*0.1
                else :
                    pixels[i,j]=white*0.1
                    pixels_buffer[i,j]=[pixels[i,j],normal]
            else :
                pixels[i,j]=white*0
                pixels_buffer[i,j]=[pixels[i,j],0]
            pg.draw.rect(screen,pixels[i,j],(i*4,j*4,4,4))
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    
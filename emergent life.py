import pygame as pg
import sys
from random import randint
from math import *
pg.init()
screen=pg.display.set_mode((600,600))
colors={}
colors[1]=(255,50,50)
colors[2]=(50,255,50)
colors[3]=(50,50,255)
colors[4]=(255,255,50)
colors[5]=(255,50,255)
colors[6]=(50,255,255)
size=3
influence=60
grid={}
x=screen.get_width()
y=screen.get_height()
for  i in range(x//(influence)+1) :
    for  j in range(y//(influence)+1) :
        grid[i,j]=[]
particles=[]
attraction={}
for i in range(1,7):
    for j in range(1,7):
        attraction[i,j]=randint(-10,10)/10
        
print(attraction)
nb_particles=400
for i in range(nb_particles):
    particles.append([pg.Vector2(randint(x/4,3*x/4),randint(y/4,3*y/4)),pg.Vector2(0,0),randint(1,6)])
while 1 :
    x=screen.get_width()
    y=screen.get_height()
    screen.fill((25,25,25))
    for  i in range(x//(influence)) :
        for  j in range(y//(influence)) :
            grid[i,j]=[]
    for i in range(nb_particles):
        grid[particles[i][0][0]//(influence),particles[i][0][1]//(influence)].append(i)
    for i in range(nb_particles) :
        near_particles=[]
        for j in range(3) :
            for k in range(3) :
                if 0<=particles[i][0][0]//influence+j-1<=x//influence and 0<=particles[i][0][1]//influence+k-1<=y//influence :
                    near_particles+=grid[particles[i][0][0]//influence+j-1,particles[i][0][1]//influence+k-1]
                    #print(grid[particles[i][0][0]//influence+j-1,particles[i][0][1]//influence+i-1])
        for j in near_particles :
            if 0!=dist(particles[i][0],particles[j][0])<=influence :
                particles[i][1]+=(particles[j][0]-particles[i][0])/dist(particles[i][0],particles[j][0])*attraction[particles[i][2],particles[j][2]]*2
                particles[i][1]+=(((particles[i][0]-particles[j][0])/dist(particles[i][0],particles[j][0]))*9/dist(particles[i][0],particles[j][0]))*4
        if dist((0,0),particles[i][1])>1 :
            particles[i][1]/=dist((0,0),particles[i][1])
        particles[i][0]+=particles[i][1]
        
        if particles[i][0][0]<0 :
            particles[i][0][0]=0
            particles[i][1][0]*=-1
        if particles[i][0][0]>x :
            particles[i][0][0]=x
            particles[i][1][0]*=-1
            
        if particles[i][0][1]<0 :
            particles[i][0][1]=0
            particles[i][1][1]*=-1
        if particles[i][0][1]>y :
            particles[i][0][1]=y
            particles[i][1][1]*=-1
        
            
        
        pg.draw.circle(screen,colors[particles[i][2]],particles[i][0],size)
        particles[i][1]*=0.9
        
        
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()
import pygame as pg
from random import randint
import sys
from math import *
pg.init()
screen=pg.display.set_mode((300,300),pg.RESIZABLE)
class randsin() :
    def __init__(self,nb_waves=1,max_magnitude=1,max_wavelength=1):
        self.magnitude_a=[]
        self.wavelength_a=[]
        self.offset_a=[]
        for i in range(nb_waves):
            self.magnitude_a.append(randint(-max_magnitude*1000,max_magnitude*1000)/1000)
            self.wavelength_a.append(randint(1,max_wavelength*1000)/1000)
            self.offset_a.append(randint(0,max_wavelength*1000)/1000)
        self.magnitude_b=[]
        self.wavelength_b=[]
        self.offset_b=[]
        for i in range(nb_waves):
            self.magnitude_b.append(randint(-max_magnitude*1000,max_magnitude*1000)/1000)
            self.wavelength_b.append(randint(1,max_wavelength*1000)/1000)
            self.offset_b.append(randint(0,max_wavelength*1000)/1000)
    def dim1(self,x):
        r=0
        for i in range(len(self.magnitude_a)) :
            r+=self.magnitude_a[i]*sin(self.wavelength_a[i]*x+self.offset_a[i])
        return r
    def dim2(self,x,y):
        r=0
        for i in range(len(self.magnitude_a)) :
            r+=self.magnitude_a[i]*sin(self.wavelength_a[i]*x+self.offset_a[i])+self.magnitude_b[i]*sin(self.wavelength_b[i]*y+self.offset_b[i])
        return r
class player():
    def __init__(self) :
        self.pos=pg.Vector3(0)
        self.fov=120*pi/180
        self.angle=[0,0]
        self.sensitivity=1
        self.screen_x=screen.get_width()
        self.center_x=self.screen_x/2
        self.screen_y=screen.get_height()
        self.center_y=self.screen_y/2
        self.cam_dist=(self.center_x)/(tan(0.5*self.fov))
        pg.mouse.set_visible(False)
        pg.mouse.set_pos(self.center_x,self.center_y)
        self.screen_origin=[-asin((self.center_x)/dist((0,0),(self.center_x,self.cam_dist))),asin(self.center_y/dist((0,0),(self.center_y,self.cam_dist))),dist((0,0,0),(self.center_x,self.center_y,self.cam_dist))]
    def update(self) :
        self.angle[0]+=atan((pg.mouse.get_pos()[0]-self.center_x)/self.cam_dist)
        self.angle[1]+=atan((pg.mouse.get_pos()[1]-self.center_y)/self.cam_dist)
        pg.mouse.set_pos(self.center_x,self.center_y)
        for event in pg.event.get() :
            if event.type==pg.KEYDOWN :
                if event.key==pg.K_UP :
                    self.pos+=pg.Vector3(cos(self.angle[0]),0,sin(self.angle[0]))
        pix_0=pg.Vector3(self.pos[0]+self.screen_origin[2]*cos(self.angle[0]+self.screen_origin[0])*cos(self.angle[1]+self.screen_origin[1]),self.pos[1]+self.screen_origin[2]*sin(self.angle[1]+self.screen_origin[1]),self.pos[2]+self.screen_origin[2]*sin(self.angle[0]+self.screen_origin[0])*cos(self.angle[1]+self.screen_origin[1]))
        vec_i=pg.Vector3(sin(self.angle[0]),0,cos(self.angle[0]))
        vec_j=pg.Vector3(cos(self.angle[0])*sin(self.angle[1]),-cos(self.angle[1]),sin(self.angle[0]*sin(self.angle[1])))
        for i in range(self.screen_x) :
            for j in range(self.screen_y) :
                pix_ij=pix_0+i*vec_i+j*vec_j
                ray=pix_ij-self.pos
                if ray[1]!=0 :
                    t=(-self.pos[1]-10)/ray[1]
                    if t>=0 :
                        pg.draw.rect(screen,(255,255,255),(i,j,1,1))
                    
pg.mouse.set_visible(False)
main=player()
noise=randsin(5,2,1)
while 1 :
    x=screen.get_width()
    y=screen.get_height()
    screen.fill((0,0,0))
    main.update()
    
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()    
    pg.display.flip()
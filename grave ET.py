import pygame as pg
import sys
import math
from random import randint
pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((1280,656),pg.RESIZABLE)
planets=[]
planet=pg.image.load("pngegg (2).png")
planet.fill((255,255,255),special_flags=pg.BLEND_RGB_MAX)
toggle=False
slide=False
offset_x=0
offset_y=0
x=screen.get_width()
y=screen.get_height()
zoom=1

def dist(a,b):
    dist=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return dist

for i in range(500) :
    c=[randint(0,x),randint(0,y)]
    planets.append([c,100000*(1/dist((x/2,y/2),(c))),[randint(0,1),randint(0,1)]])
planet.fill((100,177,255),special_flags=pg.BLEND_RGB_MIN)

while 1 :
    screen.fill((0,0,0))
    x=screen.get_width()
    y=screen.get_height()
    if toggle :
        if len(planets)>=2:
            for i in range(len(planets)) :
                for j in range(len(planets)):
                    if i!=j :
                        dist_planets=dist(planets[i][0],planets[j][0])
                        if dist_planets>0 :
                            strength = 6.67428*10**(-11)*planets[i][1]*10**3*planets[j][1]*10**3/(dist_planets*5762597.111*10**3)**2
                            sign_x=((planets[j][0][0]-planets[i][0][0])/abs(planets[j][0][0]-planets[i][0][0]))
                            sign_y=(planets[j][0][1]-planets[i][0][1])/abs(planets[j][0][1]-planets[i][0][1])
                            if sign_x!=0 :
                                slope=(planets[j][0][1]-planets[i][0][1])/(planets[j][0][0]-planets[i][0][0])
                                h=math.sqrt(1+slope**2)
                                planets[i][2][0]+=sign_x*(((strength/planets[i][1])/60)/5762597.111*10**3)/h
                                planets[i][2][1]+=sign_x*(((strength/planets[i][1])/60)/5762597.111*10**3)*slope/h
                            else :
                                planets[i][2][1]+=(((strength/planets[i][1])/60)/5762597.111*10**3)*sign_y
        for i in range(len(planets)) :
            planets[i][0][0]+=planets[i][2][0]
            planets[i][0][1]+=planets[i][2][1]
    if slide :
        add_x=(pg.mouse.get_pos()[0]-pos_0[0])/zoom
        add_y=(pg.mouse.get_pos()[1]-pos_0[1])/zoom
    else :
        add_x,add_y=0,0
    for i in range(len(planets)) :
        surf=pg.transform.scale(planet,(((planets[i][1]/((4/3)*math.pi))**(1/3)*zoom*2),(planets[i][1]/((4/3)*math.pi))**(1/3)*zoom*2))
        screen.blit(surf,((planets[i][0][0]+offset_x+add_x-x/2)*zoom+x/2-((planets[i][1]/((4/3)*math.pi))**(1/3)*zoom),(planets[i][0][1]+offset_y+add_y-y/2)*zoom+y/2-((planets[i][1]/((4/3)*math.pi))**(1/3)*zoom)))
    
    if  not toggle :
        for i in range(len(planets)) :
            pg.draw.aaline(screen,(255,0,0),((planets[i][0][0]+offset_x+add_x-x/2)*zoom+x/2,(planets[i][0][1]+offset_y+add_y-y/2)*zoom+y/2),(((planets[i][0][0]+100*(planets[i][2][0]))+offset_x+add_x-x/2)*zoom+x/2,((planets[i][0][1]+100*(planets[i][2][1]))+offset_y+add_y-y/2)*zoom+y/2))
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            if event.key==pg.K_a :
                toggle=not toggle
            if event.key==pg.K_z:
                if zoom>0 :
                    zoom-=(zoom/2)
            if event.key==pg.K_e:
                zoom+=0.01
        if event.type==pg.MOUSEBUTTONDOWN :
            if event.button==1 :
                if not slide :
                    pos_0=pg.mouse.get_pos()
                    slide=True
        if event.type==pg.MOUSEBUTTONUP :
                pos_1=pg.mouse.get_pos()
                offset_x+=(pos_1[0]-pos_0[0])/zoom
                offset_y+=(pos_1[1]-pos_0[1])/zoom
                slide=False
    pg.display.flip()
    clock.tick(60)
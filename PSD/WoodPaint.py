import pygame
from pygame.locals import *
import os
import time
"""
pic=list()

for i in range(1,1000):
    pic.append(0)
"""
pygame.init() #intialize pygame
winsize=(1000,620)#winzise turple
screen=pygame.display.set_mode(winsize,DOUBLEBUF,32)#intialize screen object
#LoadUp
bg = pygame.image.load("bg.png")
Pencil = pygame.image.load("./UIIcons/Pencil.png")
Arrow = pygame.image.load("./UIIcons/arrow.png")
Save = pygame.image.load("./UIIcons/Save.png")
Config = pygame.image.load("./UIIcons/Config.png")
Load = pygame.image.load("./UIIcons/Load.png")
self=pygame.image.load("./UIIcons/Self.png")
mainconfigwindow=pygame.image.load("./Cpnfig/configUI.png")
#fog=pygame.image.load("./Cpnfig/fog.png")
configbackground=pygame.image.load("./Cpnfig/background.png")
fb=pygame.image.load("./Cpnfig/fb.png")
gmail=pygame.image.load("./Cpnfig/gmail.png")
share=pygame.image.load("./Cpnfig/share.png")
#
woodtheme=pygame.image.load("./Cpnfig/woodtheme.png")

#frame loadup(not yet)                           

for i in range(1,75):
    exec("fr"+str(i)+"=pygame.image.load('./PSD/fir/fr ("+str(i)+").png')")
"""
for i in range(1,90):
    exec("ex"+str(i)+"=pygame.image.load('./expl/ex ("+str(i)+").png')")
"""
for i in range(10,100,5):
    exec("logo"+str(i)+"=pygame.image.load('./StartUpAnimation/"+str(i)+".png')")

#some functions
def LogoAnimation():
    for i in range(10,100,5):
        exec("screen.blit(logo"+str(i)+",(0,0))")
        time.sleep(0.05)
        pygame.display.update()
        
    time.sleep(2)
    """
    #Main NavBar camedown animation
    UIposx=[0,60,270,475,680]
    UIposy=[100,-20,-20,-20,-20]
    UInames=["Arrow","Pencil","Save","Load","Config"]
    
    Item          x   y
    Pencil        0   0
    Arrow         -   -
    Save          1   1
    Config        2   2
    Load          3   3
    camedown=1
    animation_is_active=0
    while camedown!=5:
        animation_is_active+=1
        for i in range(0,5):
            exec("screen.blit("+str(UInames[i])+",(UIposx[i],UIposy[i]))")
        pygame.display.update()
        if animation_is_active==4:
            animation_is_active=0
            UIposy[camedown]+=1
        if(UIposy[camedown]==20):
            camedown+=1
    """
        
        
        
def FireAnimation():
    pass
def ExplosionAnimation():
    pass
def Presentation():
    pass
def exit_app():
    pass

#Arrow_Handle_Animation
fire_frame_selected=1

#EventPointer
Event=False
LogoAnimation()
while(True):
    
    screen.blit(bg,(0,0))
    #TopBar Static Icons
    for i in range(0,5):
        exec("screen.blit("+str(UInames[i])+",(UIposx[i],UIposy[i]))")
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            x,y=event.pos
        if event.type==pygame.MOUSEBUTTONDOWN:
            Event=True
            print("Mouse Event get success")

    exec("screen.blit(fir"+fire_frame_selected+",(500,500))")
    fire_frame_selected+=1
    if(fire_frame_selected>=75):
        fire_frame_selected=1
    if(Arrow_Handle_Animation(x,y,"mainwindow",Event)):
        exit()
    if(Event==True):
        print("Event Passed in system") 
    Event=False
    pygame.display.update()

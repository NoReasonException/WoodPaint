import pygame
from pygame.locals import *

import os
import time

pic=list()

for i in range(1,10000):
    pic.append(0)

pygame.init() #intialize pygame
winsize=(1000,620)#winzise turple
screen=pygame.display.set_mode(winsize,DOUBLEBUF,32)#intialize screen object
#LoadUp
pygame.mouse.set_visible(0)
bg = pygame.image.load("./Background/bg.png")
#TopSidebar
newfileico = pygame.image.load("./UIIcons/newfile.png")
ArrowVertical = pygame.image.load("./UIIcons/arrowv.png")
ArrowHorizontal=pygame.image.load("./UIIcons/arrowh.png")

Save = pygame.image.load("./UIIcons/Save.png")
Config = pygame.image.load("./UIIcons/Config.png")
Load = pygame.image.load("./UIIcons/Load.png")
#LeftSidebar
self=pygame.image.load("./UIIcons/Self.png")
Bucket=pygame.image.load("./UIIcons/LeftSidebar/Bucket.png")
Brush=pygame.image.load("./UIIcons/LeftSidebar/Brush.png")
BigBrush=pygame.image.load("./UIIcons/LeftSidebar/BigBrush.png")
Eraser=pygame.image.load("./UIIcons/LeftSidebar/Erase.png")

mainconfigwindow=pygame.image.load("./Cpnfig/configUI.png")
configbackground=pygame.image.load("./Cpnfig/background.png")
fb=pygame.image.load("./Cpnfig/fb.png")
gmail=pygame.image.load("./Cpnfig/gmail.png")
share=pygame.image.load("./Cpnfig/share.png")
#
woodtheme=pygame.image.load("./Cpnfig/woodtheme.png")
self=pygame.image.load("./UIIcons/self3.png")
pencils=pygame.image.load("./UIIcons/pencils2.png")
brusharea=pygame.image.load("./UIIcons/brusharea.png")

yes=pygame.image.load("./NewFile/yes.png")
no=pygame.image.load("./NewFile/no.png")
SavePreviousIcon=pygame.image.load("./NewFile/SPF.png")
#
cursor=pygame.image.load("./Cursors/cursor.png")
cursor2=pygame.image.load("./Cursors/cursor2.png")

cursor3=pygame.image.load("./Cursors/cursor3.png")
cursor4=pygame.image.load("./Cursors/cursor4.png")



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


#Main NavBar Config
UIposx=[0,70,270,475,680]
UIposy=[100,20,20,20,20]
UInames=["ArrowVertical","newfileico","Save","Load","Config"]
"""
Item          x   y
Pencil        0   0
ArrowVertical -   -
Save          1   1
Config        2   2
Load          3   3
"""

#Main Left NavBar Config
UI_l_sposx=[30,30,30,30]
UI_l_sposy=[160,210,260,310]
UI_l_snames=["Brush","BigBrush","Bucket","Eraser"]
"""
Item          x   y
Brush         0   0
BigBrush      1   1
Bucket        2   2
Eraser        3   3
"""
#NewFileWindow Config
        
UI_n_fposx=[0,370,620,250]#first self of menu
UI_n_fposy=[0,330,330,180]#first self of menu
UI_n_fposx2=[420]#second self of menu
UI_n_fposy2=[340]#second self of menu
UI_n_fnames=["configbackground","yes","no","SavePreviousIcon"]
UI_n_fnames2=["woodtheme"]
"""
Item                    x   y
#-------------------Enviroment Items
configbackground        0   0
mainconfigwindow        1   1
#-------------------First Self Items
NULL                      2   2
NULL                      3   3
NULL                      4   4
#-------------------Second Self Items(UIbpos(x,y,names)2)
NULL                      0   0   
#
"""
def newfile():
    MenuIsActive=True
    x=0
    y=0
    Event=False
    while MenuIsActive:
        for i in range(0,len(UI_n_fnames)):
            exec("screen.blit("+UI_n_fnames[i]+",(UI_n_fposx[i],UI_n_fposy[i]))")
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                x,y=event.pos
            if event.type==pygame.MOUSEBUTTONDOWN:
                Event=True
                print("Mouse Event get success")
        if(Arrow_Handle_Animation(x,y,"newfilewindow",Event)): #so to stop the newfile menu
            MenuIsActive=False
        if Event==True:
            print("Event passed to system")
        Event=False
        print(x,y)#debug need that shit
        screen.blit(cursor,(x,y))
        pygame.display.update()
        
def save():
    pass
def load():
    pass


#ConfigWindow Config
UIcposx=[0,350,420,500,580]#first self of menu
UIcposy=[0,170,250,250,250]#first self of menu
UIcposx2=[420]#second self of menu
UIcposy2=[340]#second self of menu
UIcnames=["configbackground","mainconfigwindow","fb","gmail","share"]
UIcnames2=["woodtheme"]
"""
Item                    x   y
#-------------------Enviroment Items
configbackground        0   0
mainconfigwindow        1   1
#-------------------First Self Items
fb                      2   2
gmail                   3   3
share                   4   4
#-------------------Second Self Items(UIcpos(x,y,names)2)
woodtheme               0   0   
"""
def config():
    MenuIsActive=True
    x=0
    y=0
    Event=False
    while MenuIsActive:
        for i in range(0,len(UIcnames)):
            exec("screen.blit("+UIcnames[i]+",(UIcposx[i],UIcposy[i]))")
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                x,y=event.pos
            if event.type==pygame.MOUSEBUTTONDOWN:
                Event=True
                print("Mouse Event get success")
        if(Arrow_Handle_Animation(x,y,"configwindow",Event)): #so to stop the config menu
            MenuIsActive=False
        if Event==True:
            print("Event passed to system")
        Event=False
        screen.blit(cursor,(x,y))
        
        pygame.display.update()

typeofpointer="ArrowVertical"
def change_pointer(typeof):
    if typeof=="ArrowVertical":
        UInames[0]="ArrowVertical"
    else:
        UInames[0]="ArrowHorizontal"
def Arrow_Handle_Animation(x,y,mode,event):
    global pic
    #mode 1 = in the main window
    if mode=="mainwindow":
        if (y<=101):#only if mouse is almost in the navbar
            
            typeofpointer="ArrowVertical"
            change_pointer(typeofpointer)
            UIposy[0]=100
            if (x<=150): #when is near the brush 
                UIposx[0]=70#Go to brush and stay there
                if event==True:
                    newfile()
            elif(x<=450):#when is near the save button
                UIposx[0]=270#Go to save button and stay there
                if event==True:
                    pass
                    #save()
            elif(x<=650):#when is near to load button...
                UIposx[0]=475#Go to load button and stay there
                if event==True:
                    pass
                    #load()
            elif(x<=850):#when is near the config button
                UIposx[0]=680#go to config button and stay there
                if event==True:
                    config()
            else:
                UIposx[0]=60#Default -> brush button(because is CUTE <3 )
        else :
            typeofpointer="ArrowHorizontal"
            change_pointer(typeofpointer)
            UIposx[0]=96
            if(y>=150) and (y<=350):
                if(x<=140):
                    if(y<=200):
                        UIposy[0]=175
                        if event==True:
                            return_cursor("brush")
                    elif(y<=250):
                        UIposy[0]=230
                        if event==True:
                            return_cursor("BigBrush")
                    elif(y<=300):
                        UIposy[0]=275
                        if event==True:
                            return_cursor("Bucket")
                    elif(y<=350):
                        UIposy[0]=327
                        if event==True:
                            return_cursor("Eraser")
                            
    if mode=="configwindow":
        print(x,y)
        if (y>=200 and y <=240):
            if (x>405 and x <450):
                print("back")
                if event==True:
                    return 1
                
        if(y>=240 and y<= 310):
            if (x>=420):
                if (x<=480):
                    print("fb")
                    if event==True:
                        os.system("start https://www.facebook.com/Atticadreamer")
                elif(x<=570):
                    print("gmail")
                    if event==True:
                        os.system("start https://plus.google.com/u/0/+%CE%A3%CF%84%CE%AD%CF%86%CE%B1%CE%BD%CE%BF%CF%82%CE%A3%CF%84%CE%B5%CF%86%CE%AC%CE%BD%CE%BF%CF%851998/posts")
                elif(x<=640):
                    print("share")
                    if event==True:
                        os.system("start https://www.facebook.com")
                else:
                    print("In the background area")
                    if event==True:
                        return 1
            else:
                print("In the background area")
                if event==True:
                    return 1
            
        elif(y>=320 and y<=390) :
            if (x>=420):
                if (x<=480):
                    print("choice1")
                    if event==True:
                        pass
                elif(x<=570):
                    print("choice2")
                    if event==True:
                        pass
                elif(x<=640):
                    print("choice3")
                    if event==True:
                        pass
                else:
                    print("In the background area")
                    if event==True:
                        return 1
            else:
                print("In the background area")
                if event==True:
                    return 1
    if mode=="newfilewindow":
        print(x,y)
        if (y>=240 and y <=265):
            if (x>300 and x <350):
                print("back")
                if event==True:
                    return 1
                
        if(y>=270 and y<= 400):
            if (x>=380 and x<=440):
                print("Yes")
                if event==True:
                    print("ERROR:No code available for this")
                    return 1
            if(x>=620 and x<=680):
                    print ("NO")
                    if event==True:
                        del pic
                        pic=list()
                        for i in range(1,1000):
                            pic.append(0)
                        return 1
            else:
                print("In the background area")
                if event==True:
                    return 1
            
                #back and two down buttons code
indexoflist=0
brushsize=10
def draw_handle(x,y):
    global indexoflist
    if((x>300 and x<710) and (y>180 and y<520)):
        indexoflist+=2
        try:
            pic[indexoflist-1]=x
            pic[indexoflist-2]=y
            for i in range(1,brushsize):
                for j in range(1,brushsize):
                    indexoflist+=2
                    pic[indexoflist-1]=x+i
                    pic[indexoflist-2]=y+j
        except IndexError:
            indexoflist=0
            return

        
def color():
    return (0,0,0)

def return_cursor(typecursor):
    global cursortype
    if typecursor=="brush":
        cursortype="cursor"
    if typecursor=="BigBrush":
        cursortype="cursor2"
    if typecursor=="Bucket":
        cursortype="cursor3"
    if typecursor=="Eraser":
        cursortype="cursor4"
    

    
#mainloop
fir_fr_select=1
#EventPointer
x=0
y=0
Event=False
LogoAnimation()
cursortype="cursor"
while(True):
    
    screen.blit(bg,(0,0))
    #TopBar Static Icons
    for i in range(0,5):
        exec("screen.blit("+str(UInames[i])+",(UIposx[i],UIposy[i]))")
    #LeftBar Static Icons
    for i in range(0,4):
        exec("screen.blit("+str(UI_l_snames[i])+",(UI_l_sposx[i],UI_l_sposy[i]))")
    #LeftBar Static Icons(SELFS)
    for i in range(200,400,50):
        exec("screen.blit(self,(1,"+str(i)+"))")
    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            x,y=event.pos
        if event.type==pygame.MOUSEBUTTONDOWN:
            Event=True
            print("Mouse Event get success")
            draw_handle(x,y)
    
    screen.blit(pencils,(772,7))
    screen.blit(brusharea,(100,100))
    exec("screen.blit("+str(cursortype)+",(x,y))")
    if(Arrow_Handle_Animation(x,y,"mainwindow",Event)):
        exit()
    if(Event==True):
        print("Event Passed in system") 
    Event=False
    for i in range(2,indexoflist,2):
        screen.set_at((pic[i-1],pic[i-2]),color())
    print(x,y)
    #exec("screen.blit(fr"+str(fir_fr_select)+",(800,390))")
    fir_fr_select+=1
    if(fir_fr_select>=75):
        fir_fr_select=1
    pygame.display.update()

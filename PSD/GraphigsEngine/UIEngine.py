#!/usr/bin/python
# Filename: UIEngine.py


#Main NavBar Config
"""
UIposx=[0,60,270,475,680]
UIposy=[100,20,20,20,20]
UInames=["Arrow","Pencil","Save","Load","Config"]
#
Item          x   y
Pencil        0   0
Arrow         -   -
Save          1   1
Config        2   2
Load          3   3

#ConfigWindow Config
UIcposx=[0,350,420,500,580]#first self of menu
UIcposy=[0,170,250,250,250]#first self of menu
UIcposx2=[420]#second self of menu
UIcposy2=[340]#second self of menu
UIcnames=["configbackground","mainconfigwindow","fb","gmail","share"]
UIcnames2=["woodtheme"]

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
        
        pygame.display.update()
"""
#BrushWindow Config
UIbposx=[0,350,420,500,580]#first self of menu
UIbposy=[0,170,250,250,250]#first self of menu
UIbposx2=[420]#second self of menu
UIbposy2=[340]#second self of menu
UIbnames=["configbackground","mainconfigwindow","fb","gmail","share"]
UIbnames2=["woodtheme"]
#
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
def brush():
    MenuIsActive=True
    x=0
    y=0
    Event=False
    while MenuIsActive:
        for i in range(0,len(UIbnames)):
            exec("screen.blit("+UIbnames[i]+",(UIbposx[i],UIbposy[i]))")
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                x,y=event.pos
            if event.type==pygame.MOUSEBUTTONDOWN:
                Event=True
                print("Mouse Event get success")
        if(Arrow_Handle_Animation(x,y,"brushwindow",Event)): #so to stop the config menu
            MenuIsActive=False
        if Event==True:
            print("Event passed to system")
        Event=False
        
        pygame.display.update()
        
        


def Arrow_Handle_Animation(x,y,mode,event):
    #mode 1 = in the main window
    if mode=="mainwindow":
        if (y<=101):#only if mouse is almost in the navbar
            if (x<=150): #when is near the brush 
                UIposx[0]=60#Go to brush and stay there
                if event==True:
                    brush()
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
    if mode=="brushwindow":
        print(x,y)
        if (y>=200 and y <=240):
            if (x>405 and x <450):
                print("back")
                if event==True:
                    return 1
                
        if(y>=240 and y<= 310):
            if (x>=420):
                if (x<=480):
                    print("BrushSize")
                    if event==True:
                        pass
                elif(x<=570):
                    print("BrushType")
                    if event==True:
                        pass
                elif(x<=640):
                    print("PointerType")
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
        #back and two down buttons code
    
#mainloop
    

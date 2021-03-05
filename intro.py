import pygame
import time
import random

pygame.init()

display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MyGame')
clock=pygame.time.Clock()

game_img=pygame.image.load('car1.png')
pygame.display.set_icon(game_img)
pause=False
def car(x,y):
    gameDisplay.blit(game_img,(x,y))

def quitgame():
    pygame.QUIT
    quit()

def button(mssg,x,y,w,h,ia,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+100>mouse[0]>x and y+50>mouse[1]>y:
                    pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
                    if click[0]==1 and action!=None:
                        action()
                    
    else:
          pygame.draw.rect(gameDisplay,ia,(x,y,w,h))

    smalltext=pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect=text_object(mssg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textsurf,textrect)        

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill((255,255,255))
            largetext=pygame.font.Font('freesansbold.ttf',112)
            textsurf,textrect=text_object("Sajal's Game",largetext)
            textrect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(textsurf,textrect)

            button("Quit",550,450,100,50,(200,0,0),(255,0,0),quitgame)   
            button("Go!",150,450,100,50,(0,200,0),(0,255,0),gameloop)        

            
            pygame.display.update()
            clock.tick(15)

def unpause():
    global pause
    pause=False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill((255,255,255))
            largetext=pygame.font.Font('freesansbold.ttf',112)
            textsurf,textrect=text_object("Paused",largetext)
            textrect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(textsurf,textrect)

            button("Quit",550,450,100,50,(200,0,0),(255,0,0),quitgame)   
            button("Continue",150,450,100,50,(0,200,0),(0,255,0),unpause)        

            
            pygame.display.update()
            clock.tick(15)
            
            
         

def text_object(text,font):
    textsurface=font.render(text,True,(0,0,0,))
    return textsurface,textsurface.get_rect()
    
def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',112)
    textsurf,textrect=text_object(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf,textrect)
    
    pygame.display.update()
    time.sleep(1)
    gameloop()
    

    
def crash():
    message_display("You Crashed")
    
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    
def things1(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    
def passed(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed :" + str(count),True,(0,0,0))
    gameDisplay.blit(text,(0,0))

def gameloop():
    x=display_width*0.45
    y=display_height*0.8
    global pause

    things_startx=random.randrange(0,display_width)
    things_starty=-600
    things_height=100
    things_width=100
    things_speed=7
    x_change=0
    count=0
    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change= -5
                elif event.key==pygame.K_RIGHT:
                    x_change =5
                elif event.key==pygame.K_p:
                    pause=True
                    paused()
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x += x_change
        gameDisplay.fill((255,255,255))
        
        things(things_startx, things_starty,things_width, things_height,(0,0,0))
        
        things_starty+=things_speed
        
        car(x,y)
        passed(count) 
        
        if x<0 or x>display_width-53:
            crash()
        if things_starty>display_height:
            things_starty=0-things_height
            things_startx=random.randrange(0,display_width)
            
            count+=1
            things_speed+=0.5
           
            
            
        if y<things_height+things_starty:
            if x>things_startx and x<things_startx+things_width or x+53>things_startx and x+53<things_startx+things_width:
                crash()
            
        pygame.display.update()
        clock.tick(60)
game_intro()
gameloop()



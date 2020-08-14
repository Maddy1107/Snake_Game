#coding: utf-8
import pygame,os,time,math,sys,pygame.mixer,random
from pygame.locals import *

pygame.init()

#Setting Caption
pygame.display.set_caption("The Snake Game.")

#Display Size
display_width=800
display_height=600
new_height=550

#Colours
white=(255,255,255)
black=(0,0,0)
pink=(255,25,155)
green=(0,155,0)
grey=(50,50,50)
green2=(0,160,2)
green3=(0,255,100)
red=(200,0,0)
light_red=(255,0,0)
yellow=(255,255,0)
light_yellow=(100,255,0)
blue=(0,0,100)
light_blue=(0,0,255)

#Screen and image
screen=pygame.display.set_mode((display_width,display_height))

#Start Screen Snake
snakeimg=pygame.image.load('Snake1.png')
smallsnake=pygame.transform.scale(snakeimg,(200,150))
snakescore=pygame.transform.scale(snakeimg,(100,50))

#Over screen snake
snakesad=pygame.image.load('sadsnake.png')
snakeover=pygame.transform.scale(snakesad,(200,200))

#Apple
appleimg=pygame.image.load('apple.png')
applerotate=pygame.transform.scale(appleimg,(20,20))
AppleSize=20

#Background
bg=pygame.image.load('Grass.jpg')
bg1=pygame.transform.scale(bg,(800,550))

#Setting Icon
icon=pygame.transform.scale(appleimg,(10,10))
pygame.display.set_icon(icon)

#Snake move controller
head_x=display_width/2
head_y=new_height/2
head_x_change=0
head_y_change=0

#Timings
shift_size=10
clock=pygame.time.Clock()
FPS=20

#Style the text for over screen
smallfont = pygame.font.Font('fonts/Road_Rage.otf', 30)
largefont = pygame.font.Font('fonts/Road_Rage.otf', 70)

#Style the text for start screen
smallfont1 = pygame.font.Font('fonts/Road_Rage.otf', 30)
largefont1 = pygame.font.Font('fonts/Road_Rage.otf', 50)

#Snake Body Increase
def snake_body(shift_size,snakelist):
    #screen.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for xy in snakelist:#[:-1]:
        pygame.draw.rect(screen,green3,[xy[0],xy[1],shift_size,shift_size])

#Centering the text
def text_block(text,color,size):
    if size == 'small':
        textscr=smallfont.render(text,True,color)
        textscr=smallfont1.render(text,True,color)
    elif size == 'large':
        textscr=largefont.render(text,True,color)
        textscr=largefont1.render(text,True,color)
    return textscr,textscr.get_rect()

#Game over screen
def message(msg,color,align=0,size='small'):
    textscreen,textblock=text_block(msg,color,size)
    textblock.center= (display_width/2),(new_height/2)+align
    screen.blit(textscreen,textblock)

#Start Screen
def start_screen():
    start=True
    while start==True:
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameplay()
						
        screen.fill(green3)
        screen.blit(smallsnake,(300,20))
        message("Welcome to the Snake Game",pink,-50,'large')
        message("To score the red apples must be eaten.",black,20,'small')
        message('Each apple eaten will score 1 point.',black,70,'small')
        message('If u hit yourself or edges,you die.',black,120,'small')
        message('Press Enter to start.',black,250,'small')
        pygame.display.update()
        clock.tick(5)

#Generating apple
def apple_gen():
    rand_x=round(random.randrange(0,display_width-AppleSize))
    rand_y=round(random.randrange(0,new_height-AppleSize))
    return rand_x,rand_y

#Generating Score
def score_gen(score):
    word= smallfont.render('Score:'+ str(score), True,green2)
    screen.blit(word,(0,550))

#Pause
def pause():
    pausegame=True
    message('Paused',pink,-100,size='large')
    message('Press C to contInue or  E to exIt',black,20,size='small')
    pygame.display.update()
	
    while pausegame==True:
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        pausegame=False
                    elif event.key==pygame.K_e:
                        pygame.quit()
                        quit()
    clock.tick(5)

#Game Controller
def gameplay():
    head_x=display_width/2
    head_y=new_height/2
	
    head_x_change=10
    head_y_change=0
	
    snakelist=[]
    snakelength=1
	
    rand_x,rand_y=apple_gen()
	
    gameExit=False
    gameOver=False
	
 
	
	#Game Over Block
    while not gameExit:
	    
		#Message after hitting Boundaries
        while gameOver==True:
            screen.fill(green3)
            screen.blit(snakeover,(300,400))
            message('Game Over Asshole!!',pink,-60,size='large')
            message('Score::'+ str((snakelength-1)*100),green2,0,size='small')
            message('Press P to play agaIn or  E to exIt',black,60,size='small')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        start_screen()
                    elif event.key==pygame.K_e:
                        pygame.quit()
                        quit()

		#Key Event Block for Movement
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    head_x_change=-shift_size
                    head_y_change=0
                elif event.key==pygame.K_RIGHT:
                    head_x_change=shift_size
                    head_y_change=0
                elif event.key==pygame.K_UP:
                    head_y_change=-shift_size
                    head_x_change=0
                elif event.key==pygame.K_DOWN:
                    head_y_change=shift_size
                    head_x_change=0
                elif event.key==pygame.K_ESCAPE: 
				    pause()

        head_y+=head_y_change
        head_x+=head_x_change
		
		#Boundaries detection
        if head_x>=display_width or head_x<0 or head_y>=new_height or head_y<0:
			gameOver=True
			

        #Screen fill
        screen.fill(white)
        screen.blit(bg1,(0,0))
		
		#Score Board
        pygame.draw.rect(screen,grey,[0,550,800,50])
        screen.blit(snakescore,(700,550))
        pygame.display.update()
        
		#Placing on the screen
        screen.blit(applerotate,(rand_x,rand_y))
        snake_body(shift_size,snakelist)
        pygame.display.flip()
		
		#Snake Body
        snakehead=[]
        snakehead.append(head_x)
        snakehead.append(head_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
		    del snakelist[0]
        for blocks in snakelist[:-1]:
		   if blocks == snakehead:
		       gameOver=True   
        snake_body(shift_size,snakelist)
		
		#Calculate the score
        score_gen((snakelength-1)*100)
		
        pygame.display.update()
		
		#Eating apple
        if head_x > rand_x and head_x< rand_x+AppleSize or head_x + shift_size > rand_x and head_x + shift_size < rand_x + AppleSize:
            if head_y > rand_y and head_y< rand_y+AppleSize or head_y + shift_size > rand_y and head_y + shift_size < rand_y + AppleSize:
                rand_x,rand_y=apple_gen()
                snakelength+=1

		#Timer
        clock.tick(FPS)
    pygame.quit()
    quit()

#Start Screen Display
start_screen()

#Game starts here
gameplay()
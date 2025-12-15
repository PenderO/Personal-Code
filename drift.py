import sys, pygame
import random
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

CarBodyPreImg = pygame.image.load('CarBody.png').convert_alpha()
CarBodyImg = pygame.transform.scale(CarBodyPreImg,(CarBodyPreImg.get_width()*2,CarBodyPreImg.get_height()*2))
BodyCenter = [CarBodyImg.get_width()/2,CarBodyImg.get_height()/2]
BodyX = 100
BodyY = 200
CenterX = BodyX+BodyCenter[0]/2
CenterY = BodyY+BodyCenter[1]/2

CarFramePreImg = pygame.image.load('CarFrameFixed (1).png').convert_alpha()
CarFrameImg = pygame.transform.scale(CarFramePreImg,(CarFramePreImg.get_width()*2,CarFramePreImg.get_height()*2))
FrameCenter = [CarFrameImg.get_width()/2,CarFrameImg.get_height()/2]


TireLPreImg = pygame.image.load('Tire-1.png.png').convert_alpha()
TireLImg = pygame.transform.scale(TireLPreImg,(TireLPreImg.get_width()*2,TireLPreImg.get_height()*2))
TireLCenter = [TireLImg.get_width()/2,TireLImg.get_height()/2]

TireRPreImg = pygame.image.load('Tire-1.png.png').convert_alpha()
TireRImg = pygame.transform.scale(TireRPreImg,(TireRPreImg.get_width()*2,TireRPreImg.get_height()*2))
TireRCenter = [TireRImg.get_width()/2,TireRImg.get_height()/2]


Angle = 0

TurningLeft = False
TurningRight = False

font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('Wheel Angle: '+str(Angle), True, (255,255,255), (0,0,0))
textRect = text.get_rect()
textRect.topleft = (100, 100)

while 1:
    clock = pygame.time.Clock()
    clock.tick(60)
    screen.fill((255,255,255))
    TireLCopy = pygame.transform.rotate(TireLImg,Angle)
    TireRCopy = pygame.transform.rotate(TireRImg,Angle)
    
    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render('Wheel Angle: '+str(abs(Angle)), True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.topleft = (20, 140)

    
    BodyPos = [BodyX,BodyY]
    FramePos = [BodyX+2,BodyY+30]
    TireLPos = [BodyX+8-TireLCopy.get_width()/2, BodyY+32-TireLCopy.get_height()/2]
    TireRPos = [BodyX+66-TireRCopy.get_width()/2, BodyY+32-TireRCopy.get_height()/2]

    if TurningLeft == True:
        Angle+=1
    if TurningRight == True:
        Angle-=1
    if TurningLeft == False:
        if TurningRight == False:
            if Angle >= 0:
                Angle-=0.5
            elif Angle <= 0:
                Angle+=0.5
    if TurningRight == False:
        if TurningLeft == False:
            if Angle >= 0:
                Angle-=0.5
            elif Angle <= 0:
                Angle+=0.5


    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                TurningLeft = True

            if event.key == pygame.K_d:
                TurningRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                TurningLeft = False

            if event.key == pygame.K_d:
                TurningRight = False
        
    if Angle >= 40:
        Angle = 40
    if Angle <= -40:
        Angle = -40
    screen.blit(CarFrameImg,FramePos)
    screen.blit(TireLCopy,TireLPos)
    screen.blit(TireRCopy,TireRPos)
    screen.blit(CarBodyImg,BodyPos)
    
    screen.blit(CarFrameImg,(20+2,20+15))
    screen.blit(TireLCopy,(20+8-TireLCopy.get_width()/2, 20+16-TireLCopy.get_height()/2))
    screen.blit(TireRCopy,(20+66-TireRCopy.get_width()/2, 20+16-TireRCopy.get_height()/2))
    screen.blit(text, textRect)


    pygame.display.flip()

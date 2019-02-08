
import pygame
import time

pygame.init()

screen_width = 700
screen_height = 480

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Tik tak toe')

black = (0,0,0)
white = (255,255,255)
darkGreen = (34,139,34)

cross = pygame.image.load('cross.png')
tick = pygame.image.load('tick.jpg')

all_positions = []
cross_positions = []
tick_positions  =[]

keepgoing = True

def textOnScreen():
    font = pygame.font.SysFont("freesansbold.ttf", 40)
    text = font.render("Player-1", True, (0, 0, 205))
    screen.blit(text,(5,18))
    screen.blit(cross,(120,5))


    font = pygame.font.SysFont("freesansbold.ttf", 40)
    text = font.render("Player-2", True, (0, 0, 205))
    screen.blit(text,(5,70))
    screen.blit(tick,(120,60))
    
    pygame.display.update()


def makingOutlines():
    
    pygame.draw.rect(screen,white,[0,0,screen_width,screen_height])
    
    pygame.draw.rect(screen,black,[270,100,15,250])
    pygame.draw.rect(screen,black,[370,100,15,250])
    pygame.draw.rect(screen,black,[180,180,300,15])
    pygame.draw.rect(screen,black,[180,260,300,15])

##    pygame.draw.line(screen, (255,0,255) , (430,100), (430,360), 4)



    pygame.display.update()

makingOutlines()
textOnScreen()

def line_159():
    pygame.draw.line(screen, (255,0,255) , (445,320), (200,120), 4)
def line_357():
    pygame.draw.line(screen, (255,0,255) , (460,120), (200,330), 4)
def line_123():
    pygame.draw.line(screen, (255,0,255) , (460,140), (200,140), 4)
def line_456():
    pygame.draw.line(screen, (255,0,255) , (490,220), (170,220), 4)
def line_789():
    pygame.draw.line(screen, (255,0,255) , (490,310), (170,310), 4)
def line_147():
    pygame.draw.line(screen, (255,0,255) , (230,100), (230,360), 4)
def line_258():
    pygame.draw.line(screen, (255,0,255) , (330,100), (330,360), 4)
def line_369():
    pygame.draw.line(screen, (255,0,255) , (430,100), (430,360), 4)


def won_game():
    font = pygame.font.SysFont("freesansbold.ttf", 150)
    text = font.render("YOU WIN..!", True, (0, 0, 205))
    screen.blit(text,(130,150))
    pygame.display.update()


def tie_game():
    font = pygame.font.SysFont("freesansbold.ttf", 150)
    text = font.render("Tie Game.!", True, (128,0,0))
    screen.blit(text,(130,150))
    pygame.display.update()


def checking_win():
    win = False

##      Checking win of Cross

    
    for i in cross_positions:
        if i == 1:
            if 2 in cross_positions and 3 in cross_positions:
                win = True
                line_123()
            if 4 in cross_positions and 7 in cross_positions:
                win = True
                line_147()
            if 5 in cross_positions and 9 in cross_positions:
                win  = True
                line_159()
        elif i == 2 and 5 in cross_positions and 8 in cross_positions:
            win  = True
            line_258()
            
        elif i == 3:
            if 6 in cross_positions and 9 in cross_positions:
                win = True
                line_369()
            if 5 in cross_positions and 7 in cross_positions:
                win  = True
                line_357()
                
        elif i == 4 and 5 in cross_positions and 6 in cross_positions:
            win = True
            line_456()
        elif i == 7 and 8 in cross_positions and 9 in cross_positions:
            win = True
            line_789()


##          Checking win of Tick

    for i in tick_positions:
        if i == 1:
            if 2 in  tick_positions and 3 in tick_positions:
                win = True
                line_123()
            if 4 in tick_positions and 7 in tick_positions:
                win = True
                line_147()
            if 5 in tick_positions and 9 in tick_positions:
                win  = True
                line_159()
        elif i == 2 and 5 in tick_positions and 8 in tick_positions:
            win  = True
            line_258()
            
        elif i == 3:
            if 6 in tick_positions and 9 in cross_positions:
                win = True
                line_369()
            if 5 in tick_positions and 7 in tick_positions:
                win  = True
                line_357()
                
        elif i == 4 and 5 in tick_positions and 6 in tick_positions:
            win = True
            line_456()
        elif i == 7 and 8 in tick_positions and 9 in tick_positions:
            win = True
            line_789()
    
    return win






while keepgoing:
    for event in pygame.event.get():

        right_place = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(all_positions)%2 == 0:
                image = cross
            else:
                image = tick

            ##      Column1
            
            if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[0] <= 270:
                if pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                    right_place = True
                    number  =  1

                if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                    right_place  = True
                    number = 4

                if pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                    right_place = True
                    number  = 7

    ##      Column2
            
            if pygame.mouse.get_pos()[0] >= 285 and pygame.mouse.get_pos()[0] <= 370:
                if pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                    right_place = True
                    number = 2

                if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                    right_place = True
                    number = 5

                if pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                    right_place = True
                    number = 8


    ##      Column3
            
            if pygame.mouse.get_pos()[0] >= 385 and pygame.mouse.get_pos()[0] <= 480:
                if pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                    right_place = True
                    number = 3

                if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                    right_place = True
                    number = 6

                if pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                    right_place = True
                    number = 9
            if right_place:

                
                if number not in all_positions:


##                  Row1
                    
                    if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                        screen.blit(image,(200,110))
                        
                    if pygame.mouse.get_pos()[0] >= 285 and pygame.mouse.get_pos()[0] <= 370 and pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                        screen.blit(image,(295,110))

                    if pygame.mouse.get_pos()[0] >= 385 and pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] >= 110 and pygame.mouse.get_pos()[1] <= 180:
                        screen.blit(image,(400,110))
                        
##                  Row2
                    
                    if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                        screen.blit(image,(200,198))
                        
                    if pygame.mouse.get_pos()[0] >= 285 and pygame.mouse.get_pos()[0] <= 370 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                        screen.blit(image,(295,198))

                    if pygame.mouse.get_pos()[0] >= 385 and pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 260:
                        screen.blit(image,(400,198))

##                  Row3

                    if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                            screen.blit(image,(200,280))

                    if pygame.mouse.get_pos()[0] >= 285 and pygame.mouse.get_pos()[0] <= 370 and pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                            screen.blit(image,(295,280))

                    if pygame.mouse.get_pos()[0] >= 385 and pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] >= 275 and pygame.mouse.get_pos()[1] <= 355:
                            screen.blit(image,(400,280))

                    
                    all_positions.append(number)
                    all_positions.sort()

                    if (len(all_positions)- 1) % 2  == 0:
                        cross_positions.append(number)
                        cross_positions.sort()
                    else:
                        tick_positions.append(number)
                        tick_positions.sort()

                    checking  =  checking_win()
                    
                    if checking:
                        won_game()
                        time.sleep(2)
                        import UI.py

                    elif len(all_positions) == 9 and not checking:
                        tie_game()
                        time.sleep(2)
                        import UI.py


                    pygame.display.update()




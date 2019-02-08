import pygame
import time
## comment
pygame.init()


screen_width = 800
screen_height = 450
screen=pygame.display.set_mode((screen_width,screen_height))

pink = (255,0,255)
blue = (0, 0, 205)
white = (255,255,255)
gray = (72,209,255)

def StartButton():
    pygame.draw.rect(screen,white,[123,171,206,80])
    
    font = pygame.font.SysFont("freesansbold.ttf", 120)
    text = font.render("Start", True, blue)
    screen.blit(text,(130,170))
    
    pygame.draw.line(screen, pink , (120,170), (330,170), 4)
    pygame.draw.line(screen, pink , (120,170), (120,250), 4)
    pygame.draw.line(screen, pink , (120,250), (330,250), 4)
    pygame.draw.line(screen, pink , (330,170), (330,250), 4)

    pygame.display.update()
##    pygame.draw.line(screen, pink , (445,320), (200,120), 4)



def ExitButton():
    pygame.draw.rect(screen,white,[496,171,180,80])
    
    font = pygame.font.SysFont("freesansbold.ttf", 120)
    text = font.render("Exit", True, blue)
    screen.blit(text,(500,170))
    
    pygame.draw.line(screen, pink , (495,170), (675,170), 4)
    pygame.draw.line(screen, pink , (495,170), (495,250), 4)
    pygame.draw.line(screen, pink , (495,250), (675,250), 4)
    pygame.draw.line(screen, pink , (675,170), (675,250), 4)
##    pygame.draw.line(screen, pink , (445,320), (200,120), 4)

    pygame.display.update()


    
StartButton()
ExitButton()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[1] >= 170 and pygame.mouse.get_pos()[1] <= 250:
                if pygame.mouse.get_pos()[0] >= 120 and pygame.mouse.get_pos()[0] <= 330:
                    white = gray
                    StartButton()
                    time.sleep(0.6)

                    import  tikTakToe.py
                if pygame.mouse.get_pos()[0] >= 496 and pygame.mouse.get_pos()[0] <= 675:
                    white = gray
                    ExitButton()
                    time.sleep(0.6)
                    pygame.quit()
                    quit()
        pygame.display.update()


import pygame
pygame.init()


screen_width = 800
screen_height = 450
screen=pygame.display.set_mode((screen_width,screen_height))

pink = (255,0,255)
blue = (0, 0, 205)
white = (255,255,255)


def StartButton():
    pygame.draw.rect(screen,white,[123,171,206,80])
    
    font = pygame.font.SysFont("freesansbold.ttf", 120)
    text = font.render("Start", True, blue)
    screen.blit(text,(130,170))
    pygame.display.update()
    
    pygame.draw.line(screen, pink , (120,170), (330,170), 4)
    pygame.draw.line(screen, pink , (120,170), (120,250), 4)
    pygame.draw.line(screen, pink , (120,250), (330,250), 4)
    pygame.draw.line(screen, pink , (330,170), (330,250), 4)
##    pygame.draw.line(screen, pink , (445,320), (200,120), 4)

    pygame.display.update()



StartButton()

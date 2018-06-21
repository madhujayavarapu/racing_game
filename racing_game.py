import pygame,time

# constants

WIDTH = 800
HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
GREEN = (0,200,0)
GREY = (128,128,128)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
BLUE = (0,0,255)
BROWN = (210,105,30)

# constants
PAUSE = False


# images used in the game
playerImg = pygame.image.load('Images/car1.png')
car3 = pygame.image.load('Images/car3.png')
car4 = pygame.image.load('Images/car4.png')
baddieImage = pygame.image.load('Images/car2.png')
wallLeft = pygame.image.load('Images/left.png')
wallRight = pygame.image.load('Images/right.png')

sample = [car3, car4, baddieImage]
playerRect = playerImg.get_rect()

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Racing_game')


clock = pygame.time.Clock()

def quitGame():
    pygame.quit()
    quit()

def textObjects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
#
def messageDisplay(text,fontsize,x,y,color):
    font = pygame.font.Font('freesansbold.ttf', fontsize)
    TextSurf, TextRect = textObjects(text, font, color)
    TextRect.center = ((x/2), (y/2))
    gameDisplay.blit(TextSurf, TextRect)

def button(title,x,y,w,h,color,colorhover,bgcolor,backgroundhover,onClickAction = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, bgcolor, (x, y, w, h))
        messageDisplay(title, 20, (2 * (x + (w / 2))), (2 * (y + (h / 2))), color)

        if click[0] == 1 and onClickAction != None:
            onClickAction()

    else:
        pygame.draw.rect(gameDisplay,backgroundhover,(x, y, w, h))
        messageDisplay(title, 20, (2 * (x + (w / 2))), (2 * (y + (h / 2))), colorhover)

def unpause():
    global PAUSE
    PAUSE = False

def paused():
    global PAUSE
    while PAUSE:
        print("coming")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()

        messageDisplay('Paused',55,WIDTH-100,700,RED)

        pygame.display.update()
        clock.tick(15)

def gameIntro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitGame()
                if event.key == pygame.K_m:
                    gameLoop()

        gameDisplay.fill(BROWN)
        messageDisplay('Racing Game',55,WIDTH,600,BLACK)

        button('Start Game',(WIDTH/2)-100,(HEIGHT/2)+20,125,50,BLACK,WHITE,WHITE,BLACK,gameLoop)
        button('Quit Game',(WIDTH/2)+40,(HEIGHT/2)+20,125,50,BLACK,WHITE,WHITE,BLACK,gameLoop)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    pygame.mouse.set_visible(False)
    global PAUSE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitGame()
                if event.key == pygame.K_p:
                    PAUSE = True
                    paused()

            gameDisplay.fill(WHITE)

            messageDisplay('game starts here..',55,WIDTH,600,BLACK)
            pygame.display.update()
            clock.tick(15)

gameIntro()

pygame.quit()
quit()

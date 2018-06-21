import pygame
import time
import random


pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096)
# sounds
crash_sound = pygame.mixer.Sound('explosion.wav')

# display dimensions
display_width = 800
display_height = 800
# colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
grey= (128,128,128)

bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)
things_colors = [red,blue,black,green]

# place button in middle of the screen use this dimensions
btn_y = 400
go_btn_x = 250
quit_btn_x = 450
btn_width = 125
btn_height = 50

pause = True

score = 0

# player
car_width = 73
carImg = pygame.image.load('Images/racecar.png')

# enemies
enemyImgs = ['Images/enemy-blue.png','Images/enemy-brn.png','Images/enemy-green.png','Images/enemy-red.png','Images/enemy-yel.png']

gameDisplay = pygame.display.set_mode((display_width,display_height)) # display in which the game starts
pygame.display.set_caption("Racing") # Title of the display
pygame.display.set_icon(carImg)
clock = pygame.time.Clock() # calculate the Frames Per Second(FPS)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Dodged: "+str(count), True, white)
    gameDisplay.blit(text,(0,5))

def car(img,x,y):
    gameDisplay.blit(img, (x,y))

def textObjects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def messageDisplay(text,font_size,x,y,color):
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = textObjects(text,largeText,color)
    TextRect.center = ((x/2),(y/2))
    gameDisplay.blit(TextSurf, TextRect)
    # gameLoop()

def button(title,x,y,w,h,color,colorhover,bgcolor,bgcolorhover,onclick_action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    # print(title+" button created")
    if (x+w) > mouse[0] > x and (y+h) > mouse[1] > y:
        pygame.draw.rect(gameDisplay, bgcolor, (x,y,w,h))
        messageDisplay(title, 20, (2 * (x + (w / 2))), (2 * (y + (h / 2))), color)

        if click[0] == 1 and onclick_action != None:
            # print(title+" button clicked")
            onclick_action()

    else:
        pygame.draw.rect(gameDisplay, bgcolorhover, ( x, y, w, h ))
        messageDisplay(title, 20, (2 * (x + (w / 2))), (2 * (y + (h / 2))), colorhover)

def crashed():
    # to play the sound
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

    gameDisplay.fill(grey)
    messageDisplay('Crashed! Try Again',55,display_width,580,white)
    messageDisplay('Your Score is: '+str(score),40,display_width,700,blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Play Again", go_btn_x,btn_y,btn_width,btn_height,white,black,green,bright_green,gameLoop)
        button("Quit", quit_btn_x,btn_y,btn_width,btn_height,white,black,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

def unPause():
    pygame.mixer.music.unpause()
    global pause
    pause = False

def paused():
    pygame.mixer.music.pause()
    messageDisplay('Paused',55,display_width,700,green)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unPause()

        button("Resume", go_btn_x, btn_y, btn_width, btn_height, white, black, green, bright_green, unPause)
        button("Home", quit_btn_x, btn_y, btn_width, btn_height, white, black, red, bright_red, gameIntro)

        pygame.display.update()
        clock.tick(15)

def quitGame():
    pygame.quit()
    quit()

def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(grey)
        messageDisplay('Avoid Collision!!', 55, display_width, 700,white)

        button("Start Game",go_btn_x,btn_y,btn_width,btn_height,white,black,green,bright_green,gameLoop)
        button("Quit",quit_btn_x,btn_y,btn_width,btn_height,white,black,red,bright_red,quitGame)

        # if (go_btn_x + btn_width) > mouse[0] > go_btn_x and (btn_y + btn_height) > mouse[1] > btn_y:
        #     pygame.draw.rect(gameDisplay, green, (go_btn_x, btn_y, btn_width, btn_height))
        # else:
        #     pygame.draw.rect(gameDisplay, bright_green, (go_btn_x, btn_y, btn_width, btn_height))
        #
        # if (quit_btn_x + btn_width) > mouse[0] > quit_btn_x and (btn_y + btn_height) > mouse[1] > btn_y:
        #     pygame.draw.rect(gameDisplay, red, (quit_btn_x, btn_y, btn_width, btn_height))
        # else:
        #     pygame.draw.rect(gameDisplay, bright_red, (quit_btn_x, btn_y, btn_width, btn_height))

        # messageDisplay('GO!',20,(2*(go_btn_x+(btn_width/2))), (2*(btn_y+(btn_height/2))),black)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    global pause
    global score

    pygame.mixer.music.load('some.wav')
    pygame.mixer.music.play(-1)

    x = display_width * 0.46
    y = display_height * 0.85

    x_change = 0
    car_speed = 0

    thing_startx = random.randrange(0, display_width-car_width)
    thing_starty = -600
    thing_speed = 10
    thing_width = 73
    thing_height = 70
    thing_color = random.choice(things_colors)
    temp = random.choice(enemyImgs)
    thing_img = pygame.image.load(temp)

    score = 0

    gameExit = False

    while not gameExit:
        # button("Home", 700, 0, 80, 50, white, black, red, bright_red, game_intro())
        flag = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

            ## making the car to move around the surface...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(grey)

        car(thing_img,thing_startx,thing_starty)

        thing_starty += thing_speed

        car(carImg,x, y)

        things_dodged(score)

        if x > display_width - car_width or x < 0:
            crashed()

        # Crashing with enemies
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                if temp == 'Images/enemy-green.png':
                    score += 10
                    messageDisplay('+10',35, display_width, 700, white)
                    flag = 1
                elif temp == 'Images/enemy-blue.png':
                    if thing_speed >= 12:
                        thing_speed -= 2
                    else:
                        thing_speed = 10
                    messageDisplay('-2 speed', 35, display_width, 700, white)
                    flag = 1
                elif temp == 'Images/enemy-brn.png':
                    if score > 10:
                        score -= 10
                        messageDisplay('-10', 35, display_width, 700, white)
                    else:
			# score is 0 means we set that to 0 only..
                        score = 0
                        messageDisplay('-'+str(score), 35, display_width, 700, white)

                    flag = 1
                else:
                    crashed()

        if thing_starty > display_height or flag == 1:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - thing_width)
            temp = random.choice(enemyImgs)
            thing_img = pygame.image.load(temp)
            score += 1
            if thing_speed < 20:
                thing_speed += 1

        pygame.display.update()
        clock.tick(60) # 60 FPS


gameIntro()

pygame.quit()
quit()

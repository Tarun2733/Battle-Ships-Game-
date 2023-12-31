import pygame
import os
pygame.font.init()
pygame.mixer.init()


WIDTH , HEIGHT = 900 , 500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Battle Ships")


RED = (255,0,0)
YELLOW = (255,255,0)
BLACK_COLOR = (0,0,0,0)                                     # setting border color variable
WHITE_COLOR = (255,255,255)                                 # setting the background color variable 
Vel = 5                                                     # initialized velocity variable
FPS = 60                                                    # initializing the fps variable
BORDER = pygame.Rect(WIDTH//2 - 5 , 0 , 10 , HEIGHT)        # creating a rectangle in the middle to section the window
Bullet_vel = 7
MAX_BULLETS = 3

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)




SpaceShip_Width , SpaceShip_Height = (55,40) #setting up width and height for the spaceship

#Importing Yellow spaceship and transforming it to right orientation and size
Yellow_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 90)


#Importing the red spaceship and transforming it to the right orientation and size
Red_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Red_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')),(WIDTH,HEIGHT))


def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE ,(0,0))
    pygame.draw.rect(WIN, BLACK_COLOR, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE_COLOR)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE_COLOR)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))



    WIN.blit(Yellow_SpaceShip, (yellow.x,yellow.y))
    WIN.blit(Red_SpaceShip, (red.x,red.y))



    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet) 
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet) 



    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - Vel > 0:                                  # LEFT
        yellow.x -= Vel
    elif keys_pressed[pygame.K_d] and yellow.x + Vel + yellow.width < BORDER.x:          # RIGHT
        yellow.x += Vel
    elif keys_pressed[pygame.K_w] and yellow.y - Vel > 0:                                # UP
        yellow.y -= Vel
    elif keys_pressed[pygame.K_s] and yellow.y + Vel + yellow.height < HEIGHT - 15:      # DOWN
        yellow.y += Vel

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - Vel > BORDER.x + BORDER.width:            # LEFT
        red.x -= Vel
    elif keys_pressed[pygame.K_RIGHT] and red.x + Vel + red.width < WIDTH:               # RIGHT
        red.x += Vel
    elif keys_pressed[pygame.K_UP] and red.y - Vel > 0:                                  # UP
        red.y -= Vel  
    elif keys_pressed[pygame.K_DOWN] and red.y + Vel + red.height < HEIGHT - 15:         # DOWN
        red.y += Vel

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += Bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT)) 
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= Bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT)) 
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text=WINNER_FONT.render(text, 1, WHITE_COLOR)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2 , HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)



def main():
    #<-------------making red and yellow arguments that will be passed in the function-------------->
    red = pygame.Rect(700,300,SpaceShip_Width,SpaceShip_Height)
    yellow = pygame.Rect(100,300,SpaceShip_Width,SpaceShip_Height)


    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #red.x -= 1                              # moving the red spaceship by 1 pixel 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text =""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
#<--------function calls for the movements---------------->
        yellow_handle_movement(keys_pressed, yellow) 
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)

    main()
    

if __name__ == '__main__':
    main()

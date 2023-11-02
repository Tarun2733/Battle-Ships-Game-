import pygame
import os

WIDTH , HEIGHT = 900 , 500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Battle Ships")

WHITE_COLOR = (255,255,255) #setting the background color variable 
Vel = 5                     # initialized velocity variable
FPS = 60                    # initializing the fps variable

SpaceShip_Width , SpaceShip_Height = (55,40) #setting up width and height for the spaceship

#Importing Yellow spaceship and transforming it to right orientation and size
Yellow_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 90)


#Importing the red spaceship and transforming it to the right orientation and size
Red_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Red_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 270)

def draw_window(red,yellow):
    WIN.fill(WHITE_COLOR)
    WIN.blit(Yellow_SpaceShip, (yellow.x,yellow.y))
    WIN.blit(Red_SpaceShip, (red.x,red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:   #LEFT
        yellow.x -= Vel
    elif keys_pressed[pygame.K_d]: #RIGHT
        yellow.x += Vel
    elif keys_pressed[pygame.K_w]: #UP
        yellow.y -= Vel
    elif keys_pressed[pygame.K_s]: #DOWN
        yellow.y += Vel

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]:    #LEFT
        red.x -= Vel
    elif keys_pressed[pygame.K_RIGHT]: #RIGHT
        red.x += Vel
    elif keys_pressed[pygame.K_UP]:    #UP
        red.y -= Vel
    elif keys_pressed[pygame.K_DOWN]:  #DOWN
        red.y += Vel


def main():
    #<-------------making red and yellow arguments that will be passed in the function-------------------->
    red = pygame.Rect(700,300,SpaceShip_Width,SpaceShip_Height)
    yellow = pygame.Rect(100,300,SpaceShip_Width,SpaceShip_Height)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #red.x -= 1                              # moving the red spaceship by 1 pixel 
        
        
        keys_pressed = pygame.key.get_pressed()
#<--------function calls for the movements---------------->
        yellow_handle_movement(keys_pressed, yellow) 
        red_handle_movement(keys_pressed, red)

        draw_window(red,yellow)
    

if __name__ == '__main__':
    main()

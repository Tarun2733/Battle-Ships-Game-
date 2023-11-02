import pygame
import os

WIDTH , HEIGHT = 900 , 500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Battle Ships")

WHITE_COLOR = (255,255,255) #setting the background color variable 
FPS = 60                    # initializing the fps variable

SpaceShip_Width , SpaceShip_Height = (55,40) #setting up width and height for the spaceship

#Importing Yellow spaceship and transforming it to right orientation and size
Yellow_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 90)


#Importing the red spaceship and transforming it to the right orientation and size
Red_SpaceShip_Image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Red_SpaceShip_Image, (SpaceShip_Width,SpaceShip_Height)), 270)

def draw_window():
    WIN.fill(WHITE_COLOR)
    WIN.blit(Yellow_SpaceShip, (300,100))
    WIN.blit(Red_SpaceShip, (700,100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

if __name__ == '__main__':
    main()

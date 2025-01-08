import pygame

pygame.init()
screen=pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Heads Voleyball")
pygame.display.set_icon(pygame.image.load('pictures/icon.png'))
mrun=True
while mrun:

    pygame.display.update()

    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            mr=False
            pygame.quit()




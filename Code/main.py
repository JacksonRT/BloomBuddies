import pygame
pygame.init()

pygame.display.set_caption('Bloom Buddies')

screen = pygame.display.set_mode([800, 800])
fps = 60

def draw_window():
    screen.fill((78, 208, 225))
    pygame.display.update()


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    draw_window()


pygame.quit()
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()  # 추가

running = True
while running:
    for event in pygame.event.get():  # 추가
        if event.type == pygame.QUIT:  # 추가
            running = False
    screen.fill((255, 255, 255))     
    pygame.display.flip()
    clock.tick(80)

pygame.quit()
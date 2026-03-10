import pygame
import generator
import logic

pygame.init()
screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()

correct_answer = generator.function()
A = False
running = True

while running:
    while not A:
        answer = input("입력하세요 : ")
        A = logic.function(answer)

    print(logic.compare(answer,correct_answer))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))     
    pygame.display.flip()
    clock.tick(80)

pygame.quit()
import pygame
import random


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Rolling Simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.SysFont(None, 100)
small_font = pygame.font.SysFont(None, 40)


dice_value = 1


def draw_dice(value):
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, BLACK, (150, 150, 200, 200), 5)

    
    text = font.render(str(value), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    
    info = small_font.render("Press SPACE to Roll", True, BLACK)
    info_rect = info.get_rect(center=(WIDTH // 2, 50))
    screen.blit(info, info_rect)


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = random.randint(1, 6)

    draw_dice(dice_value)
    pygame.display.flip()

pygame.quit()
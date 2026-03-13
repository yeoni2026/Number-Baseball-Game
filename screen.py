import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def draw_background(screen):
    screen.fill(WHITE)

def draw_title(screen, font):
    title_text = font.render("숫자 야구 게임", True, BLACK)
    screen.blit(title_text, (50, 20))

def draw_instructions(screen, font):
    instruction_text = font.render("중복 없는 3자리 숫자를 맞춰보세요!", True, BLACK)
    screen.blit(instruction_text, (50, 60))

def draw_results(screen, results_list, font):
    start_y = 100
    for idx, (guess, result) in enumerate(results_list[-10:]):
        result_text = f"시도 {len(results_list) - (len(results_list[-10:]) - 1 - idx)}: {guess} -> {result}"
        text_surface = font.render(result_text, True, BLACK)
        screen.blit(text_surface, (50, start_y + idx * 30))

def draw_finished_message(screen, font, is_winner=True):
    message = "정답입니다!" if is_winner else "게임 종료"
    message_text = font.render(message, True, (255, 0, 0))
    message_rect = message_text.get_rect(center=(screen.get_width() // 2, 450))
    screen.blit(message_text, message_rect)

def get_font(size=24):
    try:
        return pygame.font.SysFont("malgungothic", size)
    except:
        return pygame.font.Font(None, size)

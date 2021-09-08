import pygame


# Display text across screen
def game_end_text(screen):
    pygame.font.init()
    my_font = pygame.font.SysFont('Times New Roman', 40)
    text_surface = my_font.render('Buzz Kill, Game Over', False, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(500 / 2, 500 / 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def keep_score(screen, counter):
    pygame.font.init()
    my_font = pygame.font.SysFont("Helvetica", 20)
    text_surface = my_font.render('Score: ' + str(counter), False, (0, 0, 0))
    screen.blit(text_surface, (0, 0))
    pass

import pygame
from Explosion import ExplosionEffects


def check_collide(buzzes, bullets, score_counter, screen, explosions):
    # Returns a dictionary containing the bullets and buzz that have collided
    # key: bullet; value: buzz
    # If collision, remove bullet
    collisions = pygame.sprite.groupcollide(bullets, buzzes, True, False)

    if collisions:
        for bullet, list_of_buzzes in collisions.items():
            # Check for collision
            for buzz in list_of_buzzes:
                # check for collision exceeding threshold
                buzz.increment_counter()
                # Delete sprite if collision exceed threshold
                if buzz.delete_image():
                    # Create an explosion using buzz's pos
                    new_explosion = ExplosionEffects(buzz, screen, 9)
                    explosions.add(new_explosion)
                    buzzes.remove(buzz)
                    score_counter += 1
                pass
            pass
    return score_counter


def check_end(character, buzzes):
    if pygame.sprite.spritecollideany(character, buzzes):
        return True
    else:
        return False

from Bullets import Bullet
from CollisionDetector import check_collide

'''Function for managing all bullet objects'''


def manage_and_update_bullets(bullets, lm_list, screen, obj, buzzes, counter, explosions):  # obj is the main character
    # Check for the max number of allowed bullets; if exceeded, no new bullets will be drawn
    # Also a total of two seconds must pass
    if len(bullets) < Bullet.max_cartridge:
        # Check for open or closed palm; no bullets if closed palm
        # Open or closed palm is check by looking at x_val of landmark 8 and 5
        if lm_list:
            # Difference greater than 5 implies lm_5 below lm_8: open palm
            if lm_list[5][2] - lm_list[8][2] > 5:
                # Create a new bullet on each iteration
                new_bullet = Bullet(screen, obj)
                # Add new bullet to existing group
                bullets.add(new_bullet)

    # For each bullet inside the group, draw the bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Delete bullets that have exited the top of the screen
    # A list of duplicated bullets are first made to avoid alternating the group list inside the for-loop
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Update all the bullet: move bullet up the screen
    bullets.update()

    # check for collision
    score_counter = check_collide(buzzes, bullets, counter, screen, explosions)

    # Return the newest score
    return score_counter
    pass

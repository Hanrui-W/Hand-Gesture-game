def manage_and_update_explosions(explosions):
    if len(explosions) > 3:
        for explosion in explosions.copy():
            explosions.remove(explosion)
            break
        pass

    # Draw the explosion
    for explosion in explosions:
        explosion.paste_on_screen()

    explosions.update()

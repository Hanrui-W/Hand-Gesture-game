from RandomBuzzGenerator import generate_meme_buzz
from Mover import check_buzz_move

'''File for managing buzzes: drawing and checking movements'''


def manage_and_update_buzz(screen, buzzes, character, debug=False):
    # Should we generate more buzz?
    generate_new = True

    # If there are buzzes
    if buzzes:
        # If last drawn buzz completely entered the screen, then create new
        for buzz in buzzes:
            if buzz.get_y_pos() < 60:
                # Generate meme buzz across the screen
                generate_new = False
    # if no buzzes yet, just draw them
    else:
        generate_meme_buzz(screen, buzzes)
        generate_new = False
        if debug:
            print("Drawing new")

    if generate_new:
        generate_meme_buzz(screen, buzzes)
        if debug:
            print("generating")

    # Draw all Buzz on screen
    for buzz in buzzes:
        buzz.paste_on_screen()
        # check whether to move left or right to chase the character
        left, right = check_buzz_move(buzz, character)
        if left:
            buzz.move_left()
        if right:
            buzz.move_right()

    # update all buzzes
    buzzes.update()

    # Delete buzzes that have exited the lower portion of the screen
    # A list of duplicated buzzes are first made to avoid alternating the group list inside the for-loop
    for buzz in buzzes.copy():
        if buzz.rect.top >= screen.get_rect().bottom:
            buzzes.remove(buzz)

    if debug:
        print(generate_new)

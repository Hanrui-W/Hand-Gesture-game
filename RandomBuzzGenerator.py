from MemeBuzz import Buzz
import random
import time

'''Meant to create a buch of meme buzz that appear randomly from top of the screen'''


def generate_meme_buzz(screen, buzzes, default_scale=7, default_rand_num=1, debug=False):
    # Create list of possible spaces
    list_of_positions = []

    # Get x and y dimensions of screen
    screen_x, screen_y = screen.get_size()

    # Generate five random buzzes at a time
    for i in range(default_rand_num):
        list_of_positions.append(random.randint(50, screen_x - 50))
        pass

    # Create a meme buzz at each position
    for each_position in list_of_positions:
        buzz = Buzz(screen, default_scale)
        buzz.set_position(each_position)
        # Add new buzz to group
        buzzes.add(buzz)

        if debug:
            print(each_position)

    if debug:
        print("finished loop")
        time.sleep(2)

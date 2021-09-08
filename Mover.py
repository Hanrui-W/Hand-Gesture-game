# A function to check where to move main character based on position of hand landmark
def check_move(cache, current, debug=False, threshold=3):
    x_val = current[0] - cache[0]
    y_val = current[1] - cache[1]

    if debug:
        print(x_val > 0, y_val > 0, x_val < 0, y_val < 0)

    # Threshold of 3 to make movement smoother
    return x_val > threshold, y_val > threshold, x_val < -threshold, y_val < -threshold


# Function for checking where to move buzz based on position of main character
def check_buzz_move(buzz, character, threshold=3, debug=False):
    if debug:
        print(buzz.get_x_pos() - character.get_x_pos() > threshold,
              buzz.get_y_pos() - character.get_y_pos() < -threshold, buzz.get_x_pos(), character.get_x_pos())

    # Stop chasing if past character
    if buzz.get_y_pos() < character.get_y_pos():
        # To chase the character, needs to know character position; set threshold for smoother action
        return buzz.get_x_pos() - character.get_x_pos() > threshold,\
               buzz.get_x_pos() - character.get_x_pos() < -threshold
    # Else, do not make any moves
    return False, False

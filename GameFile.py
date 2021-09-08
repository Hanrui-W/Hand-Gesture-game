import pygame
from pygame.sprite import Group

import cv2
import time

from HandTrackingModuel import HandDetector
from big_mouth_dude import Yawn
from ManageBullets import manage_and_update_bullets
from ExitSys import exit_pygame
from ManageBuzzes import manage_and_update_buzz
from CollisionDetector import check_end
from TextAndPrompts import game_end_text
from TextAndPrompts import keep_score
from ManageExplosions import manage_and_update_explosions

'''The main game file'''


def main(debug=False, cv_show=True):
    # Initiate a score counter
    counter = 0

    # should we end the game?
    end_game = False

    previous_time = 0
    cap = cv2.VideoCapture(1)

    detector = HandDetector(tracking_confidence=0.9, detection_confidence=0.9)

    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    yawn = Yawn(screen=screen, scale=5)

    # Cache for recording current landmarks
    cache = (0, 0)

    # Create a group object to store all bullet objects
    bullets = Group()

    # Create a group object to store all meme buzz
    buzzes = Group()

    # Create a group object to store all explosions
    explosions = Group()

    while not end_game:
        success, img = cap.read()

        img = detector.find_hands(img=img, draw=True)

        lm_list = detector.find_positions(img, draw=True, draw_finger=8)

        # Get landmark of desired finger
        if lm_list:
            current = (lm_list[8][1], lm_list[8][2])
        else:
            current = (0, 0)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 70), cv2.FONT_ITALIC, 1, (0, 0, 0), 3)

        if cv_show:
            cv2.imshow("Camera Feed", img)
            cv2.waitKey(1)

        background_color = (255, 255, 255)
        screen.fill(background_color)

        # Update explosion effects
        manage_and_update_explosions(explosions)

        # Update position according to change of hand's positions
        yawn.update(cache=cache, current=current)
        yawn.paste_on_screen()

        # Managing the bullets, including for checking for max, stop generating bullets, creating bullets and updating
        counter = manage_and_update_bullets(bullets=bullets, lm_list=lm_list, screen=screen, obj=yawn, buzzes=buzzes,
                                            counter=counter, explosions=explosions)

        # Managing meme Buzzes
        manage_and_update_buzz(screen=screen, buzzes=buzzes, character=yawn)

        # Display score
        keep_score(screen, counter)

        # Make the most recently drawn screen visible
        pygame.display.flip()

        if debug:
            print("cache: " + str(cache) + ", current: " + str(current))
            if lm_list:
                print(lm_list[5][2] - lm_list[8][2] > 0)
            print(len(bullets))

        # Update cache to current landmark
        cache = current

        # Check for key-presses that would trigger exits of pygame
        exit_pygame()

        # If end_game is true, the game terminates
        end_game = check_end(yawn, buzzes)

    while True:
        game_end_text(screen)


if __name__ == "__main__":
    main()

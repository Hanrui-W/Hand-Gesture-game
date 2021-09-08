import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.max_hands,
                                        min_detection_confidence=self.detection_confidence,
                                        min_tracking_confidence=self.tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None
        pass

    def find_hands(self, img, draw=True):

        # Flip the image
        img = cv2.flip(img, 1)
        img = cv2.flip(img, 0)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            cv2.putText(img, "Tracking...", (300, 70), cv2.FONT_ITALIC, 1, (0, 0, 0), 3)
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        else:
            cv2.putText(img, "Lost", (300, 70), cv2.FONT_ITALIC, 1, (0, 0, 0), 3)

        return img

    def find_positions(self, img, hand_id=0, draw=False, draw_finger=8):

        landmark_list = []

        if self.results.multi_hand_landmarks:
            # Extract landmarks for a particular hand of choice (First hand by default)
            target_hand = self.results.multi_hand_landmarks[hand_id]

            for idNum, lm in enumerate(target_hand.landmark):
                height, width, channel = img.shape
                center_x, center_y = int(lm.x * width), int(lm.y * height)

                # Append extracted landmark positions to list
                landmark_list.append([idNum, center_x, center_y])

                if draw:
                    if idNum == draw_finger:
                        cv2.circle(img=img, center=(center_x, center_y), radius=15, color=(255, 0, 255),
                                   thickness=cv2.FILLED)

        return landmark_list


# Dummy
def main():
    previous_time = 0
    cap = cv2.VideoCapture(1)

    detector = HandDetector(tracking_confidence=0.75, detection_confidence=0.75)

    while True:
        success, img = cap.read()

        img = detector.find_hands(img=img, draw=True)

        lms_list = detector.find_positions(img, draw=True, draw_finger=5)
        # Account for no hands found, which will give back empty list
        if lms_list:
            print(lms_list[8])

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (222, 210, 189), 3)

        cv2.imshow("image", img)
        cv2.waitKey(1)


# Will execute if program is ran as the main source code; else ignored
if __name__ == "__main__":
    main()

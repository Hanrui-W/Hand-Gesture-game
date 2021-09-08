import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

# Construct hands object for processing the image; higher confidence threshold decreases FPS
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.85, min_tracking_confidence=0.85)

# Tool for drawing landmarks
mpDraw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0

while True:
    success, img = cap.read()

    # Convert GBR to RGB for "hands" object
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Process the RGB image and return the results
    results = hands.process(imgRGB)

    # Print detected landmarks for verification purposes
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:                       # Verify the detection of the landmarks
        for handLms in results.multi_hand_landmarks:       # Extract all detected landmarks, each hand at a time
            for numID, lm in enumerate(handLms.landmark):  # Extract a list of tuples of enumerated landmarks
                # print(numID, lm)                         # Each land mark contain coord x, y, z (ratio within img)
                height, width, channel = img.shape         # Extract image's dimensions

                # Return coord of each landmark
                centerX, centerY = int(lm.x * width), int(lm.y * height)
                print(numID, centerX, centerY)

                # Mark a particular landmark inside the image
                if numID == 4:
                    cv2.circle(img, center=(centerX, centerY), radius=20, color=(255, 0, 255), thickness=cv2.FILLED)

            # Draw on original BGR image landmarks with connections
            mpDraw.draw_landmarks(img, handLms,
                                  mpHands.HAND_CONNECTIONS)

    # Calculate the frame rate
    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime

    # Display the frame rate
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (222, 210, 189), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
    pass

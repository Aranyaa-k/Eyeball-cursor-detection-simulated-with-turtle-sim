"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""


import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
cam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the cam
    _, frame = cam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"
    elif gaze.is_top():
        text = "Looking Top"
    elif gaze.is_bottom():
        text = "Looking Bottom"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 0, 255), 2)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.eye import Eye


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
link = "E:\Thi\ResFres\BIO-ID Dataset\BioID_0000.jpg";
# file_name = "BioID_0000";
# for i in range(0, 221, 1): #tên tấm hình muốn lấy
#     file = file_name + str(i);
#     while len(file) != 10:
#         file_name = file_name[:-1] #Cắt cuối chuỗi một kí tự
#         file = file_name + str(i)

    # webcam = cv2.imread(link.replace("BioID_0000", file)) 

# webcam = cv2.imread(link)

# link = "E:\Thi\ResFres\BIO-ID Dataset\BioID_0000.jpg";

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)
    # gaze.refresh(webcam)

    frame = gaze.annotated_frame() #Vẽ dấu cộng tâm mắt
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (30, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (40, 90), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (40, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)


    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
    
webcam.release()
cv2.destroyAllWindows()

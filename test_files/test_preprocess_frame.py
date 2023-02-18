import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    alpha = 1.5 # contrast control (1.0-3.0)
    beta = 50 # brightness control (0-100)
    adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    cv2.imshow("Original", frame)
    cv2.imshow("Adjusted", adjusted)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
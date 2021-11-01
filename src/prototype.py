import cv2
import imutils

cap = cv2.VideoCapture("aftotestA.mp4")

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        f_contours = []

        for c in contours:

            if cv2.contourArea(c) < 1000:
                continue
            else:
                f_contours.append(c)

        cv2.drawContours(frame, f_contours, -1, (255, 0, 0), 1)

        cv2.imshow("Thresh", thresh)
        cv2.imshow("Frane", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break



    else:
        break

cap.release()
cv2.destroyAllWindows()
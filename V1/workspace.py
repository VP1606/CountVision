import numpy as np
import time
import imutils
import cv2
from urllib.request import urlopen

url = "http://192.168.0.155:8080/shot.jpg?rnd=955360"

avg = None
video = cv2.VideoCapture("./testJ.mp4")
xvalues = list()
motion = list()
count1 = 0
count2 = 0

netCount = 0


def find_majority(k):
    myMap = {}
    maximum = ('', 0)  # (occurring element, occurrences)
    for n in k:
        if n in myMap:
            myMap[n] += 1
        else:
            myMap[n] = 1

        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n, myMap[n])

    return maximum

width = 500

while 1:
    ret, frame = video.read()
    #frameInput = urlopen(url)
    #frameProcessA = np.array(bytearray(frameInput.read()), dtype=np.uint8)
    #frame = cv2.imdecode(frameProcessA, -1)
    #flag = True
    #text = ""

    frame = imutils.resize(frame, width=500)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    (cnts, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 700:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        xvalues.append(x)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)
        tolerance = 4.7

        if (400 - tolerance) <= x <= (400 + tolerance):
            print("POS CONTACT! XVAL: " + str(x) + " TOTAL: " + str(netCount))
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (119, 3, 252), 2)
            netCount += 1

        elif (100 - tolerance) <= x <= (100 + tolerance):
            print("NEG CONTACT! XVAL: " + str(x) + " TOTAL: " + str(netCount))
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (119, 3, 252), 2)
            netCount += 1

        else:
            continue
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)

        #flag = False

    cv2.line(frame, (150, 0), (150, 1000), (0, 255, 0), 2)
    cv2.line(frame, (400, 0), (400, 1000), (0, 255, 0), 2)
    cv2.putText(frame, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(frame, "In: {}".format(count1), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    #cv2.putText(frame, "Out: {}".format(count2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(frame, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    cv2.line(binary, (150, 0), (150, 1000), (255, 255, 255), 2)
    cv2.line(binary, (400, 0), (400, 1000), (255, 255, 255), 2)
    cv2.putText(binary, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(binary, "In: {}".format(count1), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    # cv2.putText(binary, "Out: {}".format(count2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(binary, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    cv2.imshow("Frame", frame)
    #cv2.imshow("Gray", gray)
    cv2.imshow("Binary", binary)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

#video.release()
cv2.destroyAllWindows()
import numpy as np
import time
import imutils
import cv2
from urllib.request import urlopen
from dataclasses import dataclass
from enum import Enum

url = "http://192.168.0.155:8080/shot.jpg?rnd=955360"

video = cv2.VideoCapture("./testJ.mp4")

posCount = 0
negCount = 0
netCount = 0

width = 500


@dataclass
class TrackItem:
    ID: int
    xPos: int
    size: ()


unsorted = []
tracking: [TrackItem] = []

ID_Count = 0

deltaMin = 1
deltaMax = 15

while 1:
    ret, frame = video.read()
    # frameInput = urlopen(url)
    # frameProcessA = np.array(bytearray(frameInput.read()), dtype=np.uint8)
    # frame = cv2.imdecode(frameProcessA, -1)
    # flag = True
    # text = ""

    frame = imutils.resize(frame, width=500)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)

    (cnts, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 6000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)

        tolerance = 4

        centreX = x + (w / 2)

        movingRight = False

        contourID = 0

        sizeMargin = 40

        accentColor = (255, 255, 23)

        sizeLock = False

        if tracking != []:

            matched = False

            for index, tracker in enumerate(tracking):
                observedDelta = tracker.xPos - centreX

                if ((tracker.size[0] - sizeMargin) <= x <= (tracker.size[0] + sizeMargin)) and (
                        (tracker.size[1] - sizeMargin) <= y <= (tracker.size[1] + sizeMargin)) and (
                        (tracker.size[2] - sizeMargin) <= w <= (tracker.size[2] + sizeMargin)) and (
                        (tracker.size[3] - sizeMargin) <= h <= (tracker.size[3] + sizeMargin)):
                    print("Size Match")
                    sizeLock = True
                    # Red Color

                if observedDelta < 0:
                    movingRight = True
                    print("Moving Right")
                    observedDelta = observedDelta * -1

                    if deltaMin <= observedDelta <= deltaMax:
                        # Matched
                        tracking[index].xPos = centreX
                        contourID = tracker.ID
                        matched = True
                        accentColor = (0, 115, 255)
                        # Orange Color

                else:
                    if deltaMin <= observedDelta <= deltaMax:
                        # Matched
                        tracking[index].xPos = centreX
                        tracking[index].size = (x, y, w, h)
                        contourID = tracker.ID
                        matched = True
                        accentColor = (0, 115, 255)
                        # Orange Color

            if matched is False:
                # Add new Track Item
                tracking.append(TrackItem(ID_Count, centreX, (x, y, w, h)))
                contourID = ID_Count
                ID_Count += 1
                accentColor = (255, 0, 208)
                # Purple Color

        else:
            # Add new Track Item
            tracking.append(TrackItem(ID_Count, centreX, (x, y, w, h)))
            contourID = ID_Count
            ID_Count += 1
            accentColor = (255, 0, 208)
            # Purple Color

        if sizeLock is True:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "ID: {}".format(contourID), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), accentColor, 2)
            cv2.putText(frame, "ID: {}".format(contourID), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, accentColor, 2)

        if (400 - tolerance) <= centreX <= (400 + tolerance) and movingRight is True:
            print("POS CONTACT! XVAL: " + str(x) + " TOTAL: " + str(netCount))
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (119, 3, 252), 2)
            posCount += 1
            netCount += 1


        elif (100 - tolerance) <= centreX <= (100 + tolerance) and movingRight is False:
            print("NEG CONTACT! XVAL: " + str(x) + " TOTAL: " + str(netCount))
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (119, 3, 252), 2)
            negCount += 1
            netCount -= 1


        else:
            posDelta = 400 - centreX
            negDelta = 100 - centreX

            print("POS Delta: " + str(posDelta) + " NEG Delta: " + str(negDelta))

            continue
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)

        # flag = False

    cv2.line(frame, (150, 0), (150, 1000), (0, 255, 0), 2)
    cv2.line(frame, (400, 0), (400, 1000), (0, 255, 0), 2)
    cv2.putText(frame, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(frame, "POS: {}".format(posCount), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    cv2.putText(frame, "NEG: {}".format(negCount), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(frame, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    cv2.line(binary, (150, 0), (150, 1000), (255, 255, 255), 2)
    cv2.line(binary, (400, 0), (400, 1000), (255, 255, 255), 2)
    cv2.putText(binary, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(frame, "POS: {}".format(posCount), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    cv2.putText(frame, "NEG: {}".format(negCount), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(binary, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    # cv2.imshow("Gray", gray)
    cv2.imshow("Binary", binary)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# video.release()
cv2.destroyAllWindows()

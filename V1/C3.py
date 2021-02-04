import numpy as np
import time
import imutils
import cv2
import cvlib
import sys
from urllib.request import urlopen

url = "http://192.168.0.155:8080/shot.jpg?rnd=955360"

avg = None
video = cv2.VideoCapture("./testK.mp4")
xvalues = list()
motion = list()
count1 = 0
count2 = 0

netCount = 0

idCount = 0

# https://learnopencv.com/multitracker-multiple-object-tracking-using-opencv-c-python/
trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
    # Create a tracker based on tracker name
    if trackerType == trackerTypes[0]:
        tracker = cv2.legacy_TrackerBoosting.create()
    elif trackerType == trackerTypes[1]:
        tracker = cv2.legacy_TrackerMIL.create()
    elif trackerType == trackerTypes[2]:
        tracker = cv2.legacy_TrackerKCF.create()
    elif trackerType == trackerTypes[3]:
        tracker = cv2.legacy_TrackerTLD.create()
    elif trackerType == trackerTypes[4]:
        tracker = cv2.legacy_TrackerMedianFlow.create()
    elif trackerType == trackerTypes[5]:
        tracker = cv2.legacy_TrackerCSRT.create()
    elif trackerType == trackerTypes[6]:
        tracker = cv2.legacy_TrackerMOSSE.create()
    elif trackerType == trackerTypes[7]:
        tracker = cv2.legacy_TrackerCSRT.create()
    else:
        tracker = None
        print('Incorrect tracker name')
        print('Available trackers are:')
        for t in trackerTypes:
            print(t)

    return tracker

trackerType = "MOSSE"
multiTracker = cv2.legacy_MultiTracker.create()
tolerance = 50

# https://www.geeksforgeeks.org/python-displaying-real-time-fps-at-which-webcam-video-file-is-processed-using-opencv/
# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

width = 500

def ToleranceCheck(targ, box):
    match = True

    for i in range(1, 4):
        if (box[i] - 10) <= targ[i] <= (box[i] + 10):
            continue
        else:
            match = False
            delta = targ[i] - box[i]
            print("fail Delta: " + str(delta))

    return match

while 1:
    ret, frame = video.read()
    #frameInput = urlopen(url)
    #frameProcessA = np.array(bytearray(frameInput.read()), dtype=np.uint8)
    #frame = cv2.imdecode(frameProcessA, -1)
    #flag = True
    #text = ""

    new_frame_time = time.time()

    # Calculating the fps

    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # converting the fps into integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)

    newBoxes = []
    frameEmpty = True

    frame = imutils.resize(frame, width=500)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    _, boxes = multiTracker.update(frame)

    (cnts, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 6000:
            continue

        frameEmpty = False
        (x, y, w, h) = cv2.boundingRect(c)
        xvalues.append(x)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)

        targRect = cv2.boundingRect(c)
        trackLock = False

        for box in boxes:

            #if (targRect == box).any():
                #print("MATCH! TargRect: " + str(targRect) + " Box: " + str(box))
                #print(targRect[0])
                #trackLock = True

            trackLock = ToleranceCheck(targRect, box)

        if trackLock is True:
            print("TRACK LOCK")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (97, 235, 52), 2)

        if trackLock is False:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)
            multiTracker.add(createTrackerByName(trackerType), frame, targRect)
            print("Tracker Added")

    if frameEmpty is True:
        continue

    cv2.line(frame, (150, 0), (150, 1000), (0, 255, 0), 2)
    cv2.line(frame, (400, 0), (400, 1000), (0, 255, 0), 2)
    cv2.putText(frame, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(frame, "In: {}".format(count1), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    #cv2.putText(frame, "Out: {}".format(count2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(frame, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)
    cv2.putText(frame, "FPS: {}".format(fps), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    cv2.line(binary, (150, 0), (150, 1000), (255, 255, 255), 2)
    cv2.line(binary, (400, 0), (400, 1000), (255, 255, 255), 2)
    cv2.putText(binary, "CAPRA LAKE COUNT AI 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)
    cv2.putText(binary, "In: {}".format(count1), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (116, 255, 23), 2)
    # cv2.putText(binary, "Out: {}".format(count2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 23, 255), 2)
    cv2.putText(binary, "NET: {}".format(netCount), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)
    cv2.putText(frame, "FPS: {}".format(fps), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 23), 2)

    #cv2.imshow("Gray", gray)
    cv2.imshow("Binary", binary)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

#video.release()
cv2.destroyAllWindows()
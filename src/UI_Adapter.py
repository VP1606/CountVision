def RUN(count, UI):
    import imutils
    import cv2
    from urllib.request import urlopen
    from dataclasses import dataclass
    import JSON_Contractor

    video = cv2.VideoCapture("./testJ.mp4")

    mode = JSON_Contractor.VideoMode()
    print(mode)

    if mode == "VIDEO":
        print("VIDEO MODE")
        video = cv2.VideoCapture("./testJ.mp4")

    elif mode == "WEBCAM":
        print("WEBCAM MODE")
        port = JSON_Contractor.CamPort()
        video = cv2.VideoCapture(port)

    elif mode == "IP":
        print("IP MODE")
        IP_Address = JSON_Contractor.IP_URLPull()
        video = cv2.VideoCapture(IP_Address)

    else:
        print("Defaulting to VIDEO MODE")
        video = cv2.VideoCapture("./testJ.mp4")

    #count = 0

    width = 500

    @dataclass
    class TrackItem:
        ID: int
        xPos: int
        size: ()

    tracking: [TrackItem] = []

    ID_Count = 0

    deltaMin = JSON_Contractor.DeltaRead()["min"]
    deltaMax = JSON_Contractor.DeltaRead()["max"]

    def ValidContourCount(cnts):
        count = 0

        for c in cnts:
            if cv2.contourArea(c) < 6000:
                continue
            count += 1

        return count

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

        if ValidContourCount(cnts) == 0:
            print("No Contours - Resetting Systems")
            tracking = []
            ID_Count = 0

        else:
            for c in cnts:
                if cv2.contourArea(c) < 6000:
                    continue
                (x, y, w, h) = cv2.boundingRect(c)

                tolerance = 4

                centreX = x + (w / 2)

                movingRight = False

                contourID = 0

                sizeMargin = 25

                accentColor = (255, 255, 23)

                sizeLock = False

                distanceDelta = 0

                if tracking != []:

                    matched = False

                    for index, tracker in enumerate(tracking):
                        observedDelta = tracker.xPos - centreX
                        distanceDelta = observedDelta

                        print(observedDelta)

                        if ((tracker.size[0] - sizeMargin) <= x <= (tracker.size[0] + sizeMargin)) and (
                                (tracker.size[1] - sizeMargin) <= y <= (tracker.size[1] + sizeMargin)) and (
                                (tracker.size[2] - sizeMargin) <= w <= (tracker.size[2] + sizeMargin)) and (
                                (tracker.size[3] - sizeMargin) <= h <= (tracker.size[3] + sizeMargin)):
                            print("Size Match")
                            sizeLock = True
                            observedDelta = tracker.xPos - centreX
                            distanceDelta = observedDelta
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

                                distanceDelta = observedDelta * -1

                        else:
                            movingRight = False
                            if deltaMin <= observedDelta <= deltaMax:
                                # Matched
                                tracking[index].xPos = centreX
                                tracking[index].size = (x, y, w, h)
                                contourID = tracker.ID
                                matched = True
                                accentColor = (0, 115, 255)
                                # Orange Color

                                distanceDelta = observedDelta

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

                    def directionStr():
                        if movingRight is True:
                            return "POS +"
                        else:
                            return "NEG -"

                if sizeLock is True:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(frame,
                                "ID: " + str(contourID) + " DIR: " + directionStr() + " DELTA: " + str(distanceDelta),
                                (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), accentColor, 2)
                    cv2.putText(frame,
                                "ID: " + str(contourID) + " DIR: " + directionStr() + " DELTA: " + str(distanceDelta),
                                (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                if (400 - tolerance) <= centreX <= (400 + tolerance):
                    print("POS CONTACT! XVAL: " + str(x) + " TOTAL: " + str(count))
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (119, 3, 252), 2)
                    count += 1
                    UI.countText.setText(str(count))

                    import websender
                    import asyncio
                    asyncio.get_event_loop().run_until_complete(websender.send_json({
                        "count": count
                    }))


                else:
                    posDelta = 400 - centreX
                    negDelta = 100 - centreX

                    print("POS Delta: " + str(posDelta) + " NEG Delta: " + str(negDelta))

                    continue
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 23), 2)

        cv2.line(frame, (400, 0), (400, 1000), (0, 255, 0), 2)

        cv2.putText(frame, "CAPRA LAKE COUNT VISION 2021.04.05", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 2)
        cv2.putText(frame, "COUNT", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, "{}".format(str(count)), (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 255, 255), 2)

        # cv2.line(binary, (400, 0), (400, 1000), (255, 255, 255), 2)
        # cv2.putText(binary, "CAPRA LAKE COUNT VISION 2021.04.05", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 2)

        # cv2.imshow("Gray", gray)
        # cv2.imshow("Binary", binary)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # video.release()
    cv2.destroyAllWindows()

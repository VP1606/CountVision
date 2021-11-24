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